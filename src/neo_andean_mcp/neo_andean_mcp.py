"""
Neo-Andean Aesthetic MCP Server

A unified aesthetic enhancement server covering both architectural (cholet) and
fashion (cholita) domains of Neo-Andean design. Built on a shared 5D coordinate
space derived from Aymara textile traditions, Tiwanaku iconography, and
contemporary El Alto visual culture.

Three-layer architecture:
  Layer 1: Pure taxonomy lookup (0 tokens)
  Layer 2: Deterministic mapping and composition (0 tokens)
  Layer 3: Structured data for Claude synthesis (~100-200 tokens)

The textile-to-architecture functor is bidirectional: the same symbolic content
expressed at different scales, with structure-preserving mappings between domains.
"""

from fastmcp import FastMCP
import json
import math
import numpy as np

mcp = FastMCP("neo_andean_mcp")

# =============================================================================
# LAYER 1: TAXONOMY — Pure lookup, zero LLM cost
# =============================================================================

# 5D Coordinate Space
# Each axis 0.0 - 1.0
COORDINATE_AXES = {
    "chacha_warmi": {
        "name": "Chacha-Warmi Balance",
        "description": "Angular/rectilinear (chacha/masculine) to organic/curvilinear (warmi/feminine). Derived from Tiwanaku cosmological duality.",
        "low_label": "angular, stepped, rectilinear, faceted",
        "high_label": "organic, curved, flowing, voluminous",
        "midpoint_note": "Perfect chacha-warmi harmony at 0.5 — the sacred balance"
    },
    "chromatic_intensity": {
        "name": "Chromatic Intensity",
        "description": "Earth-tone Tiwanaku stone palette through full aguayo textile saturation to contemporary neon/LED.",
        "low_label": "stone, earth, ochre, muted",
        "high_label": "electric, neon, saturated, aguayo-vivid",
        "midpoint_note": "Traditional festival palette at 0.5 — whiphala flag spectrum"
    },
    "symbolic_density": {
        "name": "Symbolic Density",
        "description": "Pure geometric pattern through fully iconographic with Tiwanaku motifs, zoomorphic figures, and cosmological symbols.",
        "low_label": "geometric-only, abstract pattern, textile grid",
        "high_label": "fully iconographic, zoomorphic, narrative, cosmological",
        "midpoint_note": "Stylized chakana patterns at 0.5 — recognizable but abstracted"
    },
    "scale_register": {
        "name": "Scale Register",
        "description": "Textile intimacy through garment-body scale to monumental architectural facade. Three-stop functor: weave → wear → wall.",
        "low_label": "textile weave, thread-level, intimate pattern",
        "high_label": "monumental facade, urban-scale, skyline presence",
        "midpoint_note": "Garment/body scale at 0.5 — the cholita pollera"
    },
    "temporal_composite": {
        "name": "Temporal Composite",
        "description": "Pre-Columbian archaeological through colonial hybridization to contemporary Mamani futurism. Multiple pasts can coexist simultaneously.",
        "low_label": "Tiwanaku archaeological, pre-Columbian, ancient stone",
        "high_label": "contemporary futurism, neon-lit, El Altopia",
        "midpoint_note": "Colonial-era hybridization at 0.5 — Spanish silhouettes with Andean color"
    }
}

# Angle constraints from Andean textile tradition
GEOMETRIC_CONSTRAINTS = {
    "primary_angles": [45, 90, 135],
    "description": "Lines in Andean design are traditionally restricted to 45°, 90°, and 135° angles, derived from textile weave structure.",
    "chacha_angles": [45, 90, 135],  # Stepped, cornered, rectilinear
    "warmi_curves": ["parabolic_arch", "concentric_circle", "spiral", "organic_lobe"],
    "hybrid_forms": ["stepped_curve", "angular_spiral", "faceted_arch"]
}

# Tiwanaku iconographic vocabulary
SYMBOLIC_ELEMENTS = {
    "chakana": {
        "name": "Andean Cross (Chakana)",
        "geometry": "Stepped cross with 12 points, square void at center",
        "meaning": "Four cardinal directions, three worlds (hanan pacha, kay pacha, ukhu pacha)",
        "angle_constraint": "All edges at 90° — pure chacha geometry",
        "symbolic_density": 0.6
    },
    "inti": {
        "name": "Sun / Inti",
        "geometry": "Radial burst with alternating straight and wavy rays",
        "meaning": "Solar deity, life-giving force, temporal cycles",
        "angle_constraint": "Rays at 45° intervals, warmi-influenced wave rays",
        "symbolic_density": 0.7
    },
    "condor": {
        "name": "Condor (Hanan Pacha)",
        "geometry": "Spread wings, bilateral symmetry, stepped feather edges",
        "meaning": "Upper world, sky realm, spiritual messenger",
        "angle_constraint": "Stepped wing edges (chacha), curved body (warmi)",
        "symbolic_density": 0.8
    },
    "puma": {
        "name": "Puma (Kay Pacha)",
        "geometry": "Profile stance, geometric musculature, angular jaw",
        "meaning": "Middle world, earthly power, strength",
        "angle_constraint": "Predominantly angular (chacha-dominant)",
        "symbolic_density": 0.8
    },
    "serpent": {
        "name": "Serpent / Amaru (Ukhu Pacha)",
        "geometry": "Undulating s-curve, diamond-patterned scales",
        "meaning": "Lower world, underground, water, transformation",
        "angle_constraint": "Predominantly curvilinear (warmi-dominant)",
        "symbolic_density": 0.8
    },
    "pachamama": {
        "name": "Pachamama (Mother Earth)",
        "geometry": "Organic lobed forms suggesting fertility and growth",
        "meaning": "Earth goddess, life support, agricultural abundance",
        "angle_constraint": "Pure warmi — organic curves, no right angles",
        "symbolic_density": 0.9
    },
    "gateway_motif": {
        "name": "Gateway of the Sun Motif",
        "geometry": "Trapezoidal frame with central radiating figure, attendant rows",
        "meaning": "Derived from Tiwanaku Gateway of the Sun, cosmic authority",
        "angle_constraint": "Trapezoidal (chacha) with radial detail (hybrid)",
        "symbolic_density": 1.0
    },
    "whiphala": {
        "name": "Whiphala Flag Pattern",
        "geometry": "7×7 diagonal rainbow grid, 49 squares",
        "meaning": "Pan-Andean indigenous unity, seven colors of the spectrum",
        "angle_constraint": "45° diagonal grid — pure geometric",
        "symbolic_density": 0.3
    },
    "tocapu": {
        "name": "Tocapu Geometric Units",
        "geometry": "Small square or rectangular units containing individual geometric patterns",
        "meaning": "Inca-era communication system, status and identity markers",
        "angle_constraint": "Strict 90° grid with internal pattern variation",
        "symbolic_density": 0.5
    }
}

# Color palettes organized by chromatic_intensity
COLOR_PALETTES = {
    "tiwanaku_stone": {
        "chromatic_intensity": (0.0, 0.2),
        "colors": [
            {"name": "andesite_grey", "hex": "#8B8680", "source": "Tiwanaku carved stone"},
            {"name": "sandstone_ochre", "hex": "#C4A35A", "source": "Gateway of the Sun"},
            {"name": "earth_red", "hex": "#8B4513", "source": "Altiplano clay"},
            {"name": "lichen_green", "hex": "#6B7B3A", "source": "Highland moss on ruins"}
        ]
    },
    "traditional_textile": {
        "chromatic_intensity": (0.2, 0.5),
        "colors": [
            {"name": "cochineal_red", "hex": "#DC143C", "source": "Traditional natural dye"},
            {"name": "indigo_deep", "hex": "#1B0F6B", "source": "Añil plant dye"},
            {"name": "turmeric_gold", "hex": "#E8A317", "source": "Natural root dye"},
            {"name": "coca_green", "hex": "#2E7D32", "source": "Leaf-derived pigment"},
            {"name": "llama_brown", "hex": "#6D4C2F", "source": "Undyed camelid fiber"}
        ]
    },
    "whiphala_spectrum": {
        "chromatic_intensity": (0.4, 0.7),
        "colors": [
            {"name": "whiphala_red", "hex": "#FF0000", "source": "Earth, Andean people"},
            {"name": "whiphala_orange", "hex": "#FF8C00", "source": "Society, culture"},
            {"name": "whiphala_yellow", "hex": "#FFD700", "source": "Energy, moral strength"},
            {"name": "whiphala_white", "hex": "#FFFFFF", "source": "Time, transformation"},
            {"name": "whiphala_green", "hex": "#008000", "source": "Natural resources, economy"},
            {"name": "whiphala_blue", "hex": "#0000FF", "source": "Cosmic space, infinity"},
            {"name": "whiphala_violet", "hex": "#8B00FF", "source": "Political ideology, social power"}
        ]
    },
    "mamani_facade": {
        "chromatic_intensity": (0.6, 0.85),
        "colors": [
            {"name": "cholet_pink", "hex": "#FF69B4", "source": "Mamani signature facade"},
            {"name": "cholet_electric_green", "hex": "#39FF14", "source": "Facade accent"},
            {"name": "cholet_orange", "hex": "#FF6600", "source": "Window surround"},
            {"name": "cholet_turquoise", "hex": "#00CED1", "source": "Facade panel"},
            {"name": "cholet_gold", "hex": "#FFD700", "source": "Ornamental detail"},
            {"name": "cholet_magenta", "hex": "#FF00FF", "source": "Interior event hall"}
        ]
    },
    "neon_interior": {
        "chromatic_intensity": (0.85, 1.0),
        "colors": [
            {"name": "event_hall_neon_pink", "hex": "#FF1493", "source": "LED-lit ballroom ceiling"},
            {"name": "event_hall_neon_blue", "hex": "#00BFFF", "source": "Geometric wall panel"},
            {"name": "event_hall_neon_green", "hex": "#7FFF00", "source": "Accent lighting strip"},
            {"name": "event_hall_violet", "hex": "#9400D3", "source": "Ambient wash"},
            {"name": "mirror_chrome", "hex": "#C0C0C0", "source": "Reflective ceiling panels"}
        ]
    }
}

