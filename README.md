# Advent of Code 2024

Solutions for [Advent of Code 2024 challenge 2](https://adventofcode.com/2024/day/2) challenges.

## 📋 Project Description

This repository contains Python solutions for the second Advent of Code 2024 challenges. The current implementation analyzes sequences of numbers to determine if they are "safe" based on specific criteria.

## 🚀 Usage

### Basic Usage

```bash
python3 script.py [filename]
```

- If no filename provided, the script uses `ex0.txt`
- Input files should be placed in the `src/` directory
- Only need to specify filename not the full path

## 📁 Project Structure

```
.
├── script.py         # Main Python script
├── src/              # Input data files
│   ├── ex0.txt       # Example dataset (default)
│   ├── ex1.txt       # Challenge dataset
│   └── ex2.txt       # Additional dataset
└── README.md         # This file
```

## 🔍 How It Works

The script analyzes each line of numbers (report) and classifies it as **safe** or **unsafe** based on these rules:

### Safety Criteria

A report is considered **safe** if:
1. The levels are either **all increasing** or **all decreasing**.
2. Any two adjacent levels differ by **at least one** and **at most three**

A report is considered **unsafe** if:
- Values remain stable (consecutive identical values)
- The difference between adjacent values is greater than 3
- The direction changes (increases then decreases, or vice versa)

## 📊 Output

The script provides detailed statistics:

```
Number of safe reports : X
Number of unsafe reports : Y
Total number of reports : Z
Number of empty reports : 0
Number of reports with only one element : 0
```

## 🛠️ Input Format

Each line in the input file should contain space-separated integers:

## ⚠️ Error Handling

The script handles the following error cases:

- **File not found**: If the file doesn't exist
- **Empty file**: If the file contains no valid data
- **Empty lines**: Automatically skipped 
- **Single-element lines**: Counted separately

## 📝 License

This project is part of Advent of Code 2024 challenge solutions.

## 👤 Author

Nnoway

---

**Advent of Code** is an annual set of Christmas-themed programming challenges that can be solved in any programming language.
