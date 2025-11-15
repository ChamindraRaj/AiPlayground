# Sprint Metrics Dashboard Generator

This project contains a Python script that generates an HTML-based sprint metrics dashboard from an Excel file.

## Prerequisites

- Python 3.6+

## Setup and Execution

1.  **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the script:**

    ```bash
    python sprint_dashboard.py
    ```

## Output

Running the script will produce two files:

1.  `dashboard_data.xlsx`: A sample Excel file with data in the required format.
2.  `sprint_dashboard.html`: The generated HTML dashboard.

You can open `sprint_dashboard.html` in your web browser to view the dashboard.

The script will also run a series of unit tests to verify its functionality.