# =============================================================================
# DOMAIN-SPECIFIC VISUAL VOCABULARIES
# =============================================================================

ARCHITECTURE_VOCABULARY = {
    "facade_elements": [
        "stepped_gable", "circular_window", "angled_roofline", "trapezoidal_doorway",
        "geometric_frieze", "cantilevered_balcony", "lobed_arch", "faceted_pilaster",
        "chakana_relief", "zoomorphic_bracket", "polychrome_panel", "mirror_glass_insert"
    ],
    "interior_elements": [
        "geometric_ceiling_pattern", "neon_lit_cornice", "mirrored_column",
        "polychrome_tile_floor", "LED_strip_accent", "stepped_stage",
        "radial_chandelier", "aguayo_wall_panel", "chrome_balustrade"
    ],
    "structural_typology": {
        "ground_floor": "Commercial stalls, street-facing, public/transactional",
        "event_hall": "Second floor ballroom, maximum ornamental saturation, social/performative",
        "residence": "Upper floors, chalet-style, private/intimate",
        "rooftop": "Penthouse or sculptural crown, identity signal"
    },
    "compositional_geometry": {
        "bilateral_symmetry": "Facades centered on vertical axis, stepped profile",
        "radial_burst": "Interior ceiling patterns radiating from central fixture",
        "nested_frames": "Concentric rectangular frames diminishing toward center",
        "diagonal_grid": "45° whiphala-derived panel layout"
    }
}

FASHION_VOCABULARY = {
    "garment_elements": {
        "sombrero_bombin": {
            "description": "Bowler hat, crown ~10cm, worn at angle indicating marital status",
            "position_semiotics": "center=married, side=single/widowed, back=complicated",
            "materials": ["felt", "wool", "decorated with brooch or pin"],
            "chacha_warmi": 0.3  # Predominantly angular European form
        },
        "pollera": {
            "description": "Multi-layered pleated skirt, up to 8 meters of cloth, bell silhouette",
            "materials": ["velvet", "satin", "chiffon", "synthetic"],
            "import_sources": ["Korea (premium)", "China (standard)", "Italy (luxury)"],
            "chacha_warmi": 0.8  # Voluminous, curved, warmi-dominant
        },
        "enaguas": {
            "description": "Layered petticoats providing volume and structure beneath pollera",
            "function": "Structural skeleton — adds bulk and prominence to the bell shape",
            "materials": ["lace", "cotton", "colored to match pollera"],
            "chacha_warmi": 0.5  # Structural support, balanced
        },
        "blusa": {
            "description": "Lacy blouse, short or long sleeve depending on climate",
            "function": "Upper body, often corseted for fitted silhouette",
            "materials": ["lace", "cotton", "embroidered"],
            "chacha_warmi": 0.4  # More structured/fitted
        },
        "manta": {
            "description": "Shoulder shawl, typically alpaca or llama wool, single color or aguayo pattern",
            "function": "Outer signal layer, secured with topo pin/brooch",
            "materials": ["alpaca wool", "llama wool", "vicuña (luxury)", "synthetic"],
            "chacha_warmi": 0.6  # Draped but geometric pattern
        },
        "aguayo": {
            "description": "Multi-purpose woven sling, bright geometric patterns, carried across back",
            "function": "Carries goods, babies, packages — functional and decorative",
            "materials": ["hand-woven camelid fiber", "cotton blend"],
            "chacha_warmi": 0.5  # Geometric pattern (chacha) on draped form (warmi)
        },
        "calzados": {
            "description": "Flat shoes with rounded toe, similar to ballet flat",
            "historical": "Originally European ankle boots, evolved to current form",
            "materials": ["leather", "synthetic crystal", "plastic"],
            "chacha_warmi": 0.3  # Small, structured
        },
        "joyas": {
            "description": "Jewelry: topos (large pins), earrings, brooches",
            "function": "Status signaling, outfit securing, wealth display",
            "materials": ["gold", "silver", "rhinestone", "pearls", "fantasía"],
            "price_range": "Festival topos can exceed $1500 USD",
            "chacha_warmi": 0.4  # Geometric metalwork
        }
    },
    "layering_typology": {
        "outer_signal": "Sombrero, manta, joyas — the facade. Public identity and status.",
        "middle_performative": "Pollera, blusa — the event hall. Maximum visual presence.",
        "inner_structural": "Enaguas — the skeleton. Invisible but defines the silhouette."
    },
    "compositional_geometry": {
        "bell_silhouette": "Inverted cone from waist, maximum diameter at hem",
        "stacked_volumes": "Hat (small cone) → shoulders (manta drape) → skirt (large bell)",
        "pin_point_accent": "Topo brooch creates focal point at chest, anchoring manta",
        "bilateral_braid": "Dual braids frame face, mirror the bilateral facade symmetry"
    }
}

# Cholet canonical states — unified across domains
CANONICAL_STATES = {
    "tiwanaku_stone": {
        "description": "Archaeological pre-Columbian. Monolithic carved stone, stepped geometry, earth palette.",
        "coordinates": {"chacha_warmi": 0.2, "chromatic_intensity": 0.1, "symbolic_density": 0.7, "scale_register": 0.8, "temporal_composite": 0.0}
    },
    "aguayo_weave": {
        "description": "Traditional textile at intimate scale. Geometric grid, natural dye palette, hand-woven texture.",
        "coordinates": {"chacha_warmi": 0.5, "chromatic_intensity": 0.4, "symbolic_density": 0.4, "scale_register": 0.0, "temporal_composite": 0.2}
    },
    "colonial_hybrid": {
        "description": "Spanish-imposed silhouettes infused with Andean color. The cholita's historical origin point.",
        "coordinates": {"chacha_warmi": 0.4, "chromatic_intensity": 0.3, "symbolic_density": 0.3, "scale_register": 0.5, "temporal_composite": 0.5}
    },
    "gran_poder_festival": {
        "description": "Maximum performative display. Full cholita regalia, dance, music, competitive opulence.",
        "coordinates": {"chacha_warmi": 0.7, "chromatic_intensity": 0.8, "symbolic_density": 0.6, "scale_register": 0.5, "temporal_composite": 0.7}
    },
    "mamani_facade": {
        "description": "Classic Freddy Mamani cholet exterior. Vivid polychrome, stepped geometry with organic curves.",
        "coordinates": {"chacha_warmi": 0.5, "chromatic_intensity": 0.75, "symbolic_density": 0.6, "scale_register": 0.9, "temporal_composite": 0.8}
    },
    "event_hall_interior": {
        "description": "Cholet ballroom at maximum saturation. Neon, mirrors, geometric ceiling, LED accents.",
        "coordinates": {"chacha_warmi": 0.6, "chromatic_intensity": 0.95, "symbolic_density": 0.5, "scale_register": 0.7, "temporal_composite": 0.9}
    },
    "cholita_haute": {
        "description": "Contemporary high-fashion cholita. Vicuña wool, designer pollera, luxury materials.",
        "coordinates": {"chacha_warmi": 0.7, "chromatic_intensity": 0.6, "symbolic_density": 0.4, "scale_register": 0.5, "temporal_composite": 0.8}
    },
    "abundance_principle": {
        "description": "The recursive 'always more' aesthetic. Maximum ornamental saturation across all registers.",
        "coordinates": {"chacha_warmi": 0.5, "chromatic_intensity": 0.9, "symbolic_density": 0.9, "scale_register": 0.5, "temporal_composite": 0.7}
    },
    "el_altopia_futurism": {
        "description": "Speculative Neo-Andean future. Sci-fi cholet, digital aguayo, holographic chakana.",
        "coordinates": {"chacha_warmi": 0.5, "chromatic_intensity": 1.0, "symbolic_density": 0.8, "scale_register": 0.8, "temporal_composite": 1.0}
    },
    "crucero_de_los_andes": {
        "description": "Mamani's evolution beyond cholet — the silver ship atop El Alto. Departure point.",
        "coordinates": {"chacha_warmi": 0.6, "chromatic_intensity": 0.5, "symbolic_density": 0.3, "scale_register": 1.0, "temporal_composite": 1.0}
    }
}


