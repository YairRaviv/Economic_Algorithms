# Assignment 5: Envy-Free Allocations

This assignment focuses on envy-free allocations and fair division concepts.

## Contents

- **Assignment_5.py**: Implementation of the EF1 (Envy-Free up to 1 item) algorithm

## Key Concepts

- Envy-Free divisions
- EF1 (Envy-Free up to 1 item) property
- Fair allocation of indivisible goods

## Implementation Details

The main algorithms in this assignment implement methods to check if an allocation satisfies the EF1 property, which means that each agent prefers their bundle to any other agent's bundle after potentially removing up to one item from the other bundle.

## Usage

```python
# Example usage of the EF1 checking algorithm
from Assignment_5 import is_EF1

# Define agents and bundles
agents = [...]
bundles = [...]

# Check if allocation is EF1
result = is_EF1(agents, bundles)
print(f'The allocation is{"" if result else " not"} EF1.')
```