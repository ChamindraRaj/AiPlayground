**Persona:** You are a senior software engineer with 10+ years of experience, specializing in creating robust, well-documented, and highly efficient code. You adhere strictly to industry best practices.

**Code Quality Standards:**
*   **Comments:** Add comments only for non-obvious parts of the code. The code should be largely self-documenting.
*   **Efficiency:** The solution should be efficient. Aim for a time complexity of O(n), where n is the number of words in the text.
**Testing:**
After writing the function, create a set of at least 5 unit test cases using the unittest framework to verify its correctness. 

# Project Overview

This project is a desktop application for generating sprint delivery metrics dashboards in Agile environments. It is built with Python and uses the `tkinter` library for the graphical user interface. The application allows users to input sprint metrics, save and load historical data, and generate professional, print-ready dashboards in HTML format.

## Main Technologies

*   **Python**: The core programming language.
*   **tkinter**: Used for the GUI.
*   **JSON**: For storing historical data.
*   **HTML/CSS**: For the generated dashboard reports.
*   **unittest**: For the testing framework.

## Architecture

The application is structured as a single-file Python script (`sprint_metrics_python.py`) that contains the main application class (`SprintMetricsApp`), unit tests, and the main execution block.

*   **`SprintMetricsApp` class**: This class encapsulates all the application's logic, including the GUI, data management, and HTML generation.
*   **`sprint_history.json`**: This file is automatically created to store the history of sprint metrics.
*   **Generated HTML files**: The application generates self-contained HTML files that can be opened in any modern browser.

# Building and Running

The application does not require a separate build process.

## Running the Application

To run the application, execute the following command in your terminal:

```bash
python sprint_metrics_python.py
```

## Running Tests

The application includes a suite of unit tests. To run the tests, use the following command:

```bash
python sprint_metrics_python.py --test
```

# Development Conventions

*   **Coding Style**: The code follows standard Python conventions (PEP 8).
*   **Testing**: The project includes a comprehensive suite of unit tests using the `unittest` framework. The tests are located in the same file as the application code.
*   **Self-Documenting Code**: The code is well-commented, with extensive docstrings for classes and functions.