# =============================================================================
# PHASE 2.6: RHYTHMIC PRESETS
# =============================================================================
# Period strategy for cross-domain composition:
#   Overlap periods: 18 (nuclear, catastrophe, diatom), 20 (microscopy,
#     catastrophe, diatom), 22 (catastrophe, heraldic), 24 (microscopy)
#   Gap-filling periods: 14 (fills 12-15 gap), 28 (fills 25-30 gap)
#   All periods: [14, 18, 20, 22, 24, 28]
#
# LCM resonances introduced:
#   LCM(14,18) = 126, LCM(14,20) = 140, LCM(14,24) = 168
#   LCM(28,18) = 252, LCM(28,20) = 140, LCM(28,22) = 308

PARAMETER_NAMES = [
    "chacha_warmi",
    "chromatic_intensity",
    "symbolic_density",
    "scale_register",
    "temporal_composite"
]

NEO_ANDEAN_RHYTHMIC_PRESETS = {
    "temporal_weave": {
        "state_a": "tiwanaku_stone",
        "state_b": "el_altopia_futurism",
        "pattern": "sinusoidal",
        "num_cycles": 3,
        "steps_per_cycle": 18,
        "description": "Full temporal sweep from archaeological pre-Columbian through colonial hybridization to speculative futurism. Exercises the temporal_composite axis across its full range while shifting chromatic_intensity from earth-tone to neon."
    },
    "chacha_warmi_cycle": {
        "state_a": "tiwanaku_stone",
        "state_b": "cholita_haute",
        "pattern": "sinusoidal",
        "num_cycles": 3,
        "steps_per_cycle": 22,
        "description": "Oscillates the foundational chacha-warmi duality: angular monolithic stone geometry (chacha=0.2) through organic voluminous fashion silhouette (chacha=0.7). The cosmological gender-balance axis made rhythmic."
    },
    "chromatic_ascent": {
        "state_a": "aguayo_weave",
        "state_b": "event_hall_interior",
        "pattern": "triangular",
        "num_cycles": 3,
        "steps_per_cycle": 20,
        "description": "Triangular ramp from traditional natural-dye textile palette (chromatic=0.4) to maximum neon-saturated interior (chromatic=0.95). The linear ramp mirrors the historical chromatic intensification from traditional to contemporary."
    },
    "scale_functor": {
        "state_a": "aguayo_weave",
        "state_b": "mamani_facade",
        "pattern": "sinusoidal",
        "num_cycles": 2,
        "steps_per_cycle": 24,
        "description": "The textile-to-architecture functor made oscillatory. Intimate hand-woven scale (register=0.0) through monumental polychrome facade (register=0.9). Structure-preserving mapping: weave → garment → wall."
    },
    "abundance_pulse": {
        "state_a": "colonial_hybrid",
        "state_b": "abundance_principle",
        "pattern": "sinusoidal",
        "num_cycles": 4,
        "steps_per_cycle": 14,
        "description": "Colonial restraint (chromatic=0.3, symbolic=0.3) pulsing to maximum ornamental saturation (chromatic=0.9, symbolic=0.9). The recursive 'always more' aesthetic as rhythmic intensification."
    },
    "futurist_evolution": {
        "state_a": "mamani_facade",
        "state_b": "crucero_de_los_andes",
        "pattern": "triangular",
        "num_cycles": 2,
        "steps_per_cycle": 28,
        "description": "Classic Mamani cholet (polychrome, ornamental) evolving toward post-Mamani departure point (monumental, restrained). Triangular wave traces the evolution and return of Neo-Andean architectural ambition."
    }
}


# =============================================================================
# PHASE 2.7: VISUAL VOCABULARY TYPES FOR ATTRACTOR PROMPT GENERATION
# =============================================================================
# Each visual type anchors a region of the 5D morphospace with image-generation
# keywords. Nearest-neighbor matching maps any parameter state to the closest
# type, weighted by Euclidean distance.

NEO_ANDEAN_VISUAL_TYPES = {
    "tiwanaku_monolithic": {
        "coords": {
            "chacha_warmi": 0.2,
            "chromatic_intensity": 0.1,
            "symbolic_density": 0.7,
            "scale_register": 0.8,
            "temporal_composite": 0.0
        },
        "keywords": [
            "stepped stone geometry with 90-degree edges",
            "monolithic carved andesite relief",
            "earth-tone ochre and grey palette",
            "pre-Columbian Tiwanaku iconography",
            "bilateral symmetry on vertical axis",
            "massive megalithic block construction",
            "Gateway of the Sun radiating figure motif"
        ]
    },
    "aguayo_textile": {
        "coords": {
            "chacha_warmi": 0.5,
            "chromatic_intensity": 0.4,
            "symbolic_density": 0.4,
            "scale_register": 0.0,
            "temporal_composite": 0.2
        },
        "keywords": [
            "hand-woven geometric grid at 45-degree diagonal",
            "natural dye palette of cochineal red and indigo",
            "intimate textile-scale repeating pattern",
            "camelid fiber warp-and-weft texture",
            "whiphala-derived diagonal stripe layout",
            "chacha-warmi balanced angular-organic motifs"
        ]
    },
    "cholet_polychrome": {
        "coords": {
            "chacha_warmi": 0.5,
            "chromatic_intensity": 0.75,
            "symbolic_density": 0.6,
            "scale_register": 0.9,
            "temporal_composite": 0.8
        },
        "keywords": [
            "vivid polychrome Mamani cholet facade",
            "stepped geometric gable with organic lobed arches",
            "electric pink turquoise and gold panel surfaces",
            "monumental El Alto architectural scale",
            "chakana cross relief ornament",
            "mirrored glass window inserts",
            "bilateral facade symmetry with nested frames"
        ]
    },
    "cholita_festival": {
        "coords": {
            "chacha_warmi": 0.7,
            "chromatic_intensity": 0.8,
            "symbolic_density": 0.6,
            "scale_register": 0.5,
            "temporal_composite": 0.7
        },
        "keywords": [
            "layered pollera bell silhouette at full volume",
            "saturated velvet and satin textile surfaces",
            "bowler hat positioned at expressive angle",
            "aguayo geometric sling across the back",
            "gold topo brooch focal point at chest",
            "competitive opulence and abundance display",
            "Gran Poder festival pageantry"
        ]
    },
    "el_altopia_neon": {
        "coords": {
            "chacha_warmi": 0.5,
            "chromatic_intensity": 1.0,
            "symbolic_density": 0.8,
            "scale_register": 0.8,
            "temporal_composite": 1.0
        },
        "keywords": [
            "neon-lit geometric facade with LED strip accents",
            "holographic chakana patterns on reflective surface",
            "electric fluorescent pink blue and green palette",
            "chrome and mirror panel ceiling construction",
            "speculative Andean futurism architecture",
            "digital aguayo projection mapping",
            "sci-fi cholet with zoomorphic neon relief"
        ]
    }
}


# =============================================================================
# LAYER 1 TOOLS — Pure taxonomy lookup
# =============================================================================

@mcp.tool()
def get_coordinate_axes() -> str:
    """Return the 5D coordinate space definition for Neo-Andean aesthetics.

    Layer 1: Pure taxonomy lookup (0 tokens).

    Returns the five axes with descriptions, labels, and midpoint notes.
    """
    return json.dumps(COORDINATE_AXES, indent=2)


