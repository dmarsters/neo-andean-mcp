# Neo-Andean Aesthetic MCP Server

A unified aesthetic enhancement server covering both **architectural (cholet)** and **fashion (cholita)** domains of Neo-Andean design. Built on a shared 5D coordinate space derived from Aymara textile traditions, Tiwanaku iconography, and contemporary El Alto visual culture.

## Why One Server

The Neo-Andean aesthetic originates in textile — aguayo weave patterns, natural dye palettes, geometric constraints from loom structure. Freddy Mamani scaled those patterns up to architectural facades. Cholita haute couture layers them onto the body. The underlying taxonomy is the same; only the output vocabulary differs.

A single server with a `domain` parameter avoids duplicating the coordinate space, color system, symbolic elements, and geometric constraints across two nearly-identical servers. The **textile-to-architecture functor** is bidirectional: weave → garment → facade, with structure-preserving mappings at each scale transition.

## Architecture

Three-layer cost-optimization pattern:

| Layer | Function | LLM Cost |
|-------|----------|----------|
| **Layer 1** | Pure taxonomy lookup — coordinate axes, symbols, palettes, visual vocabulary | 0 tokens |
| **Layer 2** | Deterministic mapping — coordinate→vocabulary, distance, trajectory, intent decomposition | 0 tokens |
| **Layer 3** | Structured enhancement data — full pipeline output for Claude synthesis | ~100-200 tokens |

## 5D Coordinate Space

| Axis | Low (0.0) | High (1.0) | Midpoint |
|------|-----------|------------|----------|
| **chacha_warmi** | Angular, stepped, rectilinear | Organic, curved, flowing | Sacred balance — Tiwanaku duality |
| **chromatic_intensity** | Earth-tone stone palette | Neon, LED, electric saturated | Whiphala flag spectrum |
| **symbolic_density** | Geometric-only, abstract | Fully iconographic, zoomorphic | Stylized chakana patterns |
| **scale_register** | Textile weave, thread-level | Monumental facade, skyline | Garment/body — the cholita pollera |
| **temporal_composite** | Pre-Columbian archaeological | Contemporary Mamani futurism | Colonial-era hybridization |

The **temporal_composite** axis is structurally unique: it represents multiple historical periods coexisting simultaneously rather than a simple old-to-new spectrum. A cholita outfit is itself a temporal composite — pre-Columbian textile geometry + Spanish colonial silhouettes + British bowler hat + contemporary global fabrics — all present at once.

## Domains

### Architecture

The cholet typology organizes vertically:

- **Ground floor** — Commercial stalls, street-facing, public/transactional
- **Event hall** — Second floor ballroom, maximum ornamental saturation, social/performative
- **Residence** — Upper floors, chalet-style, private/intimate
- **Rooftop** — Penthouse or sculptural crown, identity signal

Visual vocabulary includes facade elements (stepped gables, circular windows, polychrome panels), interior elements (neon-lit cornices, mirrored columns, geometric ceilings), and compositional geometry (bilateral symmetry, radial burst, nested frames).

### Fashion

The cholita garment system follows an isomorphic three-zone layering:

- **Outer signal** — Sombrero, manta, joyas → the facade. Public identity and status.
- **Middle performative** — Pollera, blusa → the event hall. Maximum visual presence.
- **Inner structural** — Enaguas (petticoats) → the skeleton. Invisible but defines the silhouette.

Eight garment elements are individually parameterized with chacha_warmi ratings, material options, and compositional roles. Each element carries position semiotics (bowler hat angle = marital status) that parallel the cholet's facade signaling.

## Canonical States

Ten reference points spanning the full aesthetic range:

| State | Description | Key Coordinates |
|-------|-------------|-----------------|
| `tiwanaku_stone` | Archaeological pre-Columbian, monolithic carved stone | cw=0.2, ci=0.1, tc=0.0 |
| `aguayo_weave` | Traditional textile, geometric grid, natural dye palette | cw=0.5, ci=0.4, tc=0.2 |
| `colonial_hybrid` | Spanish silhouettes infused with Andean color | cw=0.4, ci=0.3, tc=0.5 |
| `gran_poder_festival` | Maximum performative display, full cholita regalia | cw=0.7, ci=0.8, tc=0.7 |
| `mamani_facade` | Classic Freddy Mamani cholet exterior | cw=0.5, ci=0.75, tc=0.8 |
| `event_hall_interior` | Cholet ballroom, neon, mirrors, geometric ceiling | cw=0.6, ci=0.95, tc=0.9 |
| `cholita_haute` | Contemporary high-fashion cholita, vicuña wool | cw=0.7, ci=0.6, tc=0.8 |
| `abundance_principle` | Recursive "always more" — maximum ornamental saturation | cw=0.5, ci=0.9, tc=0.7 |
| `el_altopia_futurism` | Speculative Neo-Andean future, digital aguayo | cw=0.5, ci=1.0, tc=1.0 |
| `crucero_de_los_andes` | Mamani's evolution beyond cholet — the silver ship | cw=0.6, ci=0.5, tc=1.0 |

## Tools

### Layer 1 — Taxonomy Lookup (7 tools)

