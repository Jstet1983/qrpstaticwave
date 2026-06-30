#!/usr/bin/env python3
"""Interactive CLI for querying and extending the QRP static waveform database."""

import json
import os
import shlex
from cmd import Cmd
from typing import Dict, List, Optional

from waveform_static_db import (
    STATIC_WAVE_DB,
    WaveformSymbol,
    create_ascii_symbol,
    create_waveform_symbol,
    get_symbol,
    symbol_numeric_value,
)
from waveform_static_language import compute_interference, create_chamber_config, infer_result, parse_expression, symbol_trace

CUSTOM_SYMBOLS_FILE = os.path.join(os.path.dirname(__file__), "waveform_static_custom.json")


def symbol_to_dict(symbol: WaveformSymbol) -> Dict[str, object]:
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


def load_custom_symbols(path: str) -> Dict[str, WaveformSymbol]:
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    custom = {}
    for entry in data:
        symbol = WaveformSymbol(
            name=entry["name"],
            frequency=float(entry["frequency"]),
            phase=float(entry["phase"]),
            amplitude=float(entry["amplitude"]),
            harmonic=int(entry["harmonic"]),
            envelope=float(entry["envelope"]),
            category=entry["category"],
            opcode=entry.get("opcode"),
            description=entry.get("description"),
        )
        custom[symbol.name.upper()] = symbol
    return custom


def save_custom_symbols(path: str, symbols: Dict[str, WaveformSymbol]) -> None:
    data = [symbol_to_dict(symbol) for symbol in symbols.values()]
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)


class WaveformCLI(Cmd):
    intro = "Welcome to QRP Static Wave CLI. Type help or ? to list commands."
    prompt = "waveform> "

    def __init__(self):
        super().__init__()
        self.custom_symbols: Dict[str, WaveformSymbol] = load_custom_symbols(CUSTOM_SYMBOLS_FILE)
        self.db = dict(STATIC_WAVE_DB)
        self.db.update(self.custom_symbols)

    def preloop(self) -> None:
        print(f"Loaded {len(self.db)} symbols ({len(self.custom_symbols)} custom).")

    def do_query(self, arg: str) -> None:
        "Query a waveform symbol by name or character: query A"
        name = arg.strip()
        if not name:
            print("Usage: query SYMBOL")
            return
        symbol = self.db.get(name.upper()) or get_symbol(name)
        self._print_symbol(symbol)

    def complete_query(self, text: str, line: str, begidx: int, endidx: int) -> List[str]:
        return [key for key in self.db.keys() if key.startswith(text.upper())][:50]

    def do_show(self, arg: str) -> None:
        "Show tokenization and waveform trace for text: show if x == 10"
        if not arg.strip():
            print("Usage: show TEXT")
            return
        symbols = parse_expression(arg)
        print(symbol_trace(symbols))

    def do_run(self, arg: str) -> None:
        "Run interference computation on text: run DATA AND PI"
        if not arg.strip():
            print("Usage: run TEXT")
            return
        symbols = parse_expression(arg)
        chamber = create_chamber_config("hyperbolic")
        interference = compute_interference(symbols, chamber=chamber)
        result = infer_result(symbols, chamber)
        print(f"Symbol count: {len(symbols)}")
        print(f"Interference score: {interference:.6f}")
        print(f"Result: {result}")

    def do_list(self, arg: str) -> None:
        "List loaded symbols; optionally filter by category: list operator"
        category = arg.strip().lower()
        symbols = [symbol for symbol in self.db.values() if not category or symbol.category.lower() == category]
        symbols.sort(key=lambda s: s.name)
        for symbol in symbols[:200]:
            print(f"{symbol.name} ({symbol.category})")
        if len(symbols) > 200:
            print(f"... and {len(symbols) - 200} more")

    def complete_list(self, text: str, line: str, begidx: int, endidx: int) -> List[str]:
        categories = sorted(set(symbol.category for symbol in self.db.values()))
        return [c for c in categories if c.startswith(text.lower())]

    def do_add(self, arg: str) -> None:
        "Add a new waveform symbol: add NAME CATEGORY [DESCRIPTION]"
        parts = shlex.split(arg)
        if len(parts) < 2:
            print("Usage: add NAME CATEGORY [DESCRIPTION]")
            return
        name = parts[0]
        category = parts[1]
        description = " ".join(parts[2:]) if len(parts) > 2 else f"Custom symbol {name}"
        if len(name) == 1 and category.lower() in {"letter", "digit", "operator", "whitespace", "ascii"}:
            symbol = create_ascii_symbol(name)
            symbol = WaveformSymbol(
                name=symbol.name,
                frequency=symbol.frequency,
                phase=symbol.phase,
                amplitude=symbol.amplitude,
                harmonic=symbol.harmonic,
                envelope=symbol.envelope,
                category=category,
                opcode=None,
                description=description,
            )
        else:
            symbol = create_waveform_symbol(name, category, description=description)
        self.db[symbol.name.upper()] = symbol
        self.custom_symbols[symbol.name.upper()] = symbol
        print(f"Added {symbol.name} ({symbol.category})")

    def do_save(self, arg: str) -> None:
        "Save custom symbol definitions to disk: save [PATH]"
        path = arg.strip() or CUSTOM_SYMBOLS_FILE
        save_custom_symbols(path, self.custom_symbols)
        print(f"Saved {len(self.custom_symbols)} custom symbol(s) to {path}")

    def do_load(self, arg: str) -> None:
        "Load custom symbol definitions from a JSON file: load PATH"
        path = arg.strip() or CUSTOM_SYMBOLS_FILE
        loaded = load_custom_symbols(path)
        self.custom_symbols.update(loaded)
        self.db.update(loaded)
        print(f"Loaded {len(loaded)} symbol(s) from {path}")

    def do_stats(self, arg: str) -> None:
        "Show database statistics."
        categories = {}
        for symbol in self.db.values():
            categories[symbol.category] = categories.get(symbol.category, 0) + 1
        print(f"Total symbols: {len(self.db)}")
        for category, count in sorted(categories.items()):
            print(f"  {category}: {count}")

    def do_exit(self, arg: str) -> bool:
        "Exit the CLI."
        return True

    def do_quit(self, arg: str) -> bool:
        "Exit the CLI."
        return True

    def do_EOF(self, arg: str) -> bool:
        print()
        return True

    def emptyline(self) -> None:
        pass

    def _print_symbol(self, symbol: WaveformSymbol) -> None:
        print(f"Name: {symbol.name}")
        print(f"Category: {symbol.category}")
        if symbol.opcode:
            print(f"Opcode: {symbol.opcode}")
        print(f"Frequency: {symbol.frequency}")
        print(f"Phase: {symbol.phase}")
        print(f"Amplitude: {symbol.amplitude}")
        print(f"Harmonic: {symbol.harmonic}")
        print(f"Envelope: {symbol.envelope}")
        print(f"Description: {symbol.description}")
        print(f"Numeric value: {symbol_numeric_value(symbol):.4f}")


def main() -> int:
    cli = WaveformCLI()
    try:
        cli.cmdloop()
    except KeyboardInterrupt:
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
