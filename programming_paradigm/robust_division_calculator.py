#!/usr/bin/python3
"""
robust_division_calculator.py

Defines a safe_divide function that performs division with
basic error handling for:
- non-numeric inputs
- division by zero
"""


def safe_divide(numerator, denominator):
    """
    Safely divide two values given as strings or numbers.

    - Tries to convert both arguments to float.
    - Handles non-numeric input (ValueError).
    - Handles division by zero (ZeroDivisionError).

    Args:
        numerator: value representing the numerator
        denominator: value representing the denominator

    Returns:
        str: a message with either the result or an error description.
    """
    # First: convert inputs to float
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    # Second: perform the division
    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    # Successful division
    return f"The result of the division is {result}"
