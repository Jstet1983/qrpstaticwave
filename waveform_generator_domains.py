#!/usr/bin/env python3
"""Generate comprehensive domain-specific waveform symbols."""

import json
from typing import List
from waveform_static_db import WaveformSymbol, create_waveform_symbol


def generate_machine_code() -> List[WaveformSymbol]:
    """Generate machine code and assembly instruction symbols."""
    instructions = [
        ("MOV", "Move instruction"),
        ("LEA", "Load effective address"),
        ("MOVZX", "Move with zero extend"),
        ("MOVSX", "Move with sign extend"),
        ("XCHG", "Exchange instruction"),
        ("PUSH", "Push to stack"),
        ("POP", "Pop from stack"),
        ("CMP", "Compare instruction"),
        ("TEST", "Test instruction"),
        ("JMP", "Unconditional jump"),
        ("JE", "Jump if equal"),
        ("JNE", "Jump if not equal"),
        ("JL", "Jump if less"),
        ("JLE", "Jump if less or equal"),
        ("JG", "Jump if greater"),
        ("JGE", "Jump if greater or equal"),
        ("CALL", "Call subroutine"),
        ("RET", "Return from subroutine"),
        ("SHL", "Shift left"),
        ("SHR", "Shift right"),
        ("SAL", "Arithmetic shift left"),
        ("SAR", "Arithmetic shift right"),
        ("ROL", "Rotate left"),
        ("ROR", "Rotate right"),
        ("IMUL", "Integer multiply"),
        ("IDIV", "Integer divide"),
        ("INC", "Increment"),
        ("DEC", "Decrement"),
        ("NEG", "Negate"),
        ("NOT", "Bitwise NOT"),
        ("AND", "Bitwise AND"),
        ("OR", "Bitwise OR"),
        ("XOR", "Bitwise XOR"),
        ("NOP", "No operation"),
        ("HLT", "Halt"),
        ("CLI", "Clear interrupt"),
        ("STI", "Set interrupt"),
        ("CLD", "Clear direction"),
        ("STD", "Set direction"),
    ]
    return [create_waveform_symbol(name, "machine_code", description=desc) for name, desc in instructions]


def generate_programming_languages() -> List[WaveformSymbol]:
    """Generate programming language identifiers."""
    languages = [
        ("PYTHON", "Python language"),
        ("JAVASCRIPT", "JavaScript language"),
        ("TYPESCRIPT", "TypeScript language"),
        ("JAVA", "Java language"),
        ("CSHARP", "C# language"),
        ("CPP", "C++ language"),
        ("RUST", "Rust language"),
        ("GO", "Go language"),
        ("RUBY", "Ruby language"),
        ("PERL", "Perl language"),
        ("PHP", "PHP language"),
        ("KOTLIN", "Kotlin language"),
        ("SWIFT", "Swift language"),
        ("OBJECTIVE_C", "Objective-C language"),
        ("SCALA", "Scala language"),
        ("HASKELL", "Haskell language"),
        ("LISP", "Lisp language"),
        ("CLOJURE", "Clojure language"),
        ("ERLANG", "Erlang language"),
        ("ELIXIR", "Elixir language"),
        ("SCHEME", "Scheme language"),
        ("RACKET", "Racket language"),
        ("PROLOG", "Prolog language"),
        ("MATLAB", "MATLAB language"),
        ("OCTAVE", "GNU Octave"),
        ("R_LANG", "R language"),
        ("JULIA", "Julia language"),
        ("LUA", "Lua language"),
        ("GROOVY", "Groovy language"),
        ("DART", "Dart language"),
    ]
    return [create_waveform_symbol(name, "programming_language", description=desc) for name, desc in languages]


def generate_mathematical_concepts() -> List[WaveformSymbol]:
    """Generate mathematical concept symbols."""
    concepts = [
        ("ALGEBRA", "Algebra concept"),
        ("GEOMETRY", "Geometry concept"),
        ("TRIGONOMETRY", "Trigonometry concept"),
        ("CALCULUS", "Calculus concept"),
        ("LINEAR_ALGEBRA", "Linear algebra concept"),
        ("ABSTRACT_ALGEBRA", "Abstract algebra concept"),
        ("REAL_ANALYSIS", "Real analysis concept"),
        ("COMPLEX_ANALYSIS", "Complex analysis concept"),
        ("FUNCTIONAL_ANALYSIS", "Functional analysis concept"),
        ("TOPOLOGY", "Topology concept"),
        ("MEASURE_THEORY", "Measure theory concept"),
        ("PROBABILITY", "Probability theory"),
        ("STATISTICS", "Statistics concept"),
        ("DISCRETE_MATH", "Discrete mathematics"),
        ("COMBINATORICS", "Combinatorics concept"),
        ("GRAPH_THEORY", "Graph theory concept"),
        ("NUMBER_THEORY", "Number theory concept"),
        ("SET_THEORY", "Set theory concept"),
        ("LOGIC_MATH", "Mathematical logic"),
        ("CATEGORY_THEORY", "Category theory"),
        ("MATRIX", "Matrix concept"),
        ("VECTOR", "Vector concept"),
        ("TENSOR", "Tensor concept"),
        ("MANIFOLD", "Manifold concept"),
        ("GROUP", "Group theory"),
        ("RING", "Ring theory"),
        ("FIELD", "Field theory"),
        ("EIGENVALUE", "Eigenvalue concept"),
        ("EIGENVECTOR", "Eigenvector concept"),
        ("DETERMINANT", "Determinant concept"),
    ]
    return [create_waveform_symbol(name, "mathematics", description=desc) for name, desc in concepts]