@mcp.tool()
def get_geometric_constraints() -> str:
    """Return Andean geometric angle constraints derived from textile tradition.

    Layer 1: Pure taxonomy lookup (0 tokens).

    Returns primary angles (45°, 90°, 135°), chacha angles, warmi curves,
    and hybrid forms.
    """
    return json.dumps(GEOMETRIC_CONSTRAINTS, indent=2)


@mcp.tool()
def get_symbolic_elements(element_name: str = "") -> str:
    """Look up Tiwanaku iconographic elements with geometry and meaning.

    Layer 1: Pure taxonomy lookup (0 tokens).

    Args:
        element_name: Specific element name (e.g. 'chakana', 'condor').
                      Empty string returns all elements.

    Returns complete visual specification including geometry, meaning,
    angle constraints, and symbolic density rating.
    """
    if element_name and element_name in SYMBOLIC_ELEMENTS:
        return json.dumps({element_name: SYMBOLIC_ELEMENTS[element_name]}, indent=2)
    elif element_name:
        available = list(SYMBOLIC_ELEMENTS.keys())
        return json.dumps({"error": f"Unknown element: {element_name}", "available": available})
    return json.dumps(SYMBOLIC_ELEMENTS, indent=2)


@mcp.tool()
def get_color_palette(palette_name: str = "", chromatic_intensity: float = -1.0) -> str:
    """Return color palettes organized by chromatic intensity.

    Layer 1: Pure taxonomy lookup (0 tokens).

    Args:
        palette_name: Specific palette (e.g. 'mamani_facade', 'whiphala_spectrum').
                      Empty returns all palettes.
        chromatic_intensity: If 0.0-1.0, returns palette(s) matching that intensity range.

    Returns hex colors with source attribution and intensity range.
    """
    if palette_name and palette_name in COLOR_PALETTES:
        return json.dumps({palette_name: COLOR_PALETTES[palette_name]}, indent=2)
    elif 0.0 <= chromatic_intensity <= 1.0:
        matching = {}
        for name, palette in COLOR_PALETTES.items():
            low, high = palette["chromatic_intensity"]
            if low <= chromatic_intensity <= high:
                matching[name] = palette
        if not matching:
            return json.dumps({"note": f"No exact match for {chromatic_intensity}. Returning nearest.", "palettes": COLOR_PALETTES})
        return json.dumps(matching, indent=2)
    return json.dumps(COLOR_PALETTES, indent=2)


@mcp.tool()
def get_visual_vocabulary(domain: str = "both") -> str:
    """Return domain-specific visual vocabulary for architecture, fashion, or both.

    Layer 1: Pure taxonomy lookup (0 tokens).

    Args:
        domain: 'architecture', 'fashion', or 'both' (default).

    Returns element lists, typology descriptions, and compositional geometry
    specific to the chosen domain.
    """
    if domain == "architecture":
        return json.dumps({"architecture": ARCHITECTURE_VOCABULARY}, indent=2)
    elif domain == "fashion":
        return json.dumps({"fashion": FASHION_VOCABULARY}, indent=2)
    return json.dumps({
        "architecture": ARCHITECTURE_VOCABULARY,
        "fashion": FASHION_VOCABULARY
    }, indent=2)


@mcp.tool()
def get_canonical_states() -> str:
    """List all 10 canonical Neo-Andean aesthetic states with 5D coordinates.

    Layer 1: Pure taxonomy lookup (0 tokens).

    States span from Tiwanaku archaeological through to El Altopia futurism,
    covering both architectural and fashion registers.
    """
    return json.dumps(CANONICAL_STATES, indent=2)


# =============================================================================
# LAYER 2 — Deterministic computation, zero LLM cost
# =============================================================================

def _euclidean_distance(a: dict, b: dict) -> float:
    """Compute Euclidean distance between two 5D coordinate dictionaries."""
    axes = ["chacha_warmi", "chromatic_intensity", "symbolic_density", "scale_register", "temporal_composite"]
    return math.sqrt(sum((a[ax] - b[ax]) ** 2 for ax in axes))


def _interpolate(a: dict, b: dict, t: float) -> dict:
    """Linear interpolation between two coordinate dictionaries at parameter t."""
    axes = ["chacha_warmi", "chromatic_intensity", "symbolic_density", "scale_register", "temporal_composite"]
    return {ax: round(a[ax] + t * (b[ax] - a[ax]), 3) for ax in axes}


def _select_palette(chromatic_intensity: float) -> list:
    """Select color palette entries matching a chromatic intensity value."""
    results = []
    for name, palette in COLOR_PALETTES.items():
        low, high = palette["chromatic_intensity"]
        if low <= chromatic_intensity <= high:
            results.extend(palette["colors"])
    if not results:
        # Nearest match
        nearest_name = min(COLOR_PALETTES.keys(),
                          key=lambda n: abs(sum(COLOR_PALETTES[n]["chromatic_intensity"]) / 2 - chromatic_intensity))
        results = COLOR_PALETTES[nearest_name]["colors"]
    return results


def _select_symbols(symbolic_density: float) -> list:
    """Select symbolic elements appropriate for a given density level."""
    results = []
    for name, elem in SYMBOLIC_ELEMENTS.items():
        if elem["symbolic_density"] <= symbolic_density + 0.15:
            results.append({"name": name, **elem})
    # Sort by density ascending
    results.sort(key=lambda x: x["symbolic_density"])
    return results


def _select_geometry(chacha_warmi: float) -> dict:
    """Select geometric forms based on chacha-warmi balance."""
    gc = GEOMETRIC_CONSTRAINTS
    if chacha_warmi < 0.35:
        return {
            "primary_forms": gc["chacha_angles"],
            "description": "Chacha-dominant: stepped edges, right angles, rectilinear grid",
            "curves_permitted": False,
            "form_vocabulary": ["stepped_gable", "trapezoidal_frame", "grid_panel", "faceted_column"]
        }
    elif chacha_warmi > 0.65:
        return {
            "primary_forms": gc["warmi_curves"],
            "description": "Warmi-dominant: organic curves, lobed arches, flowing silhouette",
            "angles_permitted": True,  # Warmi contains chacha
            "form_vocabulary": ["lobed_arch", "parabolic_dome", "organic_relief", "flowing_drape", "bell_silhouette"]
        }
    else:
        return {
            "primary_forms": gc["hybrid_forms"],
            "description": "Chacha-warmi harmony: angular framework with organic infill, stepped curves",
            "form_vocabulary": ["stepped_curve", "angular_spiral", "faceted_arch", "geometric_with_organic_detail"]
        }


def _map_to_domain(coordinates: dict, domain: str) -> dict:
    """Map 5D coordinates to domain-specific visual vocabulary."""
    scale = coordinates.get("scale_register", 0.5)
    vocab = ARCHITECTURE_VOCABULARY if domain == "architecture" else FASHION_VOCABULARY

    if domain == "architecture":
        # Scale register selects architectural zone
        if scale < 0.3:
            zone = "textile-scale detail within architecture"
            elements = ["aguayo_wall_panel", "geometric_tile_floor", "woven_texture_panel"]
        elif scale < 0.6:
            zone = "interior / event hall"
            elements = vocab["interior_elements"]
        else:
            zone = "exterior facade / monumental"
            elements = vocab["facade_elements"]
        typology = vocab["structural_typology"]
        composition = vocab["compositional_geometry"]
    else:
        # Scale register selects fashion layer
        garments = vocab["garment_elements"]
        if scale < 0.3:
            zone = "textile / weave detail"
            elements = ["aguayo", "manta"]
        elif scale < 0.7:
            zone = "garment / body"
            elements = list(garments.keys())
        else:
            zone = "ensemble / silhouette"
            elements = ["full_cholita_ensemble", "gran_poder_regalia"]
        typology = vocab["layering_typology"]
        composition = vocab["compositional_geometry"]

    return {
        "domain": domain,
        "zone": zone,
        "elements": elements,
        "typology": typology,
        "composition": composition
    }


