# Assignment 2: Fair Division Algorithms and Leximin Comparison

This assignment focuses on fair division algorithms and leximin comparison techniques, exploring how resources can be allocated fairly among different agents.

## Contents

- **BetterLeximin.py**: Implementation of an improved leximin comparison algorithm
- **findAlmostEnvyFree.py**: Algorithm to find almost envy-free allocations

## Key Concepts

- Leximin ordering for comparing allocations
- Envy-free and almost envy-free allocations
- Fair division principles and algorithms

## Implementation Details

The main algorithms in this assignment implement:
- Comparison of utility vectors using leximin ordering
- Finding allocations that minimize envy between agents

## Usage

```python
# Example usage of the BetterLeximin algorithm
from BetterLeximin import leximin_better

vector1 = [3, 1, 2]
vector2 = [2, 2, 2]
result = leximin_better(vector1, vector2)
print(result)  # Will determine which vector is better under leximin ordering
```