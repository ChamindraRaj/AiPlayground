# Developer Guide

This guide provides essential information for developers working on the Sprint Metrics Dashboard project.

## Your AI Assistant

Your assistant is a senior software engineer persona with over 10 years of experience. Its role is to help you build, modify, and maintain this project by creating robust, well-documented, and efficient code that adheres to industry best practices.

## Project Overview

This project is a desktop application for generating sprint delivery metrics dashboards in Agile environments. It is built with Python and uses the `tkinter` library for the graphical user interface.

### Core Technologies

*   **Python**: The core programming language.
*   **tkinter**: Used for the GUI.
*   **JSON**: For storing historical data.
*   **HTML/CSS**: For the generated dashboard reports.
*   **unittest**: For the testing framework.

### How it Works

1.  **GUI**: The application uses Python's `tkinter` library to provide a graphical user interface for data entry.
2.  **Data Input**: Users input sprint metrics (e.g., sprint name, dates, story points planned vs. completed).
3.  **Data Storage**: The application saves the history of sprint metrics to a `sprint_history.json` file.
4.  **Dashboard Generation**: It generates a self-contained HTML file that serves as a professional, print-ready dashboard.

## Getting Started

### Running the Application

To run the application, execute the following command in your terminal:

```bash
python sprint_metrics_python.py
```

### Running Tests

The project includes a suite of unit tests to verify its correctness and prevent regressions. To run the tests, use the following command:

```bash
python sprint_metrics_python.py --test
```

## Writing Tests

Tests are written using Python's built-in `unittest` framework and are located in the `sprint_metrics_python.py` file.

### Procedure

1.  **Locate Tests**: Open `sprint_metrics_python.py` and find the test classes, which inherit from `unittest.TestCase`.
2.  **Add a Test Method**: Add a new method to an existing test class or create a new class for a new group of tests. Test method names must begin with `test_`.
3.  **Use Assertions**: Use `self.assert...` methods to check for expected outcomes.

### Example

Here is an example of a test case for a hypothetical `calculate_velocity()` function:

```python
import unittest

# Example function to be tested
def calculate_velocity(story_points, num_sprints):
    if num_sprints == 0:
        return 0
    return sum(story_points) / num_sprints

# Test class
class TestVelocityCalculations(unittest.TestCase):
    def test_calculate_velocity_basic(self):
        """Test basic velocity calculation."""
        points = [10, 12, 8]
        self.assertEqual(calculate_velocity(points, 3), 10)

    def test_calculate_velocity_with_no_sprints(self):
        """Test velocity calculation with zero sprints."""
        self.assertEqual(calculate_velocity([], 0), 0)

    def test_calculate_velocity_with_floats(self):
        """Test that velocity can handle float results."""
        points = [10, 11]
        self.assertAlmostEqual(calculate_velocity(points, 2), 10.5)
```

### Common Assertions

*   `self.assertEqual(a, b)`: Checks for equality between `a` and `b`.
*   `self.assertTrue(x)`: Checks if `x` is `True`.
*   `self.assertFalse(x)`: Checks if `x` is `False`.
*   `self.assertRaises(Exception, function, *args)`: Checks if a specific `Exception` is raised.
