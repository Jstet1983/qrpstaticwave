"""Static waveform database for QRP Static Wave."""

import math
from dataclasses import dataclass
from typing import Dict, Optional

@dataclass(frozen=True)
class WaveformSymbol:
    name: str
    frequency: float
    phase: float
    amplitude: float
    harmonic: int
    envelope: float
    category: str
    opcode: Optional[str] = None
    description: Optional[str] = None


def _normalize_token(name: str) -> str:
    return name.strip().upper()


def _frequency_for_token(name: str, base: float = 100.0, step: float = 2.5) -> float:
    total = sum(ord(ch) for ch in name)
    return base + (total % 1800) + len(name) * step


def _phase_for_token(name: str) -> float:
    return ((sum(ord(ch) for ch in name) % 16) * 0.4) % (2 * math.pi)


def _amplitude_for_token(name: str) -> float:
    return min(1.0, 0.40 + ((sum(ord(ch) for ch in name) % 60) / 100.0))


def _harmonic_for_token(name: str) -> int:
    return 1 + (sum(ord(ch) for ch in name) % 5)


def _envelope_for_token(name: str) -> float:
    return 0.30 + min(0.60, len(name) * 0.03)


def create_waveform_symbol(
    name: str,
    category: str,
    description: Optional[str] = None,
    opcode: Optional[str] = None,
    frequency: Optional[float] = None,
    phase: Optional[float] = None,
    amplitude: Optional[float] = None,
    harmonic: Optional[int] = None,
    envelope: Optional[float] = None,
) -> WaveformSymbol:
    if frequency is None:
        frequency = _frequency_for_token(name)
    if phase is None:
        phase = _phase_for_token(name)
    if amplitude is None:
        amplitude = _amplitude_for_token(name)
    if harmonic is None:
        harmonic = _harmonic_for_token(name)
    if envelope is None:
        envelope = _envelope_for_token(name)
    if description is None:
        description = f"Waveform symbol for {name}"
    return WaveformSymbol(
        name,
        frequency,
        phase,
        amplitude,
        harmonic,
        envelope,
        category,
        opcode=opcode,
        description=description,
    )


def create_ascii_symbol(character: str) -> WaveformSymbol:
    code = ord(character)
    if character == " ":
        category = "whitespace"
    elif character.isalpha():
        category = "letter"
    elif character.isdigit():
        category = "digit"
    elif character in "+-*/=<>!&|^%~,.:;?()[]{}\\\"'`@$#":
        category = "operator"
    else:
        category = "ascii"

    frequency = 100.0 + code * 2.3
    phase = (code % 8) * 0.4
    amplitude = 0.45 + ((code % 15) / 100.0)
    harmonic = 1 + (code % 4)
    envelope = 0.32 + ((code % 6) * 0.04)

    return WaveformSymbol(
        character,
        frequency,
        phase,
        amplitude,
        harmonic,
        envelope,
        category,
        description=f"ASCII {code} '{character}'",
    )


