"""Run a smoke test of the calculator and NumPy installation."""

import numpy as np

from calculator import add_numbers, divide


def main() -> None:
    """Display sample calculations and handle division by zero."""
    print(f"NumPy version: {np.__version__}")
    values = np.array([1, 2, 3])
    print(f"NumPy array: {values}; sum: {np.sum(values)}")
    print(f"2 + 3 = {add_numbers(2, 3)}")
    print(f"10 / 2 = {divide(10, 2)}")
    try:
        divide(10, 0)
    except ValueError as error:
        print(f"Handled error: {error}")


if __name__ == "__main__":
    main()
