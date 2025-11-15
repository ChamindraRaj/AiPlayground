# Project Overview

This project is a Python script that generates a static HTML dashboard from data in an Excel file. The dashboard displays sprint metrics, including features delivered and health metrics, for different technology categories. The styling of the HTML is inlined in the Python script.

# Building and Running

1.  **Set up the environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the script:**
    ```bash
    python sprint_dashboard.py
    ```
    This will generate `dashboard_data.xlsx` and `sprint_dashboard.html`.

# Development Conventions

*   The project uses the `pandas` library for data manipulation and `openpyxl` for Excel file operations.
*   The script includes a `DashboardGenerator` class to encapsulate the logic for loading data and generating the HTML.
*   Unit tests are included in the main script and are run using the `unittest` module.
*   The script can be run as a standalone program.
