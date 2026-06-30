#!/usr/bin/env python3
"""Bulk loader for waveform symbol sets into the CLI custom database."""

import json
import os
import glob
from typing import Dict
from waveform_static_db import WaveformSymbol


def load_symbol_from_dict(data: Dict[str, object]) -> WaveformSymbol:
    """Load a symbol from a dictionary."""
    return WaveformSymbol(
        name=str(data["name"]),
        frequency=float(data["frequency"]),
        phase=float(data["phase"]),
        amplitude=float(data["amplitude"]),
        harmonic=int(data["harmonic"]),
        envelope=float(data["envelope"]),
        category=str(data["category"]),
        opcode=data.get("opcode"),
        description=data.get("description"),
    )


def load_symbol_file(filepath: str) -> Dict[str, WaveformSymbol]:
    """Load symbols from a JSON file."""
    symbols = {}
    with open(filepath, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    if isinstance(data, list):
        for entry in data:
            symbol = load_symbol_from_dict(entry)
            symbols[symbol.name.upper()] = symbol
    return symbols


def symbol_to_dict(symbol: WaveformSymbol) -> Dict[str, object]:
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


def load_all_symbol_files(pattern: str = "*.json", exclude: str = "waveform_static_custom.json") -> Dict[str, WaveformSymbol]:
    """Load all symbol files matching pattern."""
    all_symbols: Dict[str, WaveformSymbol] = {}
    for filepath in sorted(glob.glob(pattern)):
        if filepath == exclude:
            continue
        if not os.path.exists(filepath):
            continue
        print(f"Loading {filepath}...", end=" ")
        symbols = load_symbol_file(filepath)
        all_symbols.update(symbols)
        print(f"({len(symbols)} symbols)")
    return all_symbols


def merge_into_custom(symbols: Dict[str, WaveformSymbol], custom_path: str = "waveform_static_custom.json") -> None:
    """Merge symbols into the custom database, avoiding duplicates."""
    existing = {}
    if os.path.exists(custom_path):
        with open(custom_path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        for entry in data:
            symbol = load_symbol_from_dict(entry)
            existing[symbol.name.upper()] = symbol
    
    before = len(existing)
    existing.update(symbols)
    after = len(existing)
    added = after - before
    
    data = [symbol_to_dict(s) for s in existing.values()]
    with open(custom_path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)
    
    print(f"\nMerged {added} new symbols.")
    print(f"Custom database now contains {after} symbols total.")
    print(f"Saved to {custom_path}")


def main() -> int:
    """Load all generated symbol files and merge into custom database."""
    print("Loading generated waveform symbol files...")
    symbols = load_all_symbol_files(pattern="*.json", exclude="waveform_static_custom.json")
    
    if not symbols:
        print("No symbol files found.")
        return 1
    
    print(f"\nTotal symbols loaded: {len(symbols)}")
    categories = {}
    for symbol in symbols.values():
        categories[symbol.category] = categories.get(symbol.category, 0) + 1
    
    print("By category:")
    for category, count in sorted(categories.items()):
        print(f"  {category}: {count}")
    
    merge_into_custom(symbols)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