def generate_chemistry_concepts() -> List[WaveformSymbol]:
    """Generate chemistry concept and element symbols."""
    elements = [
        ("HYDROGEN", "Hydrogen (H)"),
        ("HELIUM", "Helium (He)"),
        ("LITHIUM", "Lithium (Li)"),
        ("BERYLLIUM", "Beryllium (Be)"),
        ("BORON", "Boron (B)"),
        ("CARBON", "Carbon (C)"),
        ("NITROGEN", "Nitrogen (N)"),
        ("OXYGEN", "Oxygen (O)"),
        ("FLUORINE", "Fluorine (F)"),
        ("NEON", "Neon (Ne)"),
        ("SODIUM", "Sodium (Na)"),
        ("MAGNESIUM", "Magnesium (Mg)"),
        ("ALUMINUM", "Aluminum (Al)"),
        ("SILICON", "Silicon (Si)"),
        ("PHOSPHORUS", "Phosphorus (P)"),
        ("SULFUR", "Sulfur (S)"),
        ("CHLORINE", "Chlorine (Cl)"),
        ("ARGON", "Argon (Ar)"),
        ("POTASSIUM", "Potassium (K)"),
        ("CALCIUM", "Calcium (Ca)"),
        ("IRON", "Iron (Fe)"),
        ("COPPER", "Copper (Cu)"),
        ("ZINC", "Zinc (Zn)"),
        ("SILVER", "Silver (Ag)"),
        ("GOLD", "Gold (Au)"),
        ("LEAD", "Lead (Pb)"),
        ("MERCURY", "Mercury (Hg)"),
        ("URANIUM", "Uranium (U)"),
    ]
    concepts = [
        ("ORGANIC_CHEMISTRY", "Organic chemistry"),
        ("INORGANIC_CHEMISTRY", "Inorganic chemistry"),
        ("BIOCHEMISTRY", "Biochemistry"),
        ("PHYSICAL_CHEMISTRY", "Physical chemistry"),
        ("ANALYTICAL_CHEMISTRY", "Analytical chemistry"),
        ("POLYMER_CHEMISTRY", "Polymer chemistry"),
        ("REACTION", "Chemical reaction"),
        ("KINETICS", "Reaction kinetics"),
        ("THERMODYNAMICS", "Thermodynamics"),
        ("EQUILIBRIUM", "Chemical equilibrium"),
        ("CATALYST", "Catalyst concept"),
        ("OXIDATION", "Oxidation process"),
        ("REDUCTION", "Reduction process"),
        ("ACID_BASE", "Acid-base chemistry"),
        ("SPECTROSCOPY", "Spectroscopy technique"),
        ("CHROMATOGRAPHY", "Chromatography technique"),
    ]
    all_symbols = [create_waveform_symbol(name, "element", description=desc) for name, desc in elements]
    all_symbols.extend([create_waveform_symbol(name, "chemistry_concept", description=desc) for name, desc in concepts])
    return all_symbols


def generate_physics_concepts() -> List[WaveformSymbol]:
    """Generate physics concept symbols."""
    concepts = [
        ("MECHANICS", "Classical mechanics"),
        ("KINEMATICS", "Kinematics concept"),
        ("DYNAMICS", "Dynamics concept"),
        ("STATICS", "Statics concept"),
        ("THERMODYNAMICS", "Thermodynamics"),
        ("ELECTROMAGNETISM", "Electromagnetism"),
        ("OPTICS", "Optics concept"),
        ("WAVES", "Wave physics"),
        ("ACOUSTICS", "Acoustics concept"),
        ("QUANTUM_MECHANICS", "Quantum mechanics"),
        ("RELATIVITY", "Relativity theory"),
        ("SPECIAL_RELATIVITY", "Special relativity"),
        ("GENERAL_RELATIVITY", "General relativity"),
        ("PARTICLE_PHYSICS", "Particle physics"),
        ("NUCLEAR_PHYSICS", "Nuclear physics"),
        ("ASTRO_PHYSICS", "Astrophysics"),
        ("COSMOLOGY", "Cosmology concept"),
        ("PLASMA_PHYSICS", "Plasma physics"),
        ("FLUID_DYNAMICS", "Fluid dynamics"),
        ("SOLID_STATE", "Solid state physics"),
        ("CONDENSED_MATTER", "Condensed matter physics"),
        ("PHOTONICS", "Photonics concept"),
        ("SUPERCONDUCTIVITY", "Superconductivity"),
        ("SUPERFLUIDITY", "Superfluidity concept"),
        ("BOSE_EINSTEIN", "Bose-Einstein statistics"),
        ("FERMI_DIRAC", "Fermi-Dirac statistics"),
        ("STRING_THEORY", "String theory"),
        ("LOOP_QUANTUM", "Loop quantum gravity"),
        ("FIELD_THEORY", "Quantum field theory"),
        ("LAGRANGIAN", "Lagrangian formalism"),
        ("HAMILTONIAN", "Hamiltonian formalism"),
    ]
    return [create_waveform_symbol(name, "physics", description=desc) for name, desc in concepts]


