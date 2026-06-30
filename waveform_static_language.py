"""Prototype interpreter for static waveform chamber computation."""

import argparse
import math
import re
from dataclasses import dataclass
from typing import List, Sequence

from waveform_static_db import DEFAULT_SYMBOL, WaveformSymbol, get_symbol, symbol_numeric_value, STATIC_WAVE_DB


@dataclass
class ChamberConfig:
    type: str
    curvature: float
    interference_gain: float


def create_chamber_config(chamber_type: str) -> ChamberConfig:
    if chamber_type == "hyperbolic":
        return ChamberConfig("hyperbolic", curvature=-1.0, interference_gain=1.25)
    if chamber_type == "parabolic":
        return ChamberConfig("parabolic", curvature=0.0, interference_gain=1.0)
    return ChamberConfig("elliptic", curvature=1.0, interference_gain=0.9)


def waveform_value(symbol: WaveformSymbol, position: float, chamber: ChamberConfig) -> float:
    base = symbol.amplitude * math.sin(2 * math.pi * symbol.frequency * position + symbol.phase)
    envelope = math.exp(-abs(chamber.curvature) * symbol.envelope * position)
    harmonic = math.sin(symbol.harmonic * 2 * math.pi * position)
    return base * envelope * (1 + 0.1 * harmonic) * chamber.interference_gain


def combine_waveforms(symbols: Sequence[WaveformSymbol], chamber: ChamberConfig, steps: int = 128) -> List[float]:
    result = []
    for step in range(steps):
        position = step / steps
        total = 0.0
        for symbol in symbols:
            total += waveform_value(symbol, position, chamber)
        result.append(total)
    return result


def compute_interference(symbols: Sequence[WaveformSymbol], chamber: ChamberConfig) -> float:
    values = combine_waveforms(symbols, chamber, steps=256)
    return sum(values) / len(values)


def infer_result(symbols: Sequence[WaveformSymbol], chamber: ChamberConfig) -> str:
    total = compute_interference(symbols, chamber)
    score = sum(symbol_numeric_value(symbol) for symbol in symbols)
    if total > 0.75 and score > 1000:
        return "RESONANT_TRUE"
    if total < -0.75 and score < 500:
        return "RESONANT_FALSE"
    return "INTERFERENCE_UNKNOWN"


def symbol_trace(symbols: Sequence[WaveformSymbol], chamber: ChamberConfig) -> str:
    trace = []
    for symbol in symbols:
        trace.append(f"{symbol.name}({symbol.frequency:.1f}Hz, phase={symbol.phase:.2f}, amp={symbol.amplitude:.2f}, cat={symbol.category})")
    return " + ".join(trace)


def _tokenize_text(text: str) -> List[str]:
    return re.findall(r"[A-Za-z0-9_]+|[^\s]", text)


def parse_expression(text: str) -> Sequence[WaveformSymbol]:
    tokens = _tokenize_text(text)
    return [get_symbol(token) for token in tokens]


def parse_static_program(lines: Sequence[str]) -> Sequence[WaveformSymbol]:
    symbols = []
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        tokens = _tokenize_text(stripped)
        for token in tokens:
            symbols.append(get_symbol(token))
    return symbols


def execute_program(lines: Sequence[str], chamber: ChamberConfig) -> str:
    symbols = parse_static_program(lines)
    interference = compute_interference(symbols, chamber)
    return infer_result(symbols, chamber)


def main(argv: Sequence[str]) -> int:
    parser = argparse.ArgumentParser(description="Run a QRP static waveform chamber computation.")
    parser.add_argument("--text", help="Text or expression to encode as static waveform symbols")
    parser.add_argument("--program", help="Path to a static-wave program file")
    parser.add_argument("--chamber", choices=["parabolic", "hyperbolic", "elliptic"], default="hyperbolic")
    args = parser.parse_args(argv)

    chamber = create_chamber_config(args.chamber)
    if args.program:
        with open(args.program, "r", encoding="utf-8") as fh:
            lines = fh.readlines()
        symbols = parse_static_program(lines)
        interference = compute_interference(symbols, chamber)
        result = infer_result(symbols, chamber)
        source = f"program {args.program}"
    elif args.text:
        symbols = parse_expression(args.text)
        interference = compute_interference(symbols, chamber)
        result = infer_result(symbols, chamber)
        source = f"text '{args.text}'"
    else:
        raise ValueError("Either --text or --program must be provided")

    print("QRP Static Wave Computation")
    print(f"Input: {source}")
    print(f"Chamber: {chamber.type}")
    print(f"Symbol trace: {symbol_trace(symbols, chamber)}")
    if args.program:
        print(f"Symbol count: {len(symbols)}")
    print(f"Interference score: {interference:.6f}")
    print(f"Inferred result: {result}")
    return 0


import sys

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
