# Bayan Performance Benchmark Suite

This directory contains benchmarks for measuring and comparing the performance of Bayan language against Python and Prolog.

## Structure

```
benchmarks/
├── README.md                      # This file
├── run_all_benchmarks.py         # Main benchmark runner
├── report_generator.py           # Results visualization
├── bayan/                        # Bayan benchmarks
│   ├── logic_benchmarks.bayan
│   ├── oop_benchmarks.bayan
│   ├── data_structures.bayan
│   └── hybrid_benchmarks.bayan
├── python/                       # Python equivalents
│   ├── logic_benchmarks.py
│   ├── oop_benchmarks.py
│   └── data_structures.py
├── prolog/                       # Prolog equivalents
│   ├── logic_benchmarks.pl
│   └── README.md
└── results/                      # Benchmark results
    └── .gitkeep
```

## Benchmark Categories

### 1. Logic Programming
- **Fact lookups**: Measure query performance on large fact bases
- **Recursive rules**: Fibonacci, factorial, tree traversal
- **Complex queries**: Multiple variables, backtracking
- **Unification**: Pattern matching performance

### 2. Object-Oriented Programming
- **Class instantiation**: Create 1K, 10K, 100K objects
- **Method calls**: Instance and class methods
- **Inheritance**: Multi-level inheritance
- **Attribute access**: Read and write performance

### 3. Data Structures
- **Lists**: Append, iteration, slicing, comprehensions
- **Dictionaries**: Insert, lookup, delete, iteration
- **Nested structures**: Complex data manipulation

### 4. Hybrid Features (Bayan-specific)
- **Entity system**: Creation, state management
- **Logic + OOP**: Mixed paradigm code
- **Semantic features**: Knowledge representation

## Running Benchmarks

### Run All Benchmarks
```bash
python run_all_benchmarks.py
```

### Run Specific Category
```bash
python run_all_benchmarks.py --category logic
python run_all_benchmarks.py --category oop
```

### Generate Report
```bash
python report_generator.py
```

This creates:
- `results/benchmark_results_YYYYMMDD.json` - Raw data
- `results/performance_report.html` - Interactive report
- `results/comparison_charts.png` - Visual comparison

## Interpreting Results

Results show:
- **Execution time**: min, max, mean, median (in seconds)
- **Memory usage**: Peak memory consumption
- **Relative performance**: Speedup/slowdown vs baseline
- **Bottleneck analysis**: Top 5 slowest operations

## Adding New Benchmarks

1. Create benchmark in `bayan/` directory
2. Create equivalent in `python/` (and optionally `prolog/`)
3. Add to benchmark registry in `run_all_benchmarks.py`
4. Document the benchmark purpose and expected behavior

## Performance Targets

Based on similar hybrid languages:

| Operation | Current | Target (6mo) | Target (1yr) |
|-----------|---------|--------------|--------------|
| Logic queries | Baseline | 2-3x faster | 5-10x faster |
| OOP operations | Baseline | 1.5-2x faster | 3-5x faster |
| Data structures | Baseline | 1.5-2x faster | 2-4x faster |

## Notes

- Benchmarks run with Python 3.12+
- Each benchmark runs 100 iterations by default
- Results averaged over 5 runs
- System specs included in report metadata

---

**Created**: 2025-11-25
**Last Updated**: 2025-11-25