def generate_mechanical_engineering() -> List[WaveformSymbol]:
    """Generate mechanical engineering concept symbols."""
    concepts = [
        ("STATICS", "Statics in mechanics"),
        ("DYNAMICS", "Dynamics in mechanics"),
        ("KINEMATICS", "Kinematics in mechanisms"),
        ("STRESS", "Stress analysis"),
        ("STRAIN", "Strain analysis"),
        ("ELASTICITY", "Elasticity concept"),
        ("PLASTICITY", "Plasticity concept"),
        ("CREEP", "Creep behavior"),
        ("FATIGUE", "Fatigue analysis"),
        ("FRACTURE_MECHANICS", "Fracture mechanics"),
        ("VIBRATION", "Vibration analysis"),
        ("MODAL_ANALYSIS", "Modal analysis"),
        ("FINITE_ELEMENT", "Finite element method"),
        ("BOUNDARY_ELEMENT", "Boundary element method"),
        ("HEAT_TRANSFER", "Heat transfer concept"),
        ("CONDUCTION", "Thermal conduction"),
        ("CONVECTION", "Thermal convection"),
        ("RADIATION", "Thermal radiation"),
        ("FLUID_MECHANICS", "Fluid mechanics"),
        ("LAMINAR_FLOW", "Laminar flow"),
        ("TURBULENT_FLOW", "Turbulent flow"),
        ("COMPRESSIBLE_FLOW", "Compressible flow"),
        ("AERODYNAMICS", "Aerodynamics concept"),
        ("HYDRODYNAMICS", "Hydrodynamics concept"),
        ("GEAR_DESIGN", "Gear design"),
        ("BEARING_DESIGN", "Bearing design"),
        ("SPRING_DESIGN", "Spring design"),
        ("WELDS", "Welding and joining"),
        ("COMPOSITES", "Composite materials"),
        ("MACHINE_DESIGN", "Machine design"),
        ("CAM_MECHANISM", "Cam and follower"),
        ("LINKAGE", "Linkage mechanisms"),
        ("RELIABILITY", "Reliability engineering"),
        ("QUALITY_CONTROL", "Quality control"),
        ("OPTIMIZATION", "Design optimization"),
        ("SIMULATION", "Engineering simulation"),
    ]
    return [create_waveform_symbol(name, "mechanical_engineering", description=desc) for name, desc in concepts]


def symbol_to_dict(symbol: WaveformSymbol) -> dict:
    """Convert symbol to JSON-serializable dict."""
    return {
        "name": symbol.name,
        "frequency": symbol.frequency,
        "phase": symbol.phase,
        "amplitude": symbol.amplitude,
        "harmonic": symbol.harmonic,
        "envelope": symbol.envelope,
        "category": symbol.category,
        "opcode": symbol.opcode,
        "description": symbol.description,
    }


def save_symbols(filepath: str, symbols: List[WaveformSymbol]) -> None:
    """Save symbols to a JSON file."""
    data = [symbol_to_dict(s) for s in symbols]
    with open(filepath, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)
    print(f"Saved {len(symbols)} symbols to {filepath}")


def main() -> int:
    """Generate domain-specific symbol files."""
    generators = [
        ("machine_code_instructions.json", generate_machine_code),
        ("programming_languages_expanded.json", generate_programming_languages),
        ("mathematical_concepts.json", generate_mathematical_concepts),
        ("chemistry_expanded.json", generate_chemistry_concepts),
        ("physics_concepts.json", generate_physics_concepts),
        ("mechanical_engineering.json", generate_mechanical_engineering),
    ]

    all_symbols: List[WaveformSymbol] = []
    
    for filename, generator_fn in generators:
        symbols = generator_fn()
        save_symbols(filename, symbols)
        all_symbols.extend(symbols)
        print(f"  Generated {len(symbols)} {generator_fn.__doc__.strip()}")

    print(f"\nTotal symbols generated: {len(all_symbols)}")
    print(f"Symbol categories:")
    categories = {}
    for symbol in all_symbols:
        categories[symbol.category] = categories.get(symbol.category, 0) + 1
    for category, count in sorted(categories.items()):
        print(f"  {category}: {count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
