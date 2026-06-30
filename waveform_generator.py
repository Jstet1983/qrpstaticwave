#!/usr/bin/env python3
"""Generate and expand the static waveform database with domain-specific symbols."""

import json
import math
from typing import Dict, List
from waveform_static_db import WaveformSymbol, create_waveform_symbol


def generate_math_functions() -> List[WaveformSymbol]:
    """Generate mathematical function symbols."""
    functions = [
        ("ABS", "Absolute value function"),
        ("CEIL", "Ceiling function"),
        ("FLOOR", "Floor function"),
        ("ROUND", "Rounding function"),
        ("EXP", "Exponential function"),
        ("POW", "Power function"),
        ("ASIN", "Inverse sine"),
        ("ACOS", "Inverse cosine"),
        ("ATAN", "Inverse tangent"),
        ("SINH", "Hyperbolic sine"),
        ("COSH", "Hyperbolic cosine"),
        ("TANH", "Hyperbolic tangent"),
        ("SIGN", "Sign function"),
        ("MIN", "Minimum function"),
        ("MAX", "Maximum function"),
        ("GCD", "Greatest common divisor"),
        ("LCM", "Least common multiple"),
        ("MOD", "Modulo function"),
        ("REM", "Remainder function"),
        ("TRUNC", "Truncate function"),
    ]
    return [create_waveform_symbol(name, "function", description=desc) for name, desc in functions]


def generate_logic_operators() -> List[WaveformSymbol]:
    """Generate logical operator symbols."""
    operators = [
        ("NOT", "Logical NOT"),
        ("AND", "Logical AND"),
        ("OR", "Logical OR"),
        ("XOR", "Logical XOR"),
        ("NAND", "Logical NAND"),
        ("NOR", "Logical NOR"),
        ("IMPLIES", "Logical implication"),
        ("IFF", "If and only if"),
        ("FORALL", "Universal quantifier"),
        ("EXISTS", "Existential quantifier"),
    ]
    return [create_waveform_symbol(name, "logic_operator", description=desc) for name, desc in operators]


def generate_comparison_operators() -> List[WaveformSymbol]:
    """Generate comparison operator symbols."""
    operators = [
        ("EQ", "Equal comparison"),
        ("NE", "Not equal comparison"),
        ("LT", "Less than comparison"),
        ("LE", "Less than or equal"),
        ("GT", "Greater than comparison"),
        ("GE", "Greater than or equal"),
        ("IN", "Membership test"),
        ("NOT_IN", "Non-membership test"),
    ]
    return [create_waveform_symbol(name, "comparison", description=desc) for name, desc in operators]


def generate_bitwise_operators() -> List[WaveformSymbol]:
    """Generate bitwise operator symbols."""
    operators = [
        ("BITAND", "Bitwise AND"),
        ("BITOR", "Bitwise OR"),
        ("BITXOR", "Bitwise XOR"),
        ("BITNOT", "Bitwise NOT"),
        ("LSHIFT", "Left shift"),
        ("RSHIFT", "Right shift"),
        ("ROTL", "Rotate left"),
        ("ROTR", "Rotate right"),
    ]
    return [create_waveform_symbol(name, "bitwise", description=desc) for name, desc in operators]


def generate_physical_constants() -> List[WaveformSymbol]:
    """Generate physical constant symbols."""
    constants = [
        ("ELECTRON_MASS", "Electron mass"),
        ("PROTON_MASS", "Proton mass"),
        ("FINE_STRUCTURE", "Fine structure constant"),
        ("MAGNETIC_MOMENT", "Magnetic moment"),
        ("RYDBERG", "Rydberg constant"),
        ("STEFAN_BOLTZMANN", "Stefan-Boltzmann constant"),
        ("GRAVITATIONAL", "Gravitational constant"),
        ("SPEED_OF_LIGHT", "Speed of light"),
        ("PLANCK_CONSTANT", "Planck constant"),
        ("IMPEDANCE_VACUUM", "Impedance of vacuum"),
    ]
    return [create_waveform_symbol(name, "physical_constant", description=desc) for name, desc in constants]


def generate_units() -> List[WaveformSymbol]:
    """Generate physical unit symbols."""
    units = [
        ("METER", "Unit of length"),
        ("KILOGRAM", "Unit of mass"),
        ("SECOND", "Unit of time"),
        ("AMPERE", "Unit of electric current"),
        ("KELVIN", "Unit of temperature"),
        ("MOLE", "Unit of substance"),
        ("CANDELA", "Unit of luminosity"),
        ("HERTZ", "Unit of frequency"),
        ("NEWTON", "Unit of force"),
        ("PASCAL", "Unit of pressure"),
        ("JOULE", "Unit of energy"),
        ("WATT", "Unit of power"),
        ("COULOMB", "Unit of electric charge"),
        ("VOLT", "Unit of electric potential"),
        ("OHMS", "Unit of electrical resistance"),
        ("FARAD", "Unit of capacitance"),
        ("HENRY", "Unit of inductance"),
        ("TESLA", "Unit of magnetic flux density"),
        ("WEBER", "Unit of magnetic flux"),
        ("SIEMENS", "Unit of electrical conductance"),
    ]
    return [create_waveform_symbol(name, "unit", description=desc) for name, desc in units]


