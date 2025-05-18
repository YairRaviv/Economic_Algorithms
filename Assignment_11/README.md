# Economic Algorithms - Assignment 11

This assignment focuses on budget allocation mechanisms in participatory budgeting scenarios.

## Overview

This assignment implements a budget computation algorithm for participatory budgeting that is:
- Strategy-proof
- Pareto efficient
- Individually rational

## Implementation

The `compute_budget` function implements a mechanism that:
1. Takes citizen votes on how to allocate a budget to various subjects/projects
2. Creates additional "phantom votes" with specific properties 
3. Uses the median of all votes (including phantom votes) to determine the final allocation

## Algorithm Details

The main steps of the algorithm:
1. Calculate parameter t = 1/n (where n is the number of citizens)
2. Create n-1 "phantom functions" with values based on t
3. Create additional votes based on these phantom functions
4. Combine the original citizen votes with the phantom votes
5. Calculate the median vote for each subject
6. Return the resulting allocation

## Mathematical Background

This approach guarantees:
- **Strategy-proofness**: No citizen can benefit by misrepresenting their preferences
- **Efficiency**: The mechanism produces Pareto-optimal allocations
- **Budget-balance**: The sum of allocations equals the total available budget

## Usage Example

```python
total_budget = 100
citizen_votes = [
    [30, 40, 30],  # Citizen 1's votes for projects A, B, C
    [20, 50, 30],  # Citizen 2's votes
    [10, 20, 70]   # Citizen 3's votes
]

allocation = compute_budget(total_budget, citizen_votes)
print(allocation)  # The final allocation for projects A, B, C
```

## References

This implementation is based on the concept of phantom voters for creating strategy-proof mechanisms in collective decision-making contexts, particularly in participatory budgeting scenarios.