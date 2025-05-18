# Assignment 10: Nash Welfare Optimization for Budget Allocation

This assignment focuses on optimizing Nash welfare for budget allocation problems.

## Contents

- **Assignment_10.py**: Implementation of the Nash welfare optimization algorithm for budget allocation

## Key Concepts

- Nash welfare optimization
- Budget allocation problems
- Convex optimization using CVXPY
- Fair division of resources

## Implementation Details

The main algorithm in this assignment implements a method to fairly allocate budgets across different subjects based on citizen preferences, maximizing the Nash social welfare (product of utilities). The implementation uses the CVXPY library to solve the convex optimization problem.

## Usage

```python
# Example usage of the Nash budget algorithm
from Assignment_10 import Nash_budget

# Define parameters
total_budget = 1000  # Total budget to allocate
subjects = ["Education", "Healthcare", "Infrastructure", "Defense"]
preferences = [
    ["Education", "Healthcare"],           # Citizen 0 preferences
    ["Healthcare", "Infrastructure"],      # Citizen 1 preferences
    ["Infrastructure", "Defense"],         # Citizen 2 preferences
    ["Defense", "Education"]               # Citizen 3 preferences
]

# Calculate optimal Nash welfare allocations
Nash_budget(total_budget, subjects, preferences)
```

## Dependencies

- CVXPY: For solving convex optimization problems
- NumPy: For numerical operations