# MSCS532_Assignment1

## Assignment 1 – Getting Started

This repository contains the implementation of the **Insertion Sort algorithm** modified to sort an array in **monotonically decreasing order**, as required for MSCS532 Assignment 1.

The algorithm follows the structure presented in *Introduction to Algorithms (4th ed.)* by Cormen, Leiserson, Rivest, and Stein, with the comparison logic adjusted to produce decreasing order instead of increasing order.

## Environment

The project was developed using:

* **Python 3.13.9**
* **Visual Studio Code**
* Git and GitHub for version control

Python version was verified using:

```bash
python3 --version
```

## Algorithm Overview

Insertion Sort builds a sorted portion of the array incrementally. For each element (key), the algorithm compares it with elements in the sorted subarray to its left and shifts smaller elements to the right. This ensures the final array is sorted in strictly decreasing order.

### Time Complexity

* Worst Case: O(n²)
* Best Case: O(n)
* Space Complexity: O(1) (in-place sorting)

## Repository Requirements

This repository satisfies the assignment requirements:

* Implementation of Insertion Sort in monotonically decreasing order
* Public repository named `MSCS532_Assignment1`
* Minimum of three commits demonstrating development progress

## How to Run

1. Clone the repository:

```bash
git clone [<MSCS532_Assignment1>](https://github.com/HARIPRASAD-001/MSCS532_Assignment1.git)
```

2. Navigate to the project directory:

```bash
cd MSCS532_Assignment1
```

3. Run the Python script:

```bash
python3 insertion_sort.py
```

---