@mcp.tool()
def map_coordinates(
    chacha_warmi: float = 0.5,
    chromatic_intensity: float = 0.5,
    symbolic_density: float = 0.5,
    scale_register: float = 0.5,
    temporal_composite: float = 0.5,
    domain: str = "both"
) -> str:
    """Map 5D coordinates to visual vocabulary, color palette, symbols, and geometry.

    Layer 2: Deterministic mapping (0 tokens).

    Args:
        chacha_warmi: 0.0 (angular) to 1.0 (organic). Default 0.5.
        chromatic_intensity: 0.0 (earth) to 1.0 (neon). Default 0.5.
        symbolic_density: 0.0 (geometric) to 1.0 (iconographic). Default 0.5.
        scale_register: 0.0 (textile) to 1.0 (monumental). Default 0.5.
        temporal_composite: 0.0 (pre-Columbian) to 1.0 (futurism). Default 0.5.
        domain: 'architecture', 'fashion', or 'both'.

    Returns complete visual specification: geometry, palette, symbols,
    domain vocabulary, and compositional structure.
    """
    coords = {
        "chacha_warmi": max(0.0, min(1.0, chacha_warmi)),
        "chromatic_intensity": max(0.0, min(1.0, chromatic_intensity)),
        "symbolic_density": max(0.0, min(1.0, symbolic_density)),
        "scale_register": max(0.0, min(1.0, scale_register)),
        "temporal_composite": max(0.0, min(1.0, temporal_composite))
    }

    result = {
        "coordinates": coords,
        "geometry": _select_geometry(coords["chacha_warmi"]),
        "palette": _select_palette(coords["chromatic_intensity"]),
        "symbols": _select_symbols(coords["symbolic_density"]),
    }

    if domain in ("architecture", "both"):
        result["architecture"] = _map_to_domain(coords, "architecture")
    if domain in ("fashion", "both"):
        result["fashion"] = _map_to_domain(coords, "fashion")

    # Find nearest canonical state
    nearest_state = min(
        CANONICAL_STATES.items(),
        key=lambda item: _euclidean_distance(coords, item[1]["coordinates"])
    )
    result["nearest_canonical_state"] = {
        "name": nearest_state[0],
        "description": nearest_state[1]["description"],
        "distance": round(_euclidean_distance(coords, nearest_state[1]["coordinates"]), 3)
    }

    return json.dumps(result, indent=2)


@mcp.tool()
def compute_state_distance(state_a: str, state_b: str) -> str:
    """Compute Euclidean distance between two canonical states in 5D space.

    Layer 2: Deterministic computation (0 tokens).

    Args:
        state_a: First canonical state name.
        state_b: Second canonical state name.
    """
    if state_a not in CANONICAL_STATES:
        return json.dumps({"error": f"Unknown state: {state_a}", "available": list(CANONICAL_STATES.keys())})
    if state_b not in CANONICAL_STATES:
        return json.dumps({"error": f"Unknown state: {state_b}", "available": list(CANONICAL_STATES.keys())})

    ca = CANONICAL_STATES[state_a]["coordinates"]
    cb = CANONICAL_STATES[state_b]["coordinates"]

    return json.dumps({
        "state_a": state_a,
        "state_b": state_b,
        "distance": round(_euclidean_distance(ca, cb), 4),
        "axis_deltas": {ax: round(cb[ax] - ca[ax], 3) for ax in ca}
    }, indent=2)


@mcp.tool()
def compute_trajectory(state_a: str, state_b: str, steps: int = 8) -> str:
    """Compute smooth trajectory between two canonical states through 5D space.

    Layer 2: Deterministic interpolation (0 tokens).

    Args:
        state_a: Starting canonical state.
        state_b: Target canonical state.
        steps: Number of interpolation steps (default 8).

    Returns sequence of coordinates suitable for animation keyframes
    or progressive enhancement.
    """
    if state_a not in CANONICAL_STATES:
        return json.dumps({"error": f"Unknown state: {state_a}", "available": list(CANONICAL_STATES.keys())})
    if state_b not in CANONICAL_STATES:
        return json.dumps({"error": f"Unknown state: {state_b}", "available": list(CANONICAL_STATES.keys())})

    ca = CANONICAL_STATES[state_a]["coordinates"]
    cb = CANONICAL_STATES[state_b]["coordinates"]
    steps = max(2, min(steps, 20))

    trajectory = []
    for i in range(steps + 1):
        t = i / steps
        point = _interpolate(ca, cb, t)
        trajectory.append({"step": i, "t": round(t, 3), "coordinates": point})

    return json.dumps({
        "from": state_a,
        "to": state_b,
        "steps": steps,
        "trajectory": trajectory
    }, indent=2)


@mcp.tool()
def find_nearest_states(
    chacha_warmi: float = 0.5,
    chromatic_intensity: float = 0.5,
    symbolic_density: float = 0.5,
    scale_register: float = 0.5,
    temporal_composite: float = 0.5,
    max_results: int = 3
) -> str:
    """Find canonical states nearest to given coordinates in 5D space.

    Layer 2: Deterministic distance computation (0 tokens).

    Args:
        chacha_warmi: 0.0-1.0
        chromatic_intensity: 0.0-1.0
        symbolic_density: 0.0-1.0
        scale_register: 0.0-1.0
        temporal_composite: 0.0-1.0
        max_results: Number of nearest states to return (default 3).
    """
    coords = {
        "chacha_warmi": chacha_warmi,
        "chromatic_intensity": chromatic_intensity,
        "symbolic_density": symbolic_density,
        "scale_register": scale_register,
        "temporal_composite": temporal_composite
    }

    distances = []
    for name, state in CANONICAL_STATES.items():
        d = _euclidean_distance(coords, state["coordinates"])
        distances.append({
            "name": name,
            "description": state["description"],
            "distance": round(d, 4),
            "coordinates": state["coordinates"]
        })

    distances.sort(key=lambda x: x["distance"])
    return json.dumps({"query_coordinates": coords, "nearest": distances[:max_results]}, indent=2)


@mcp.tool()
def decompose_intent(description: str) -> str:
    """Decompose natural language into Neo-Andean 5D coordinates via keyword matching.

    Layer 2: Deterministic classification (0 tokens).

    Args:
        description: Natural language description (e.g. 'vivid cholet facade with
                      condor motifs', 'elegant cholita in traditional festival dress',
                      'ancient Tiwanaku stone carving').

    Returns matching coordinates ranked by keyword overlap score.
    """
    desc_lower = description.lower()

    # Keyword → axis influence mappings
    axis_signals = {
        "chacha_warmi": {
            "low": ["angular", "stepped", "geometric", "rectilinear", "faceted", "sharp", "grid", "square", "rigid"],
            "high": ["organic", "curved", "flowing", "voluminous", "round", "soft", "draped", "bell", "lobed", "spiral"]
        },
        "chromatic_intensity": {
            "low": ["stone", "earth", "muted", "grey", "brown", "ochre", "subdued", "monochrome", "ancient"],
            "high": ["vivid", "neon", "bright", "electric", "saturated", "colorful", "fluorescent", "LED", "glowing", "vibrant"]
        },
        "symbolic_density": {
            "low": ["minimal", "abstract", "simple", "clean", "plain", "geometric-only", "pattern"],
            "high": ["iconographic", "symbolic", "condor", "puma", "serpent", "chakana", "pachamama", "gateway", "zoomorphic", "narrative", "mythic"]
        },
        "scale_register": {
            "low": ["textile", "weave", "thread", "fabric", "intimate", "small", "detail", "close-up"],
            "high": ["monumental", "facade", "building", "tower", "skyline", "urban", "architectural", "cholet", "massive"]
        },
        "temporal_composite": {
            "low": ["ancient", "pre-columbian", "tiwanaku", "archaeological", "ruins", "stone", "ancestral"],
            "high": ["contemporary", "modern", "futuristic", "neon", "digital", "sci-fi", "altopia", "current", "today"]
        }
    }

    # Fashion/architecture domain detection
    fashion_keywords = ["cholita", "pollera", "manta", "blusa", "sombrero", "bombin", "dress", "fashion",
                        "garment", "outfit", "skirt", "shawl", "jewelry", "hat", "wear", "costume", "regalia"]
    arch_keywords = ["cholet", "facade", "building", "interior", "ballroom", "event hall", "architecture",
                     "structure", "roofline", "window", "wall", "column", "ceiling"]

    fashion_score = sum(1 for kw in fashion_keywords if kw in desc_lower)
    arch_score = sum(1 for kw in arch_keywords if kw in desc_lower)

    if fashion_score > arch_score:
        detected_domain = "fashion"
    elif arch_score > fashion_score:
        detected_domain = "architecture"
    else:
        detected_domain = "both"

    # Compute axis values
    coordinates = {}
    keyword_matches = {}
    for axis, signals in axis_signals.items():
        low_hits = [kw for kw in signals["low"] if kw in desc_lower]
        high_hits = [kw for kw in signals["high"] if kw in desc_lower]
        total = len(low_hits) + len(high_hits)
        if total == 0:
            coordinates[axis] = 0.5  # Default neutral
        else:
            coordinates[axis] = round(len(high_hits) / total, 2)
        keyword_matches[axis] = {"low_matches": low_hits, "high_matches": high_hits}

    # Find nearest canonical state
    nearest = min(
        CANONICAL_STATES.items(),
        key=lambda item: _euclidean_distance(coordinates, item[1]["coordinates"])
    )

    return json.dumps({
        "input_description": description,
        "detected_domain": detected_domain,
        "coordinates": coordinates,
        "keyword_matches": keyword_matches,
        "nearest_canonical_state": {
            "name": nearest[0],
            "description": nearest[1]["description"],
            "distance": round(_euclidean_distance(coordinates, nearest[1]["coordinates"]), 3)
        }
    }, indent=2)


