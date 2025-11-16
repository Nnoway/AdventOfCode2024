# Advent of Code 2024

Solutions for [Advent of Code 2024 challenge 2](https://adventofcode.com/2024/day/2) challenges.

## Project Description

This repository contains Python solutions for the second Advent of Code 2024 challenges. The current implementation analyzes sequences of numbers to determine if they are "safe" based on specific criteria.

## Usage

### Part 1: Basic Safety Analysis

```bash
python3 script.py [filename]
```

- If no filename provided, the script uses `ex0.txt`
- Input files should be placed in the `src/` directory
- Only need to specify filename not the full path

### Part 2: Safety Analysis with Problem Dampener

```bash
python3 d2/script_etoile.py [filename]
```

This version implements the "Problem Dampener" which tolerates a single bad level in what would otherwise be a safe report.

## Project Structure

```
.
├── d2/
|   ├── src/                  # Input data files
|   |   ├── ex0.txt           # Example dataset (default)
|   |   ├── ex1.txt           # Challenge dataset
|   │   └── ex2.txt           # Additional dataset
│   ├── script_etoile.py      # Part 2: With Problem Dampener
│   └── script.py             # Part 1: Basic safety analysis
└── README.md                 # This file
```

## How It Works

The script analyzes each line of numbers (report) and classifies it as **safe** or **unsafe** based on these rules:

### Part 1: Safety Criteria

A report is considered **safe** if:
1. The levels are either **all increasing** or **all decreasing**.
2. Any two adjacent levels differ by **at least one** and **at most three**

A report is considered **unsafe** if:
- Values remain stable (consecutive identical values)
- The difference between adjacent values is greater than 3
- The direction changes (increases then decreases, or vice versa)

### Part 2: Problem Dampener

The Problem Dampener is a safety system that **tolerates a single bad level** in what would otherwise be a safe report.

The dampened safety analysis:
1. First checks if the report is already safe (without removing any level)
2. If not, tries removing each level one at a time
3. If removing any single level makes the report safe, it counts as safe
4. Only if no single removal works is the report considered unsafe

## Output

### Part 1 Output

```
Number of safe reports : X
Number of unsafe reports : Y
Total number of reports : Z
Number of empty reports : 0
Number of reports with only one element : 0
```

### Part 2 Output (with Problem Dampener)

```
Number of safe reports (with dampener): X
Number of unsafe reports: Y
Total number of reports: Z
Number of empty reports : 0
Number of reports with only one element : 0
```

The dampener typically increases the number of safe reports by catching cases where removing one problematic level fixes the sequence.

## Input Format

Each line in the input file should contain space-separated integers:

## Error Handling

The script handles the following error cases:

- **File not found**: If the file doesn't exist
- **Empty file**: If the file contains no valid data
- **Empty lines**: Automatically skipped 
- **Single-element lines**: Counted separately

## License

This project is part of Advent of Code 2024 challenge solutions.

## Author

Nnoway

---

**Advent of Code** is an annual set of Christmas-themed programming challenges that can be solved in any programming language.
