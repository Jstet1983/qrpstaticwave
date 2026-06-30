# QRP Static Wave Syntax

## Overview

QRP Static Wave programs are written as line-oriented statements. Each statement is a sequence of static waveform symbols or machine-code opcodes.

## Statement types

- `SETCHAMBER <type>`
  - Selects the virtual chamber geometry.
  - Supported values: `hyperbolic`, `parabolic`, `elliptic`.

- `LOAD <symbol>`
  - Loads a waveform symbol into the current register context.

- `STORE <symbol>`
  - Stores the computed waveform state into a named symbol.

- `ADD`, `SUB`, `MUL`, `DIV`
  - Perform arithmetic-like waveform combination operations.
  - These opcodes add symbolic waveform contributions to the chamber.

- `CMP`
  - Compare waveform resonance patterns.

- `EMIT`
  - Emit the chamber output and finalize the interference result.

- `NOP`
  - No-operation; preserves the current waveform state.

## Example

```
# Set chamber geometry
SETCHAMBER hyperbolic

# Build a symbolic waveform expression
LOAD A
LOAD D
ADD
STORE RESULT

# Combine scientific meaning
LOAD PHYS
LOAD CHEM
AND
STORE CONTEXT

# Emit the final interference result
EMIT
```

## Static waveform program rules

- Comments begin with `#` and are ignored.
- Identifiers are case-insensitive.
- Symbols are either single characters or named abstractions such as `PI`, `H2O`, `ALG`, `PHYS`, `CODE`.
- Instructions are encoded as special waveform symbols with `opcode` metadata.
- The computation is driven by the interference score computed inside the virtual chamber.

## Symbol categories

- `letter`, `digit`, `operator`, `logic`, `constant`, `molecule`, `element`, `knowledge`, `instruction`

## Chamber geometry

- `hyperbolic` gives stronger interference gain for resonance seekers.
- `parabolic` models a neutral chamber with less curvature.
- `elliptic` is more damped and conservative.