# =============================================================================
# PHASE 2.6 — Rhythmic Composition Tools (Layer 2: deterministic, 0 tokens)
# =============================================================================

def _generate_oscillation(num_steps: int, num_cycles: float, pattern: str) -> np.ndarray:
    """Generate oscillation pattern returning values in [0, 1]."""
    t = np.linspace(0, 2 * np.pi * num_cycles, num_steps, endpoint=False)
    if pattern == "sinusoidal":
        return 0.5 * (1.0 + np.sin(t))
    elif pattern == "triangular":
        t_norm = (t / (2 * np.pi)) % 1.0
        return np.where(t_norm < 0.5, 2.0 * t_norm, 2.0 * (1.0 - t_norm))
    elif pattern == "square":
        t_norm = (t / (2 * np.pi)) % 1.0
        return np.where(t_norm < 0.5, 0.0, 1.0)
    else:
        raise ValueError(f"Unknown pattern: {pattern}")


def _generate_preset_trajectory(preset_config: dict) -> np.ndarray:
    """Generate forced-orbit trajectory for a single preset.

    Returns array of shape (total_steps, 5) in parameter space.
    Closure is guaranteed by construction: step 0 == step T.
    """
    state_a = CANONICAL_STATES[preset_config["state_a"]]["coordinates"]
    state_b = CANONICAL_STATES[preset_config["state_b"]]["coordinates"]
    num_cycles = preset_config["num_cycles"]
    steps_per_cycle = preset_config["steps_per_cycle"]
    total_steps = num_cycles * steps_per_cycle

    alpha = _generate_oscillation(total_steps, num_cycles, preset_config["pattern"])

    vec_a = np.array([state_a[p] for p in PARAMETER_NAMES])
    vec_b = np.array([state_b[p] for p in PARAMETER_NAMES])

    trajectory = np.outer(1.0 - alpha, vec_a) + np.outer(alpha, vec_b)
    return trajectory


def _extract_visual_vocabulary_from_params(params: dict, strength: float = 1.0) -> dict:
    """Nearest-neighbor visual type matching in 5D morphospace.

    Args:
        params: dict with all 5 parameter values.
        strength: domain strength weight [0, 1].

    Returns:
        dict with nearest_type, distance, keywords, strength.
    """
    query = np.array([params.get(p, 0.5) for p in PARAMETER_NAMES])

    best_type = None
    best_dist = float("inf")
    best_kw = []

    for vtype, spec in NEO_ANDEAN_VISUAL_TYPES.items():
        ref = np.array([spec["coords"][p] for p in PARAMETER_NAMES])
        dist = float(np.linalg.norm(query - ref))
        if dist < best_dist:
            best_dist = dist
            best_type = vtype
            best_kw = spec["keywords"]

    return {
        "nearest_type": best_type,
        "distance": round(best_dist, 4),
        "keywords": best_kw,
        "strength": round(strength, 3)
    }


@mcp.tool()
def list_neo_andean_presets() -> str:
    """List all Phase 2.6 rhythmic presets with periods and descriptions.

    Layer 2: Pure lookup (0 tokens).

    Returns preset names, periods, patterns, endpoint states,
    and the strategic rationale for each period choice.
    """
    result = {}
    all_periods = []
    for name, cfg in NEO_ANDEAN_RHYTHMIC_PRESETS.items():
        period = cfg["steps_per_cycle"]
        all_periods.append(period)
        result[name] = {
            "period": period,
            "pattern": cfg["pattern"],
            "state_a": cfg["state_a"],
            "state_b": cfg["state_b"],
            "num_cycles": cfg["num_cycles"],
            "total_steps": cfg["num_cycles"] * period,
            "description": cfg["description"]
        }
    return json.dumps({
        "domain": "neo_andean",
        "phase": "2.6",
        "preset_count": len(result),
        "periods": sorted(set(all_periods)),
        "period_strategy": {
            "overlap": "18 (nuclear/catastrophe/diatom), 20 (microscopy/catastrophe/diatom), 22 (catastrophe/heraldic), 24 (microscopy)",
            "gap_fill": "14 (fills 12-15 gap), 28 (fills 25-30 gap)",
            "novel_lcm": "LCM(14,18)=126, LCM(14,20)=140, LCM(28,22)=308"
        },
        "presets": result
    }, indent=2)


@mcp.tool()
def apply_neo_andean_preset(
    preset_name: str,
    num_cycles: int = 0,
    steps_per_cycle: int = 0
) -> str:
    """Apply a Phase 2.6 rhythmic preset, generating a complete oscillation trajectory.

    Layer 2: Deterministic forced-orbit integration (0 tokens).

    Args:
        preset_name: Name of preset (e.g. 'temporal_weave', 'scale_functor').
        num_cycles: Override number of cycles (0 = use preset default).
        steps_per_cycle: Override steps per cycle (0 = use preset default).

    Returns complete trajectory as array of 5D coordinate snapshots with
    per-step nearest canonical state identification.
    """
    if preset_name not in NEO_ANDEAN_RHYTHMIC_PRESETS:
        return json.dumps({
            "error": f"Unknown preset: {preset_name}",
            "available": list(NEO_ANDEAN_RHYTHMIC_PRESETS.keys())
        })

    cfg = dict(NEO_ANDEAN_RHYTHMIC_PRESETS[preset_name])
    if num_cycles > 0:
        cfg["num_cycles"] = min(num_cycles, 10)
    if steps_per_cycle > 0:
        cfg["steps_per_cycle"] = max(4, min(steps_per_cycle, 60))

    trajectory = _generate_preset_trajectory(cfg)
    total_steps = len(trajectory)

    # Convert to list of dicts with nearest-state annotation
    steps = []
    for i in range(total_steps):
        coords = {p: round(float(trajectory[i, j]), 4) for j, p in enumerate(PARAMETER_NAMES)}
        nearest = min(
            CANONICAL_STATES.items(),
            key=lambda item: _euclidean_distance(coords, item[1]["coordinates"])
        )
        steps.append({
            "step": i,
            "coordinates": coords,
            "nearest_state": nearest[0],
            "state_distance": round(_euclidean_distance(coords, nearest[1]["coordinates"]), 4)
        })

    return json.dumps({
        "preset": preset_name,
        "pattern": cfg["pattern"],
        "period": cfg["steps_per_cycle"],
        "num_cycles": cfg["num_cycles"],
        "total_steps": total_steps,
        "state_a": cfg["state_a"],
        "state_b": cfg["state_b"],
        "trajectory": steps
    }, indent=2)