- **`get_coordinate_axes`** — 5D space definition with axis descriptions and labels
- **`get_geometric_constraints`** — Andean angle constraints (45°/90°/135°) and form vocabularies
- **`get_symbolic_elements`** — Tiwanaku iconography with geometry, meaning, and density ratings
- **`get_color_palette`** — Five palettes organized by chromatic intensity, with hex values and cultural sources
- **`get_visual_vocabulary`** — Domain-specific element lists, typologies, and compositional geometry
- **`get_canonical_states`** — Ten reference states with full 5D coordinates
- **`get_server_info`** — Server metadata and capability summary

### Layer 2 — Deterministic Computation (5 tools)

- **`map_coordinates`** — Maps 5D coordinates → geometry, palette, symbols, and domain vocabulary
- **`decompose_intent`** — Natural language → 5D coordinates via keyword classification
- **`compute_state_distance`** — Euclidean distance between canonical states
- **`compute_trajectory`** — Smooth interpolation path between states (animation keyframes)
- **`find_nearest_states`** — Proximity search in 5D space

### Layer 3 — Enhancement Pipeline (2 tools)

- **`enhance_neo_andean_prompt`** — Full pipeline: intent + optional state + domain → structured data for Claude synthesis
- **`get_domain_registry_config`** — Integration signature for aesthetics-dynamics-core composition

## Usage Examples

### Architecture Enhancement

```
enhance_neo_andean_prompt(
    intent="vivid cholet facade with condor motifs and stepped geometry",
    domain="architecture",
    canonical_state="mamani_facade",
    intensity=0.7
)
```

### Fashion Enhancement

```
enhance_neo_andean_prompt(
    intent="elegant cholita in flowing pollera with traditional earth tones",
    domain="fashion",
    canonical_state="cholita_haute",
    intensity=0.6
)
```

### Cross-Domain Composition

```
enhance_neo_andean_prompt(
    intent="gran poder festival cholita with cholet backdrop",
    domain="both",
    canonical_state="gran_poder_festival",
    intensity=0.6
)
```

Returns both fashion and architecture vocabularies plus a `cross_domain_functor` block describing the structural relationship between the two outputs.

### Trajectory (Animation/Progressive Enhancement)

```
compute_trajectory(
    state_a="tiwanaku_stone",
    state_b="el_altopia_futurism",
    steps=8
)
```

Returns 9 interpolated coordinate sets tracing the path from pre-Columbian archaeological through to speculative Neo-Andean future — usable as keyframes or progressive enhancement stages.

## Prompt Integration Pattern

The intended workflow for image generation:

1. **Claude** receives user intent and extracts creative direction
2. **Claude** calls `decompose_intent` or `enhance_neo_andean_prompt` with the intent
3. **MCP server** returns structured data (coordinates, geometry, palette, symbols, vocabulary)
4. **Claude** synthesizes the structured data into an image generation prompt using explicit geometric specifications

The server provides the taxonomy and mapping; Claude provides the creative synthesis. This separation keeps deterministic operations at zero cost while concentrating LLM spend on the creative step.

## Deployment

### FastMCP Cloud

Entrypoint: `neo_andean_mcp.py:mcp`

The server returns the `mcp` object directly — no `server.run()` call in the module body. The `__main__.py` file handles local execution.

### Local

```bash
python __main__.py
```

### File Structure

```
neo-andean-mcp/
├── neo_andean_mcp.py   # Server implementation (single file)
├── pyproject.toml       # Package metadata and dependencies
├── __main__.py          # Local execution entry point
└── README.md
```

## Composition with Other Domains

The `get_domain_registry_config` tool returns the integration signature for aesthetics-dynamics-core multi-domain composition. Axis mappings to generic compositional parameters:

| Neo-Andean Axis | Generic Mapping | Composition Notes |
|-----------------|-----------------|-------------------|
| chacha_warmi | tension_axis | Maps to structural tension in any domain |
| chromatic_intensity | energy_axis | Maps to saturation/energy |
| symbolic_density | complexity_axis | Maps to information density |
| scale_register | zoom_axis | Unique three-stop functor: textile→garment→architecture |
| temporal_composite | temporal_axis | Multiple simultaneous pasts — novel parameter |

The **scale_register** axis is particularly interesting for cross-domain work because it encodes a three-stop functor (weave → wear → wall) that has no direct analogue in other domains. When composing Neo-Andean with, for example, microscopy aesthetics, the textile-scale end of this axis creates natural resonance with surface-pattern domains.

## Cultural Context

Neo-Andean design is rooted in the cultural resurgence of the Aymara people in El Alto, Bolivia. The aesthetic vocabulary encoded in this server draws from living cultural traditions — aguayo textile weaving, cholita fashion, Gran Poder festival regalia — as well as archaeological sources (Tiwanaku, ~200 BC). Freddy Mamani Silvestre's architectural work since 2005 represents the contemporary apex of this tradition, with over 200 buildings transforming the El Alto skyline.

The "abundance principle" — the recursive "always more" aesthetic — is not decorative excess but a cultural assertion. Each cholet declares presence; each cholita outfit at Gran Poder performs identity. The server's coordinate space respects this by treating ornamental saturation as a meaningful parameter rather than a deviation from some assumed neutral.
