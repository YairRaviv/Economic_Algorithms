# Economic Algorithms - Assignment 12

This assignment focuses on house allocation problems and implements a graph-based approach to analyze agent preferences.

## Overview

This assignment explores the house allocation problem, where n agents must be assigned to n houses given their valuations for each house. It implements a directed graph representation of agent preferences to visualize and analyze potential allocations.

## Implementation

The `build_graph` function builds a directed graph that represents agent preferences:
- Nodes represent agents
- Edges connect agents to their most-valued houses
- Multiple edges can emerge from an agent if they have multiple top choices

## Graph Structure

In the graph:
- Each node i represents agent i
- An edge from node i to node j means that house j is among agent i's most preferred houses
- The graph can be analyzed to find cycles, which represent potential exchange opportunities

## Visualization

The implementation includes code to visualize the preference graph using matplotlib and networkx:
- Nodes represent agents
- Directed edges show preferences
- The visualization helps identify potential allocations or cycles

## Mathematical Background

This approach relates to several economic concepts:
1. **Top Trading Cycle**: Finding cycles in the graph can identify groups of agents who can trade to improve their allocation
2. **Stability**: Analyzing the graph can help determine if an allocation is stable
3. **Pareto Efficiency**: The graph can be used to find Pareto improvements

## Usage Example

```python
valuations = [
    [25, 50, 30, 50, 49],  # Agent 0's valuations for houses 0-4
    [60, 20, 40, 70, 43],  # Agent 1's valuations
    [30, 30, 40, 30, 30],  # Agent 2's valuations
    [13, 90, 90, 30, 30],  # Agent 3's valuations
    [30, 30, 30, 20, 20]   # Agent 4's valuations
]

G = build_graph(valuations)  # Create preference graph
# Analyze graph to find optimal allocations
```

## Applications

This approach can be used for:
- House allocation problems
- Course assignment in universities
- Job matching markets
- Any resource allocation scenario with indivisible goods

## Required Libraries

- NetworkX: For graph operations
- Matplotlib: For visualization
- NumPy: For numerical operations