@mcp.tool()
def generate_rhythmic_neo_andean_sequence(
    preset_name: str,
    num_cycles: int = 0,
    steps_per_cycle: int = 0
) -> str:
    """Generate rhythmic oscillation between two Neo-Andean configurations.

    Layer 2: Deterministic forced-orbit composition (0 tokens).

    Produces a complete oscillation sequence with visual vocabulary,
    color palette, and symbolic elements mapped at each keyframe.
    Suitable for animation keyframes or temporal prompt sequences.

    Args:
        preset_name: Name of preset (e.g. 'abundance_pulse').
        num_cycles: Override cycle count (0 = default).
        steps_per_cycle: Override period (0 = default).

    Returns keyframe sequence with full visual mapping at each step.
    """
    if preset_name not in NEO_ANDEAN_RHYTHMIC_PRESETS:
        return json.dumps({
            "error": f"Unknown preset: {preset_name}",
            "available": list(NEO_ANDEAN_RHYTHMIC_PRESETS.keys())
        })

    cfg = dict(NEO_ANDEAN_RHYTHMIC_PRESETS[preset_name])
    if num_cycles > 0:
        cfg["num_cycles"] = min(num_cycles, 10)
    if steps_per_cycle > 0:
        cfg["steps_per_cycle"] = max(4, min(steps_per_cycle, 60))

    trajectory = _generate_preset_trajectory(cfg)
    total_steps = len(trajectory)

    # Sample keyframes (every step for short presets, every Nth for long)
    sample_rate = max(1, total_steps // 24)  # Cap at ~24 keyframes for output size
    keyframes = []

    for i in range(0, total_steps, sample_rate):
        coords = {p: round(float(trajectory[i, j]), 4) for j, p in enumerate(PARAMETER_NAMES)}

        # Map each keyframe through the visual pipeline
        geometry = _select_geometry(coords["chacha_warmi"])
        palette = _select_palette(coords["chromatic_intensity"])
        symbols = _select_symbols(coords["symbolic_density"])
        vocab = _extract_visual_vocabulary_from_params(coords)

        keyframes.append({
            "step": i,
            "cycle": i // cfg["steps_per_cycle"],
            "phase_in_cycle": round((i % cfg["steps_per_cycle"]) / cfg["steps_per_cycle"], 3),
            "coordinates": coords,
            "visual_type": vocab["nearest_type"],
            "type_distance": vocab["distance"],
            "geometry_mode": geometry["description"],
            "palette_colors": [c["name"] for c in palette[:4]],
            "active_symbols": [s["name"] for s in symbols[:3]],
            "image_keywords": vocab["keywords"][:4]
        })

    return json.dumps({
        "preset": preset_name,
        "description": cfg["description"],
        "period": cfg["steps_per_cycle"],
        "num_cycles": cfg["num_cycles"],
        "total_steps": total_steps,
        "sample_rate": sample_rate,
        "keyframe_count": len(keyframes),
        "keyframes": keyframes
    }, indent=2)


# =============================================================================
# PHASE 2.7 — Attractor Visualization Prompt Generation (Layer 2: 0 tokens)
# =============================================================================

@mcp.tool()
def get_neo_andean_visual_types() -> str:
    """List all Neo-Andean visual vocabulary types with coordinates and keywords.

    Layer 2: Pure lookup (0 tokens).

    Returns the 5 canonical visual types spanning the Neo-Andean morphospace,
    each with 5D coordinates and image-generation-ready keyword lists.
    Types range from Tiwanaku archaeological through aguayo textile,
    cholet polychrome, cholita festival, to El Altopia neon futurism.
    """
    result = {}
    for vtype, spec in NEO_ANDEAN_VISUAL_TYPES.items():
        result[vtype] = {
            "coordinates": spec["coords"],
            "keywords": spec["keywords"],
            "keyword_count": len(spec["keywords"])
        }
    return json.dumps({
        "domain": "neo_andean",
        "phase": "2.7",
        "visual_type_count": len(result),
        "visual_types": result
    }, indent=2)


@mcp.tool()
def generate_neo_andean_attractor_prompt(
    chacha_warmi: float = 0.5,
    chromatic_intensity: float = 0.5,
    symbolic_density: float = 0.5,
    scale_register: float = 0.5,
    temporal_composite: float = 0.5,
    strength: float = 1.0,
    mode: str = "composite"
) -> str:
    """Generate image-generation-ready prompt from 5D attractor coordinates.

    Layer 2: Deterministic vocabulary extraction (0 tokens).

    Maps any point in Neo-Andean parameter space to the nearest visual
    vocabulary type and returns weighted keywords suitable for Stable
    Diffusion, DALL-E, or ComfyUI prompt construction.

    Args:
        chacha_warmi: 0.0 (angular/chacha) to 1.0 (organic/warmi).
        chromatic_intensity: 0.0 (earth/stone) to 1.0 (neon/LED).
        symbolic_density: 0.0 (geometric) to 1.0 (iconographic).
        scale_register: 0.0 (textile) to 1.0 (monumental).
        temporal_composite: 0.0 (pre-Columbian) to 1.0 (futurism).
        strength: Domain weight for multi-domain composition (0.0-1.0).
        mode: 'composite' (blended prompt), 'detailed' (full breakdown).

    Returns prompt-ready keywords with visual type identification and
    distance metric for confidence assessment.
    """
    params = {
        "chacha_warmi": max(0.0, min(1.0, chacha_warmi)),
        "chromatic_intensity": max(0.0, min(1.0, chromatic_intensity)),
        "symbolic_density": max(0.0, min(1.0, symbolic_density)),
        "scale_register": max(0.0, min(1.0, scale_register)),
        "temporal_composite": max(0.0, min(1.0, temporal_composite))
    }
    strength = max(0.0, min(1.0, strength))

    vocab = _extract_visual_vocabulary_from_params(params, strength)

    # Also get secondary match for blending when between types
    query = np.array([params[p] for p in PARAMETER_NAMES])
    type_distances = []
    for vtype, spec in NEO_ANDEAN_VISUAL_TYPES.items():
        ref = np.array([spec["coords"][p] for p in PARAMETER_NAMES])
        dist = float(np.linalg.norm(query - ref))
        type_distances.append((vtype, dist, spec["keywords"]))
    type_distances.sort(key=lambda x: x[1])

    # Weight keywords by inverse distance (closer type = more keywords)
    if mode == "composite":
        # Use primary type's full keywords, add secondary if close
        primary = type_distances[0]
        secondary = type_distances[1] if len(type_distances) > 1 else None

        weighted_keywords = list(primary[2])
        if secondary and secondary[1] < 0.5:
            # Blend in secondary keywords that don't duplicate
            primary_set = set(weighted_keywords)
            blend_count = max(1, int(len(secondary[2]) * (1.0 - secondary[1] / 0.5)))
            for kw in secondary[2][:blend_count]:
                if kw not in primary_set:
                    weighted_keywords.append(kw)

        # Apply strength weighting: reduce keyword count for low strength
        if strength < 1.0:
            keep = max(2, int(len(weighted_keywords) * strength))
            weighted_keywords = weighted_keywords[:keep]

        # Add color palette context
        palette = _select_palette(params["chromatic_intensity"])
        palette_note = ", ".join(c["name"].replace("_", " ") for c in palette[:3])

        result = {
            "mode": "composite",
            "prompt_keywords": weighted_keywords,
            "palette_context": palette_note,
            "nearest_visual_type": vocab["nearest_type"],
            "type_distance": vocab["distance"],
            "domain_strength": strength,
            "coordinates": params
        }

    else:  # detailed mode
        geometry = _select_geometry(params["chacha_warmi"])
        palette = _select_palette(params["chromatic_intensity"])
        symbols = _select_symbols(params["symbolic_density"])

        nearest_state = min(
            CANONICAL_STATES.items(),
            key=lambda item: _euclidean_distance(params, item[1]["coordinates"])
        )

        result = {
            "mode": "detailed",
            "nearest_visual_type": vocab["nearest_type"],
            "type_distance": vocab["distance"],
            "all_type_distances": {
                td[0]: round(td[1], 4) for td in type_distances
            },
            "primary_keywords": type_distances[0][2],
            "secondary_keywords": type_distances[1][2] if len(type_distances) > 1 else [],
            "geometry": geometry,
            "palette": [{"name": c["name"], "hex": c["hex"]} for c in palette[:5]],
            "symbols": [s["name"] for s in symbols[:4]],
            "nearest_canonical_state": {
                "name": nearest_state[0],
                "distance": round(_euclidean_distance(params, nearest_state[1]["coordinates"]), 4)
            },
            "domain_strength": strength,
            "coordinates": params
        }

    return json.dumps(result, indent=2)


# =============================================================================
# LAYER 3 — Structured data for Claude synthesis
# =============================================================================

@mcp.tool()
def enhance_neo_andean_prompt(
    intent: str,
    domain: str = "both",
    canonical_state: str = "",
    intensity: float = 0.7
) -> str:
    """Full pipeline: intent + optional state + domain → structured enhancement data.

    Layer 3: Provides structured data for Claude synthesis (~100-200 tokens).

    Args:
        intent: Natural language description of desired aesthetic.
        domain: 'architecture', 'fashion', or 'both'.
        canonical_state: Optional canonical state to anchor the enhancement.
        intensity: Enhancement intensity 0.0-1.0 (default 0.7).

    Returns complete structured data including coordinates, compositional
    geometry, visual vocabulary, color associations, and symbolic elements
    for Claude to synthesize into a final image generation prompt.
    """
    # Step 1: Decompose intent into coordinates
    intent_result = json.loads(decompose_intent(intent))
    coordinates = intent_result["coordinates"]
    detected_domain = intent_result["detected_domain"]

    # Override domain if explicitly provided and different from 'both'
    if domain != "both":
        detected_domain = domain

    # Step 2: If canonical state provided, blend with intent
    if canonical_state and canonical_state in CANONICAL_STATES:
        state_coords = CANONICAL_STATES[canonical_state]["coordinates"]
        # Blend: intent weighted by intensity, state fills the rest
        for axis in coordinates:
            coordinates[axis] = round(
                coordinates[axis] * intensity + state_coords[axis] * (1 - intensity), 3
            )

    # Step 3: Map to full visual specification
    mapping_result = json.loads(map_coordinates(
        chacha_warmi=coordinates["chacha_warmi"],
        chromatic_intensity=coordinates["chromatic_intensity"],
        symbolic_density=coordinates["symbolic_density"],
        scale_register=coordinates["scale_register"],
        temporal_composite=coordinates["temporal_composite"],
        domain=detected_domain
    ))

    # Step 4: Assemble enhancement data
    enhancement = {
        "intent": intent,
        "domain": detected_domain,
        "intensity": intensity,
        "coordinates": coordinates,
        "geometry": mapping_result["geometry"],
        "palette": mapping_result["palette"],
        "symbols": [s["name"] for s in mapping_result["symbols"][:5]],
        "nearest_canonical_state": mapping_result["nearest_canonical_state"],
        "angle_constraints": GEOMETRIC_CONSTRAINTS["primary_angles"],
    }

    # Add domain-specific vocabulary
    if detected_domain in ("architecture", "both") and "architecture" in mapping_result:
        enhancement["architecture_vocabulary"] = mapping_result["architecture"]
    if detected_domain in ("fashion", "both") and "fashion" in mapping_result:
        enhancement["fashion_vocabulary"] = mapping_result["fashion"]

    # Step 5: Add cross-domain functor note
    if detected_domain == "both":
        enhancement["cross_domain_functor"] = {
            "principle": "Textile-to-architecture functor: the same symbolic content expressed at different scales with structure-preserving mapping.",
            "fashion_zone": mapping_result.get("fashion", {}).get("zone", ""),
            "architecture_zone": mapping_result.get("architecture", {}).get("zone", ""),
            "shared_elements": "aguayo pattern, chakana geometry, chacha-warmi duality"
        }

    return json.dumps(enhancement, indent=2)


@mcp.tool()
def get_domain_registry_config() -> str:
    """Return Tier 4D integration configuration for compositional limit cycles.

    Layer 2: Pure lookup (0 tokens).

    Returns the domain signature for registering with
    aesthetic-dynamics-core multi-domain composition, including
    Phase 2.6 preset periods and predicted emergent attractors.
    """
    preset_periods = sorted(set(
        cfg["steps_per_cycle"] for cfg in NEO_ANDEAN_RHYTHMIC_PRESETS.values()
    ))
    return json.dumps({
        "domain_name": "neo_andean",
        "version": "2.6.0",
        "coordinate_space": {
            "dimensions": 5,
            "axes": list(COORDINATE_AXES.keys()),
            "parameter_names": PARAMETER_NAMES,
            "ranges": {ax: [0.0, 1.0] for ax in COORDINATE_AXES}
        },
        "canonical_states": list(CANONICAL_STATES.keys()),
        "domains": ["architecture", "fashion"],
        "cross_domain_functors": ["textile_to_architecture", "architecture_to_fashion"],
        "composable_axes": {
            "chacha_warmi": "tension_axis",
            "chromatic_intensity": "energy_axis",
            "symbolic_density": "complexity_axis",
            "scale_register": "zoom_axis",
            "temporal_composite": "temporal_axis"
        },
        "phase_2_6": {
            "status": "complete",
            "preset_count": len(NEO_ANDEAN_RHYTHMIC_PRESETS),
            "periods": preset_periods,
            "presets": {
                name: {
                    "period": cfg["steps_per_cycle"],
                    "pattern": cfg["pattern"],
                    "states": f"{cfg['state_a']} ↔ {cfg['state_b']}"
                }
                for name, cfg in NEO_ANDEAN_RHYTHMIC_PRESETS.items()
            }
        },
        "phase_2_7": {
            "status": "complete",
            "visual_type_count": len(NEO_ANDEAN_VISUAL_TYPES),
            "visual_types": list(NEO_ANDEAN_VISUAL_TYPES.keys()),
            "prompt_modes": ["composite", "detailed"]
        },
        "predicted_emergent_attractors": [
            {
                "type": "gap_filler",
                "predicted_period": 14,
                "mechanism": "Fills 12-15 gap in period landscape",
                "estimated_basin_size": 0.04,
                "confidence": "high",
                "notes": "abundance_pulse preset at P14 is only domain with this period"
            },
            {
                "type": "lcm_sync",
                "predicted_period": 28,
                "mechanism": "Reinforces known P28 composite beat (60-2×16). futurist_evolution preset.",
                "estimated_basin_size": 0.06,
                "confidence": "medium",
                "notes": "May strengthen fragile P28 attractor with additional domain reinforcement"
            },
            {
                "type": "harmonic",
                "predicted_period": 126,
                "mechanism": "LCM(14,18) — neo_andean × nuclear/catastrophe/diatom",
                "estimated_basin_size": 0.02,
                "confidence": "low",
                "notes": "Novel high-period harmonic from P14 gap-filler"
            },
            {
                "type": "multi_domain_sync",
                "predicted_period": 20,
                "mechanism": "4-domain reinforcement: neo_andean + microscopy + catastrophe + diatom",
                "estimated_basin_size": 0.08,
                "confidence": "high",
                "notes": "chromatic_ascent preset adds fourth domain to P20 synchronization"
            }
        ],
        "integration_notes": "Chacha-warmi maps to generic tension in other domains. Chromatic intensity maps to energy/saturation. Scale register is unique to this domain's textile→garment→architecture functor. P14 (abundance_pulse) introduces first period in 12-15 gap across all registered domains."
    }, indent=2)


@mcp.tool()
def get_server_info() -> str:
    """Get server metadata and capabilities.

    Layer 1: Pure reference (0 tokens).
    """
    return json.dumps({
        "name": "neo_andean_mcp",
        "version": "2.6.0",
        "description": "Neo-Andean aesthetic enhancement server covering architecture (cholet) and fashion (cholita) domains. Shared 5D coordinate space derived from Aymara textile traditions, Tiwanaku iconography, and contemporary El Alto visual culture.",
        "domains": ["architecture", "fashion"],
        "coordinate_axes": list(COORDINATE_AXES.keys()),
        "parameter_names": PARAMETER_NAMES,
        "canonical_states": len(CANONICAL_STATES),
        "symbolic_elements": len(SYMBOLIC_ELEMENTS),
        "color_palettes": len(COLOR_PALETTES),
        "layer_architecture": {
            "layer_1": "Pure taxonomy lookup — coordinate axes, symbols, palettes, vocabulary (0 tokens)",
            "layer_2": "Deterministic mapping — coordinate→vocabulary, distance, trajectory, intent decomposition, rhythmic presets, attractor prompts (0 tokens)",
            "layer_3": "Structured enhancement data — full pipeline for Claude synthesis (~100-200 tokens)"
        },
        "phase_2_6_enhancements": {
            "rhythmic_presets": True,
            "preset_count": len(NEO_ANDEAN_RHYTHMIC_PRESETS),
            "periods": sorted(set(
                cfg["steps_per_cycle"] for cfg in NEO_ANDEAN_RHYTHMIC_PRESETS.values()
            )),
            "forced_orbit_integration": True,
            "tools": [
                "list_neo_andean_presets",
                "apply_neo_andean_preset",
                "generate_rhythmic_neo_andean_sequence"
            ]
        },
        "phase_2_7_enhancements": {
            "attractor_visualization": True,
            "visual_type_count": len(NEO_ANDEAN_VISUAL_TYPES),
            "visual_types": list(NEO_ANDEAN_VISUAL_TYPES.keys()),
            "prompt_modes": ["composite", "detailed"],
            "tools": [
                "get_neo_andean_visual_types",
                "generate_neo_andean_attractor_prompt"
            ]
        },
        "key_concepts": {
            "chacha_warmi": "Angular/organic duality from Tiwanaku cosmology",
            "textile_architecture_functor": "Structure-preserving mapping: weave → garment → facade",
            "abundance_principle": "Recursive 'always more' aesthetic driving both domains",
            "temporal_composite": "Multiple historical periods coexisting simultaneously"
        }
    }, indent=2)

if __name__ == "__main__":
    mcp.run()
