# RecursionError in Python Factorial Function

This repository demonstrates a common error in Python programming: the `RecursionError`. This error occurs when a recursive function calls itself infinitely, exceeding the maximum recursion depth allowed by Python.

The `bug.py` file contains a factorial function that works correctly for non-negative integers. However, when a negative integer is passed as an argument, it leads to infinite recursion and a `RecursionError`. The `bugSolution.py` file shows how to modify the function to avoid this error by explicitly checking for negative inputs.

## How to Reproduce

1.  Clone this repository.
2.  Run `bug.py` with a negative input, such as `python bug.py -1`. You'll observe a `RecursionError`.
3.  Run `bugSolution.py`. This file demonstrates a corrected function that handles negative inputs gracefully.