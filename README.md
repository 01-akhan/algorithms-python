# Algorithms in Python — Starter

A small educational repo with classic algorithms and data structures in Python.
Use this to build your ELTE CS portfolio project.

## What's inside
- `src/searching.py` — linear & binary search
- `src/sorting.py` — bubble, insertion, merge, quick sort
- `src/structures.py` — Stack, Queue
- `src/graphs.py` — BFS, DFS, Dijkstra
- `tests/` — basic pytest unit tests
- `examples/run_examples.py` — simple benchmark runner for sorts

## Quickstart
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements-dev.txt
pytest -q
python examples/run_examples.py
```

## Complexity (Big-O)
| Algorithm              | Time Avg      | Time Worst | Space |
|------------------------|---------------|------------|-------|
| Linear Search          | O(n)          | O(n)       | O(1)  |
| Binary Search          | O(log n)      | O(log n)   | O(1)  |
| Bubble Sort            | O(n^2)        | O(n^2)     | O(1)  |
| Insertion Sort         | O(n^2)        | O(n^2)     | O(1)  |
| Merge Sort             | O(n log n)    | O(n log n) | O(n)  |
| Quick Sort             | O(n log n)    | O(n^2)     | O(log n) avg |
| BFS/DFS                | O(V + E)      | O(V + E)   | O(V)  |
| Dijkstra (bin heap)    | O((V+E)logV)  | —          | O(V)  |

## What to add next
- Docstrings & explanations in README
- Heap sort, LinkedList, more tests
- Benchmarks chart and screenshots