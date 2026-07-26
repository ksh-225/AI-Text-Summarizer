from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import re 
import json
import queue
import threading
import asyncio
from fastapi.templating import Jinja2Templates # UI
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Text Summarizer App", description="Text Summarization using T5", version="1.0")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load T5 model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("./saved_summary_model")
tokenizer = T5Tokenizer.from_pretrained("./saved_summary_model")

# Choose execution device
if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

model.to(device)

# Configure Jinja2 templates directory
templates = Jinja2Templates(directory=".")

class DialogueInput(BaseModel):
    dialogue: str
    mode: str = "Executive Summary"

def clean_data(text):
    text = re.sub(r"\r\n", " ", text) # lines
    text = re.sub(r"\s+", " ", text) # spaces
    text = re.sub(r"<.*?>", " ", text) # html tags <p> <h1>
    text = text.strip().lower()
    return text

def summarize_dialogue(dialogue: str, mode: str = "Executive Summary") -> str:
    cleaned = clean_data(dialogue)
    prompt = "summarize: " + cleaned
    
    max_len = 150
    min_len = 30
    length_penalty = 2.0
    
    if mode == "TL;DR":
        max_len = 60
        min_len = 10
    elif mode == "Bullet Points":
        max_len = 120
        min_len = 30
    elif mode == "Executive Summary":
        max_len = 200
        min_len = 50
        
    inputs = tokenizer(
        prompt,
        padding="max_length",
        max_length=512,
        truncation=True,
        return_tensors="pt"
    ).to(device)
    
    model.to(device)
    targets = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=max_len,
        min_length=min_len,
        num_beams=4,
        length_penalty=length_penalty,
        early_stopping=True
    )
    
    summary = tokenizer.decode(targets[0], skip_special_tokens=True)
    if mode == "Bullet Points":
        sentences = re.split(r'(?<=[.!?])\s+', summary)
        bullets = [f"• {s.capitalize()}" for s in sentences if s.strip()]
        summary = "\n".join(bullets)
    return summary

# API Endpoints
@app.post("/summarize/")
async def summarize(dialogue_input: DialogueInput):
    summary = summarize_dialogue(dialogue_input.dialogue, dialogue_input.mode)
    return {"summary": summary}

@app.post("/api/summarize-stream")
async def summarize_stream(dialogue_input: DialogueInput):
    async def event_generator():
        event_queue = queue.Queue()
        
        def run_inference():
            try:
                # 1. Clean
                event_queue.put({"status": "cleaning", "progress": 10})
                cleaned = clean_data(dialogue_input.dialogue)
                
                # 2. Setup prompt and parameters based on mode
                prompt = "summarize: " + cleaned
                
                max_len = 150
                min_len = 30
                length_penalty = 2.0
                
                if dialogue_input.mode == "TL;DR":
                    max_len = 60
                    min_len = 10
                elif dialogue_input.mode == "Bullet Points":
                    max_len = 120
                    min_len = 30
                elif dialogue_input.mode == "Executive Summary":
                    max_len = 200
                    min_len = 50
                
                # 3. Tokenize
                event_queue.put({"status": "tokenizing", "progress": 20})
                inputs = tokenizer(
                    prompt,
                    padding="max_length",
                    max_length=512,
                    truncation=True,
                    return_tensors="pt"
                ).to(device)
                
                event_queue.put({"status": "generating", "progress": 30})
                
                # 4. Generate with progress tracking logits processor
                step_count = 0
                from transformers import LogitsProcessorList, LogitsProcessor
                
                class ProgressProcessor(LogitsProcessor):
                    def __call__(self, input_ids, scores):
                        nonlocal step_count
                        step_count += 1
                        # progress goes from 30% to 90%
                        prog = min(90, 30 + int((step_count / max_len) * 60))
                        event_queue.put({"status": f"generating (step {step_count})", "progress": prog})
                        return scores
                
                model.to(device)
                targets = model.generate(
                    input_ids=inputs["input_ids"],
                    attention_mask=inputs["attention_mask"],
                    max_length=max_len,
                    min_length=min_len,
                    num_beams=4,
                    length_penalty=length_penalty,
                    early_stopping=True,
                    logits_processor=LogitsProcessorList([ProgressProcessor()])
                )
                
                # 5. Decode
                event_queue.put({"status": "decoding", "progress": 95})
                summary = tokenizer.decode(targets[0], skip_special_tokens=True)
                
                if dialogue_input.mode == "Bullet Points":
                    sentences = re.split(r'(?<=[.!?])\s+', summary)
                    bullets = [f"• {s.capitalize()}" for s in sentences if s.strip()]
                    summary = "\n".join(bullets)
                
                event_queue.put({"status": "complete", "progress": 100, "summary": summary})
            except Exception as e:
                event_queue.put({"status": "error", "progress": 100, "error": str(e)})

        # Run inference in a background thread
        thread = threading.Thread(target=run_inference)
        thread.daemon = True
        thread.start()
        
        while True:
            try:
                # Retrieve items from queue
                event = event_queue.get(timeout=0.05)
                yield f"data: {json.dumps(event)}\n\n"
                if event["status"] in ["complete", "error"]:
                    break
            except queue.Empty:
                await asyncio.sleep(0.05)
                if not thread.is_alive() and event_queue.empty():
                    break
                    
    return StreamingResponse(event_generator(), media_type="text/event-stream")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")