def generate_chemistry_compounds() -> List[WaveformSymbol]:
    """Generate chemistry compound symbols."""
    compounds = [
        ("ETHANOL", "Ethanol (C2H6O)"),
        ("METHANOL", "Methanol (CH4O)"),
        ("ACETONE", "Acetone (C3H6O)"),
        ("BENZENE", "Benzene (C6H6)"),
        ("TOLUENE", "Toluene (C7H8)"),
        ("AMMONIA", "Ammonia (NH3)"),
        ("SULFURIC_ACID", "Sulfuric acid (H2SO4)"),
        ("NITRIC_ACID", "Nitric acid (HNO3)"),
        ("SALT", "Salt (NaCl)"),
        ("GLUCOSE", "Glucose (C6H12O6)"),
    ]
    return [create_waveform_symbol(name, "compound", description=desc) for name, desc in compounds]


def generate_data_structures() -> List[WaveformSymbol]:
    """Generate data structure type symbols."""
    structures = [
        ("ARRAY", "Array data structure"),
        ("LINKED_LIST", "Linked list structure"),
        ("STACK", "Stack structure"),
        ("QUEUE", "Queue structure"),
        ("TREE", "Tree structure"),
        ("BINARY_TREE", "Binary tree structure"),
        ("GRAPH", "Graph structure"),
        ("HASH_TABLE", "Hash table structure"),
        ("HEAP", "Heap structure"),
        ("TRIE", "Trie structure"),
        ("SET", "Set collection"),
        ("MAP", "Map collection"),
        ("TUPLE", "Tuple structure"),
        ("RECORD", "Record structure"),
        ("UNION", "Union type"),
    ]
    return [create_waveform_symbol(name, "data_structure", description=desc) for name, desc in structures]


def generate_algorithms() -> List[WaveformSymbol]:
    """Generate algorithm class symbols."""
    algorithms = [
        ("BUBBLE_SORT", "Bubble sort algorithm"),
        ("QUICK_SORT", "Quick sort algorithm"),
        ("MERGE_SORT", "Merge sort algorithm"),
        ("HEAP_SORT", "Heap sort algorithm"),
        ("INSERTION_SORT", "Insertion sort algorithm"),
        ("SELECTION_SORT", "Selection sort algorithm"),
        ("BINARY_SEARCH", "Binary search algorithm"),
        ("LINEAR_SEARCH", "Linear search algorithm"),
        ("DFS", "Depth-first search"),
        ("BFS", "Breadth-first search"),
        ("DIJKSTRA", "Dijkstra's algorithm"),
        ("BELLMAN_FORD", "Bellman-Ford algorithm"),
        ("FLOYD_WARSHALL", "Floyd-Warshall algorithm"),
        ("KRUSKAL", "Kruskal's algorithm"),
        ("PRIM", "Prim's algorithm"),
    ]
    return [create_waveform_symbol(name, "algorithm", description=desc) for name, desc in algorithms]


def generate_control_flow() -> List[WaveformSymbol]:
    """Generate control flow statement symbols."""
    statements = [
        ("SWITCH", "Switch statement"),
        ("CASE", "Case branch"),
        ("DEFAULT", "Default case"),
        ("BREAK", "Break statement"),
        ("CONTINUE", "Continue statement"),
        ("RETURN", "Return statement"),
        ("YIELD", "Yield statement"),
        ("TRY", "Try block"),
        ("CATCH", "Catch block"),
        ("FINALLY", "Finally block"),
        ("THROW", "Throw exception"),
        ("ASSERT", "Assert statement"),
        ("SYNCHRONIZED", "Synchronized block"),
        ("WITH", "With statement"),
        ("FOR_EACH", "For-each loop"),
    ]
    return [create_waveform_symbol(name, "control_flow", description=desc) for name, desc in statements]


def generate_meta_symbols() -> List[WaveformSymbol]:
    """Generate meta-programming and reflection symbols."""
    symbols = [
        ("TYPEOF", "Type inspection"),
        ("INSTANCEOF", "Instance check"),
        ("CLASS", "Class definition"),
        ("INTERFACE", "Interface definition"),
        ("ENUM", "Enumeration definition"),
        ("STRUCT", "Structure definition"),
        ("NAMESPACE", "Namespace scope"),
        ("MODULE", "Module scope"),
        ("IMPORT", "Import statement"),
        ("EXPORT", "Export statement"),
        ("PUBLIC", "Public visibility"),
        ("PRIVATE", "Private visibility"),
        ("PROTECTED", "Protected visibility"),
        ("STATIC", "Static member"),
        ("CONST", "Constant declaration"),
        ("VAR", "Variable declaration"),
        ("LET", "Lexically scoped variable"),
        ("ASYNC", "Asynchronous function"),
        ("AWAIT", "Await expression"),
        ("LAMBDA", "Lambda function"),
    ]
    return [create_waveform_symbol(name, "meta", description=desc) for name, desc in symbols]


def symbol_to_dict(symbol: WaveformSymbol) -> Dict[str, object]:
    """Convert a symbol to JSON-serializable dict."""
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
    """Generate and save expanded waveform database."""
    generators = [
        ("math_functions.json", generate_math_functions),
        ("logic_operators.json", generate_logic_operators),
        ("comparison_operators.json", generate_comparison_operators),
        ("bitwise_operators.json", generate_bitwise_operators),
        ("physical_constants.json", generate_physical_constants),
        ("units.json", generate_units),
        ("chemistry_compounds.json", generate_chemistry_compounds),
        ("data_structures.json", generate_data_structures),
        ("algorithms.json", generate_algorithms),
        ("control_flow.json", generate_control_flow),
        ("meta_symbols.json", generate_meta_symbols),
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
