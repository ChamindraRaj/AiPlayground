# Sprint Metrics Dashboard Generator

## Overview

The Sprint Metrics Dashboard Generator is a user-friendly desktop application designed for teams using Agile development methods. In simple terms, it's a tool that helps track a team's performance and progress through different development cycles (called "sprints").

Users can input key metrics—like the number of features delivered and team health—and the application will instantly generate a professional, visually appealing dashboard. This dashboard is created as both a webpage (HTML file) and an image (PNG file), making it easy to share, print, or include in presentations. The application also saves historical data, allowing teams to track their performance over time.

## Key Features

- **Simple Graphical Interface:** An intuitive and easy-to-navigate interface that doesn't require technical expertise.
- **Customizable Metrics:** Input performance and health metrics for up to four different technology areas.
- **History Tracking:** Save snapshots of your sprint data and easily load or delete them later.
- **Professional Dashboards:** Generate polished, self-contained HTML dashboards with modern styling.
- **Image Export:** Automatically create high-quality PNG images of the dashboards for easy sharing.
- **Configurable Sprints:** Easily configure the current increment and sprint numbers to match your project's timeline.

## Getting Started

Follow these steps to get the application running on your computer.

### Prerequisites

- **Python (version 3.7 or newer):** The application is built with Python. You can download it from [python.org](https://www.python.org/downloads/).
- **Google Chrome or Chromium Browser:** The application uses Chrome to automatically generate the PNG image of the dashboard.

### Installation

1.  The application uses a few external libraries. You can install the required package using pip:
    ```bash
    pip install selenium
    ```
2.  No other installation is needed. Just download the `sprint_metrics_python.py` file.

### Running the Application

To start the application, open your terminal or command prompt, navigate to the directory where you saved the file, and run the following command:

```bash
python sprint_metrics_python.py
```

The application window should now appear on your screen.

## How to Use the Application

1.  **Launch the Application:** Run the command above to open the main window.
2.  **Set the Sprint:** In the "Sprint Configuration" section, set the **Increment Number** and select the **Current Sprint** from the dropdown. You can also customize the **Sprint Range** text if needed.
3.  **Enter Metrics:** For each of the four categories (e.g., "Digital Technology," "Digital"), fill in the following fields:
    - **Features Delivered:** The number of features completed in the sprint.
    - **Total Features:** The total number of features planned.
    - **Health Score:** The team's health or happiness score (out of 4.00).
4.  **Save Your Data (Optional):** Click the **Save to History** button to store the current data. This is useful for tracking progress over time.
5.  **Generate the Dashboard:** Click the **Generate HTML & Image** button. A file dialog will open, allowing you to choose a location and name for your dashboard files. The application will save both an `.html` and a `.png` file.
6.  **View Past Data (Optional):** Click the **View History** button to open a new window where you can see all your saved entries. From there, you can choose to **Load** an old configuration back into the main form or **Delete** an entry.

## For Developers (Technical Overview)

### Architecture

The application is intentionally designed as a single-file script (`sprint_metrics_python.py`) for simplicity and portability.

- **Core Class:** The `SprintMetricsApp` class encapsulates all application logic, including the GUI, data handling, and file generation.
- **GUI Framework:** The user interface is built using **tkinter**, the standard GUI toolkit for Python.
- **Data Storage:** Sprint history is persisted in a JSON file named `sprint_history.json`. This file is automatically created and managed by the application.

### Dashboard Generation

- **HTML:** The `_generate_html_content` method dynamically creates a complete, self-contained HTML document. All CSS styles are embedded within the file, so it requires no external dependencies to be viewed correctly in a browser.
- **PNG Image:** To generate the image, the application uses the **Selenium** library. It programmatically opens the newly created HTML file in a headless instance of Google Chrome, captures the full height of the dashboard content, and saves it as a PNG file. This process runs in a separate thread to keep the UI responsive.

### Testing

The project includes a suite of unit tests written with Python's built-in `unittest` framework. The tests cover UI logic, data management, and HTML generation.

To run the tests, execute the script with the `--test` flag:

```bash
python sprint_metrics_python.py --test
```

## File Descriptions

- **`sprint_metrics_python.py`**: The main application script. It contains all the Python code for the GUI, business logic, and unit tests.
- **`sprint_history.json`**: This file is automatically created in the same directory to store historical sprint data in JSON format.
- **`sprint-dashboard-*.html`**: These are the generated HTML dashboard files, named based on the increment and sprint number.
- **`sprint-dashboard-*.png`**: These are the generated PNG image files, which are screenshots of the corresponding HTML dashboards.
