# Assignment 7: Resource Allocation Algorithms

This assignment focuses on resource allocation algorithms and threshold-based payment systems.

## Contents

- **Assignment_7.py**: Implementation of choice rules and payment calculation algorithms

## Key Concepts

- Choice rules for resource allocation
- Threshold-based payment mechanisms
- Algorithmic mechanism design

## Implementation Details

The main algorithms in this assignment implement:
- Different choice rule functions (top 3 values, top 3 values ≥ 10)
- Payment calculation based on threshold values
- Testing through doctest for verification

## Usage

```python
# Example usage of the payment calculation
from Assignment_7 import payments, choise_1, choise_2

# Define values
values = [15, 14, 13, 12]

# Calculate payments using choice rule 1 (top 3 values)
payments_rule1 = payments(values, choise_1)
print(f'Payments using choice rule 1: {payments_rule1}')

# Calculate payments using choice rule 2 (top 3 values ≥ 10)
payments_rule2 = payments(values, choise_2)
print(f'Payments using choice rule 2: {payments_rule2}')
```