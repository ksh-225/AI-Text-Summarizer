---
name: Synthetic Intelligence Interface
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#ccc3d8'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#958da1'
  outline-variant: '#4a4455'
  surface-tint: '#d2bbff'
  primary: '#d2bbff'
  on-primary: '#3f008e'
  primary-container: '#7c3aed'
  on-primary-container: '#ede0ff'
  inverse-primary: '#732ee4'
  secondary: '#4cd7f6'
  on-secondary: '#003640'
  secondary-container: '#03b5d3'
  on-secondary-container: '#00424e'
  tertiary: '#4edea3'
  on-tertiary: '#003824'
  tertiary-container: '#007650'
  on-tertiary-container: '#76ffc2'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#eaddff'
  primary-fixed-dim: '#d2bbff'
  on-primary-fixed: '#25005a'
  on-primary-fixed-variant: '#5a00c6'
  secondary-fixed: '#acedff'
  secondary-fixed-dim: '#4cd7f6'
  on-secondary-fixed: '#001f26'
  on-secondary-fixed-variant: '#004e5c'
  tertiary-fixed: '#6ffbbe'
  tertiary-fixed-dim: '#4edea3'
  on-tertiary-fixed: '#002113'
  on-tertiary-fixed-variant: '#005236'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  mono-label:
    fontFamily: Space Grotesk
    fontSize: 11px
    fontWeight: '400'
    lineHeight: '1.0'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
  container-max: 1200px
---

## Brand & Style

The design system embodies a high-fidelity, futuristic aesthetic that merges the precision of aerospace interfaces with the refined minimalism of premium consumer electronics. It is engineered for a "Cyberpunk-meets-Apple" experience: dark, atmospheric, and technically sophisticated, yet impeccably clean and accessible.

The visual narrative is built on **Glassmorphism** and **High-Contrast Minimalism**. It utilizes deep obsidian surfaces, ultra-thin glowing strokes, and vibrant light-emission effects to create a sense of depth and intelligence. The emotional response is one of "calm power"—an advanced AI tool that feels both cutting-edge and effortlessly simple to operate.

## Colors

This design system operates exclusively in a deep-space dark mode. The palette is anchored by an absolute black base to maximize the "pop" of luminous accents.

- **Primary (Electric Violet):** Used for primary actions, AI processing states, and focal points.
- **Secondary (Cyan):** Used for data visualization, links, and secondary interactive elements.
- **Tertiary (Neon Emerald):** Reserved for success states, completed summaries, and "Active" status indicators.
- **Surface Strategy:** Backgrounds utilize `#050505`. Elevated surfaces use semi-transparent glass layers with a `backdrop-filter: blur(12px)`.
- **Glow Accents:** Borders are typically 1px wide, utilizing low-opacity versions of the accent colors to simulate a light-leak or neon-tube effect.

## Typography

The typography strategy focuses on a high-tech, geometric rhythm. **Space Grotesk** provides a technical, slightly industrial feel for headings and data labels, while **Plus Jakarta Sans** ensures the summarized text remains highly legible and warm.

- **Tracking:** Headlines use tight letter-spacing for a modern "locked-up" look. Small labels and "metadata" use increased tracking (0.1em) and uppercase styling to evoke a digital HUD (Heads-Up Display) aesthetic.
- **Contrast:** High hierarchy is achieved through weight variance rather than color, maintaining the monochrome-plus-accent theme.

## Layout & Spacing

The design system follows a 4px hard grid with a fluid 12-column layout for desktop. 

- **Density:** High whitespace is critical to prevent the dark UI from feeling claustrophobic. Components are spaced generously to allow the "glow" of borders to breathe.
- **Grid:** Use a fixed-width central container (1200px) for the primary reading experience.
- **Responsive Behavior:** On mobile, margins shrink to 16px, and glassmorphic cards stack vertically with increased vertical padding to maintain touch targets.

## Elevation & Depth

Depth is not communicated through traditional shadows, but through **Tonal Layering and Opacity**.

- **Level 0 (Base):** Solid `#050505`.
- **Level 1 (Cards/Panels):** `rgba(20, 20, 20, 0.4)` with `backdrop-filter: blur(12px)`.
- **Level 2 (Overlays/Modals):** `rgba(30, 30, 30, 0.8)` with a more intense blur (24px).
- **Edge Treatment:** Every elevated surface must have a 1px border. Use `linear-gradient(135deg, rgba(255,255,255,0.1), rgba(255,255,255,0.02))` for neutral containers, or a themed gradient (e.g., Violet to Transparent) for active elements.

## Shapes

The shape language is "Calculated Softness." Elements utilize a 0.5rem (8px) base radius which feels modern and intentional—not as aggressive as sharp corners, but more disciplined than full pills.

- **Inputs/Cards:** 8px (Rounded).
- **Action Buttons:** 12px (Rounded-LG) to distinguish them from structural elements.
- **Indicators:** Circles or very small 2px radii for a "micro-chip" feel.

## Components

### Buttons
- **Primary:** Shimmering gradient background (`#7C3AED` to `#06B6D4`). Hover state triggers a `box-shadow: 0 0 20px rgba(124, 58, 237, 0.4)`.
- **Ghost:** Transparent background with a 1px glowing border. Text uses the accent color.

### AI Status Badges
- Small, pill-shaped elements with a 4px "breathing" dot (CSS animation: opacity 0.4 to 1.0).
- Neon Emerald for "AI Ready", Electric Violet for "Processing".

### Summarization Cards
- Glassmorphic panels with `backdrop-filter: blur(12px)`. 
- Top-left corner features a "Micro-label" (e.g., "VERIFIED SOURCE") in Space Grotesk 11px.

### Mode Selector
- A segmented control (pill) where the active state is a sliding glass layer with a 2px neon underline or "glow" behind the text.

### Input Fields
- Dark background (`#000000`) with a subtle inner-glow on focus. The cursor is stylized as a thick neon block or a pulsing line.