def _build_named_database() -> Dict[str, WaveformSymbol]:
    symbols: Dict[str, WaveformSymbol] = {}

    for code in range(32, 127):
        char = chr(code)
        symbols[char] = create_ascii_symbol(char)

    named_symbols = {
        "PI": create_waveform_symbol("PI", "constant", description="Mathematical constant π"),
        "E": create_waveform_symbol("E", "constant", description="Euler's number"),
        "PLANCK": create_waveform_symbol("PLANCK", "constant", description="Planck constant"),
        "G": create_waveform_symbol("G", "constant", description="Gravitational constant"),
        "C": create_waveform_symbol("C", "constant", description="Speed of light"),
        "KB": create_waveform_symbol("KB", "constant", description="Boltzmann constant"),
        "NA": create_waveform_symbol("NA", "constant", description="Avogadro's number"),
        "H2O": create_waveform_symbol("H2O", "molecule", description="Water molecule"),
        "CO2": create_waveform_symbol("CO2", "molecule", description="Carbon dioxide"),
        "O2": create_waveform_symbol("O2", "molecule", description="Oxygen molecule"),
        "H2": create_waveform_symbol("H2", "molecule", description="Hydrogen molecule"),
        "CH4": create_waveform_symbol("CH4", "molecule", description="Methane molecule"),
        "FE": create_waveform_symbol("FE", "element", description="Iron element"),
        "HE": create_waveform_symbol("HE", "element", description="Helium element"),
        "MATH": create_waveform_symbol("MATH", "knowledge", description="Mathematics domain"),
        "PHYSICS": create_waveform_symbol("PHYSICS", "knowledge", description="Physics domain"),
        "CHEMISTRY": create_waveform_symbol("CHEMISTRY", "knowledge", description="Chemistry domain"),
        "BIOLOGY": create_waveform_symbol("BIOLOGY", "knowledge", description="Biology domain"),
        "COMPUTER_SCIENCE": create_waveform_symbol("COMPUTER_SCIENCE", "knowledge", description="Computer science domain"),
        "PROGRAMMING": create_waveform_symbol("PROGRAMMING", "knowledge", description="Programming domain"),
        "PYTHON": create_waveform_symbol("PYTHON", "language", description="Python programming language"),
        "JAVASCRIPT": create_waveform_symbol("JAVASCRIPT", "language", description="JavaScript programming language"),
        "JAVA": create_waveform_symbol("JAVA", "language", description="Java programming language"),
        "CPP": create_waveform_symbol("CPP", "language", description="C++ programming language"),
        "C_SHARP": create_waveform_symbol("C_SHARP", "language", description="C# programming language"),
        "RUST": create_waveform_symbol("RUST", "language", description="Rust programming language"),
        "GO": create_waveform_symbol("GO", "language", description="Go programming language"),
        "SQL": create_waveform_symbol("SQL", "language", description="SQL query language"),
        "HTML": create_waveform_symbol("HTML", "language", description="HTML markup language"),
        "CSS": create_waveform_symbol("CSS", "language", description="CSS stylesheet language"),
        "BASH": create_waveform_symbol("BASH", "language", description="Bash shell language"),
        "DATA": create_waveform_symbol("DATA", "knowledge", description="Data abstraction"),
        "TIME": create_waveform_symbol("TIME", "knowledge", description="Time abstraction"),
        "ENERGY": create_waveform_symbol("ENERGY", "knowledge", description="Energy abstraction"),
        "FORCE": create_waveform_symbol("FORCE", "knowledge", description="Force abstraction"),
        "FIELD": create_waveform_symbol("FIELD", "knowledge", description="Field abstraction"),
        "WAVE": create_waveform_symbol("WAVE", "knowledge", description="Wave abstraction"),
        "MEMORY": create_waveform_symbol("MEMORY", "knowledge", description="Memory abstraction"),
        "TRUE": create_waveform_symbol("TRUE", "logic", description="Logical true"),
        "FALSE": create_waveform_symbol("FALSE", "logic", description="Logical false"),
        "IF": create_waveform_symbol("IF", "instruction", opcode="IF", description="Conditional branch"),
        "THEN": create_waveform_symbol("THEN", "instruction", opcode="THEN", description="Conditional target"),
        "ELSE": create_waveform_symbol("ELSE", "instruction", opcode="ELSE", description="Conditional alternate"),
        "LOOP": create_waveform_symbol("LOOP", "instruction", opcode="LOOP", description="Repeat block"),
        "FUNC": create_waveform_symbol("FUNC", "instruction", opcode="FUNC", description="Function definition"),
        "SQRT": create_waveform_symbol("SQRT", "function", description="Square root function"),
        "LOG": create_waveform_symbol("LOG", "function", description="Logarithm function"),
        "SIN": create_waveform_symbol("SIN", "function", description="Sine function"),
        "COS": create_waveform_symbol("COS", "function", description="Cosine function"),
        "TAN": create_waveform_symbol("TAN", "function", description="Tangent function"),
        "LOAD": create_waveform_symbol("LOAD", "instruction", opcode="LOAD", description="Load waveform into register"),
        "STORE": create_waveform_symbol("STORE", "instruction", opcode="STORE", description="Store register value"),
        "ADD": create_waveform_symbol("ADD", "instruction", opcode="ADD", description="Add two waveform values"),
        "SUB": create_waveform_symbol("SUB", "instruction", opcode="SUB", description="Subtract waveform values"),
        "MUL": create_waveform_symbol("MUL", "instruction", opcode="MUL", description="Multiply waveform values"),
        "DIV": create_waveform_symbol("DIV", "instruction", opcode="DIV", description="Divide waveform values"),
        "CMP": create_waveform_symbol("CMP", "instruction", opcode="CMP", description="Compare waveform values"),
        "EMIT": create_waveform_symbol("EMIT", "instruction", opcode="EMIT", description="Emit register output"),
        "SETCHAMBER": create_waveform_symbol("SETCHAMBER", "instruction", opcode="SETCHAMBER", description="Set virtual chamber geometry"),
        "NOP": create_waveform_symbol("NOP", "instruction", opcode="NOP", description="No operation"),
        "JMP": create_waveform_symbol("JMP", "instruction", opcode="JMP", description="Jump instruction"),
        "HLT": create_waveform_symbol("HLT", "instruction", opcode="HLT", description="Halt instruction"),
        "PUSH": create_waveform_symbol("PUSH", "instruction", opcode="PUSH", description="Push value to stack"),
        "POP": create_waveform_symbol("POP", "instruction", opcode="POP", description="Pop value from stack"),
    }

    symbols.update(named_symbols)
    return symbols


STATIC_WAVE_DB: Dict[str, WaveformSymbol] = _build_named_database()


DEFAULT_SYMBOL = WaveformSymbol("UNKNOWN", 120.0, 0.0, 0.40, 1, 0.30, "unknown", description="Unknown waveform")


def get_symbol(name: str) -> WaveformSymbol:
    if not name:
        return DEFAULT_SYMBOL
    key = _normalize_token(name)
    if key in STATIC_WAVE_DB:
        return STATIC_WAVE_DB[key]
    if len(name) == 1 and 32 <= ord(name) <= 126:
        return create_ascii_symbol(name)
    return create_waveform_symbol(name, "token", description=f"Generated waveform for token '{name}'")


def symbol_numeric_value(symbol: WaveformSymbol) -> float:
    return symbol.frequency * 0.01 + symbol.amplitude * 100 + symbol.phase * 10 + symbol.harmonic * 2
