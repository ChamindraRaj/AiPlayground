"""
Sprint Metrics Dashboard Generator - Desktop Application
=========================================================

A complete GUI application for generating sprint metrics dashboards in an Agile environment.
Supports multiple increments, tracks history, and generates professional HTML reports and PNG images.

Author: Sprint Metrics Team
Version: 2.0.0
Python: 3.7+

Requirements:
    - tkinter (comes with Python by default)
    - selenium (for HTML to PNG conversion)
    - Chrome/Chromium browser
    
Installation:
    pip install selenium
    
Usage:
    python sprint_metrics_app.py
    
Features:
    - Configure increment numbers and sprint ranges
    - Enter metrics for 4 categories
    - Save and load historical data
    - Generate professional HTML dashboards
    - Generate PNG images from HTML
    - Persistent storage using JSON
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os
from datetime import datetime
from pathlib import Path
import unittest
from unittest.mock import Mock, patch, MagicMock
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class SprintMetricsApp:
    """
    Main application class for Sprint Metrics Dashboard Generator.
    
    This class handles the GUI, data management, and HTML generation for
    sprint metrics tracking across agile increments.
    
    Attributes:
        root: The main tkinter window
        history_file: Path to JSON file storing historical data
        history: List of previous metric records
        increment: Current increment number (e.g., 17)
        current_sprint: Current sprint identifier (e.g., "17.1")
        sprint_range: Display range for sprints (e.g., "17.1 - 17.1")
        metrics: Dictionary storing all metric values for four categories
    """
    
    def __init__(self, root):
        """
        Initialize the Sprint Metrics Application.
        
        Args:
            root: tkinter.Tk() root window instance
        """
        self.root = root
        self.root.title("Sprint Metrics Dashboard Generator")
        self.root.geometry("1000x800")
        self.root.configure(bg="#f8f9fa")
        
        # Initialize data storage path - stores history in same directory as script
        self.history_file = Path("sprint_history.json")
        self.history = self.load_history()
        
        # Initialize default configuration values
        self.increment = tk.IntVar(value=17)  # Current increment number
        self.current_sprint = tk.StringVar(value="17.1")  # Active sprint
        self.sprint_range = tk.StringVar(value="17.1 - 17.1")  # Display range
        
        # Initialize metrics storage for all four categories
        # Each category tracks: delivered features, total features, and health score
        self.metrics = {
            'digitalTechnology': {
                'delivered': tk.IntVar(value=5),
                'total': tk.IntVar(value=153),
                'health': tk.DoubleVar(value=3.38)
            },
            'digital': {
                'delivered': tk.IntVar(value=3),
                'total': tk.IntVar(value=39),
                'health': tk.DoubleVar(value=3.63)
            },
            'enterpriseApplications': {
                'delivered': tk.IntVar(value=0),
                'total': tk.IntVar(value=43),
                'health': tk.DoubleVar(value=3.58)
            },
            'technologyOperations': {
                'delivered': tk.IntVar(value=2),
                'total': tk.IntVar(value=71),
                'health': tk.DoubleVar(value=3.21)
            }
        }
        
        # Build the user interface
        self.setup_ui()
        
        # Populate sprint dropdown with current increment values
        self.update_sprint_dropdown()
    
    def setup_ui(self):
        """
        Setup the complete user interface with all components.
        
        Creates:
            - Header section with title and subtitle
            - Configuration section for increment and sprint settings
            - Metrics input section with four category cards
            - Action buttons for history, save, and generate
        """
        # === HEADER SECTION ===
        # Dark blue header with application title and description
        header_frame = tk.Frame(self.root, bg="#003d5c", pady=15)
        header_frame.pack(fill=tk.X)
        
        title = tk.Label(
            header_frame,
            text="Sprint Metrics Dashboard Generator",
            font=("Inter", 20, "bold"),
            bg="#003d5c",
            fg="white"
        )
        title.pack()
        
        subtitle = tk.Label(
            header_frame,
            text="Configure and generate your sprint delivery metrics",
            font=("Inter", 10),
            bg="#003d5c",
            fg="#ff6633"
        )
        subtitle.pack()
        
        # === MAIN CONTAINER ===
        # Container for all form elements
        main_container = tk.Frame(self.root, bg="#f8f9fa", padx=20, pady=20)
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # === CONFIGURATION SECTION ===
        # Input fields for increment, sprint selection, and sprint range
        config_frame = tk.LabelFrame(
            main_container,
            text="Sprint Configuration",
            font=("Inter", 12, "bold"),
            bg="white",
            padx=15,
            pady=15
        )
        config_frame.pack(fill=tk.X, pady=(0, 15))
        
        config_grid = tk.Frame(config_frame, bg="white")
        config_grid.pack(fill=tk.X)
        
        # Increment Number Input
        # Allows selection of increment (e.g., 17, 18, 19)
        tk.Label(
            config_grid,
            text="Increment Number:",
            font=("Inter", 10, "bold"),
            bg="white"
        ).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        increment_spin = tk.Spinbox(
            config_grid,
            from_=1,
            to=100,
            textvariable=self.increment,
            font=("Inter", 10),
            width=15,
            command=self.update_sprint_dropdown  # Update sprints when increment changes
        )
        increment_spin.grid(row=1, column=0, padx=5, pady=5)
        
        # Current Sprint Dropdown
        # Shows sprints .1 through .6 for selected increment
        tk.Label(
            config_grid,
            text="Current Sprint:",
            font=("Inter", 10, "bold"),
            bg="white"
        ).grid(row=0, column=1, sticky="w", padx=5, pady=5)
        
        self.sprint_dropdown = ttk.Combobox(
            config_grid,
            textvariable=self.current_sprint,
            font=("Inter", 10),
            width=13,
            state="readonly"
        )
        self.sprint_dropdown.grid(row=1, column=1, padx=5, pady=5)
        
        # Sprint Range Input
        # Customizable display text for sprint range
        tk.Label(
            config_grid,
            text="Sprint Range:",
            font=("Inter", 10, "bold"),
            bg="white"
        ).grid(row=0, column=2, sticky="w", padx=5, pady=5)
        
        sprint_range_entry = tk.Entry(
            config_grid,
            textvariable=self.sprint_range,
            font=("Inter", 10),
            width=20
        )
        sprint_range_entry.grid(row=1, column=2, padx=5, pady=5)
        
        # === METRICS SECTION ===
        # Four category cards for entering delivery metrics
        metrics_frame = tk.LabelFrame(
            main_container,
            text="Metrics Configuration",
            font=("Inter", 12, "bold"),
            bg="white",
            padx=15,
            pady=15
        )
        metrics_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        metrics_grid = tk.Frame(metrics_frame, bg="white")
        metrics_grid.pack(fill=tk.BOTH, expand=True)
        
        # Define the four metric categories
        categories = [
            ('digitalTechnology', 'Digital Technology'),
            ('digital', 'Digital'),
            ('enterpriseApplications', 'Enterprise Applications'),
            ('technologyOperations', 'Technology Operations')
        ]
        
        # Create input card for each category
        for idx, (key, title) in enumerate(categories):
            # Calculate grid position (2x2 layout)
            row = idx // 2
            col = idx % 2
            
            # Create card frame with light blue background
            cat_frame = tk.Frame(metrics_grid, bg="#e3f2fd", relief=tk.RIDGE, bd=2)
            cat_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            
            # Category title
            tk.Label(
                cat_frame,
                text=title,
                font=("Inter", 11, "bold"),
                bg="#e3f2fd"
            ).pack(pady=(10, 5))
            
            # Features Delivered Input
            tk.Label(
                cat_frame,
                text="Features Delivered:",
                font=("Inter", 9),
                bg="#e3f2fd"
            ).pack(anchor="w", padx=10)
            
            tk.Entry(
                cat_frame,
                textvariable=self.metrics[key]['delivered'],
                font=("Inter", 10),
                width=20
            ).pack(padx=10, pady=(0, 5))
            
            # Total Features Input
            tk.Label(
                cat_frame,
                text="Total Features:",
                font=("Inter", 9),
                bg="#e3f2fd"
            ).pack(anchor="w", padx=10)
            
            tk.Entry(
                cat_frame,
                textvariable=self.metrics[key]['total'],
                font=("Inter", 10),
                width=20
            ).pack(padx=10, pady=(0, 5))
            
            # Health Score Input (0-4.00 scale)
            tk.Label(
                cat_frame,
                text="Health Score (out of 4.00):",
                font=("Inter", 9),
                bg="#e3f2fd"
            ).pack(anchor="w", padx=10)
            
            tk.Entry(
                cat_frame,
                textvariable=self.metrics[key]['health'],
                font=("Inter", 10),
                width=20
            ).pack(padx=10, pady=(0, 10))
        
        # Make grid columns expand equally
        metrics_grid.columnconfigure(0, weight=1)
        metrics_grid.columnconfigure(1, weight=1)
        
        # === ACTION BUTTONS SECTION ===
        # Buttons for history management and HTML generation
        button_frame = tk.Frame(main_container, bg="#f8f9fa")
        button_frame.pack(fill=tk.X)
        
        # View History Button
        tk.Button(
            button_frame,
            text="📜 View History",
            font=("Inter", 11, "bold"),
            bg="#6c757d",
            fg="white",
            padx=20,
            pady=10,
            command=self.show_history,
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)
        
        # Save to History Button
        tk.Button(
            button_frame,
            text="💾 Save to History",
            font=("Inter", 11, "bold"),
            bg="#28a745",
            fg="white",
            padx=20,
            pady=10,
            command=self.save_to_history,
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)
        
        # Generate & Download HTML Button
        tk.Button(
            button_frame,
            text="⬇ Generate HTML & Image",
            font=("Inter", 11, "bold"),
            bg="#007bff",
            fg="white",
            padx=20,
            pady=10,
            command=self.generate_files,
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)
    
    def update_sprint_dropdown(self):
        """
        Update the sprint dropdown options based on current increment.
        
        Generates sprint values from .1 to .6 for the selected increment.
        For example, if increment is 17, generates: 17.1, 17.2, ..., 17.6
        """
        inc = self.increment.get()
        sprints = [f"{inc}.{i}" for i in range(1, 7)]  # Generate 6 sprints
        self.sprint_dropdown['values'] = sprints
        
        # Reset current sprint if it doesn't match new increment
        if self.current_sprint.get() not in sprints:
            self.current_sprint.set(sprints[0])
    
    def load_history(self):
        """
        Load historical data from JSON file.
        
        Returns:
            list: List of historical records, or empty list if file doesn't exist
                  or contains invalid data
        """
        if self.history_file.exists():
            try:
                with open(self.history_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                # Return empty list if file is corrupted or unreadable
                return []
        return []
    
    def save_history(self):
        """
        Save current history list to JSON file.
        
        Persists all historical records to disk for future sessions.
        Uses pretty-printing (indent=2) for human readability.
        """
        with open(self.history_file, 'w') as f:
            json.dump(self.history, f, indent=2)
    
    def save_to_history(self):
        """
        Save current configuration and metrics to history.
        
        Creates a snapshot of current state including:
        - Increment and sprint information
        - All four categories' metrics
        - Timestamp for tracking
        
        Shows success message to user after saving.
        """
        # Create record with current configuration
        record = {
            'increment': self.increment.get(),
            'current_sprint': self.current_sprint.get(),
            'sprint_range': self.sprint_range.get(),
            'metrics': {
                key: {
                    'delivered': var['delivered'].get(),
                    'total': var['total'].get(),
                    'health': var['health'].get()
                }
                for key, var in self.metrics.items()
            },
            'timestamp': datetime.now().isoformat()
        }
        
        # Add to beginning of history list (most recent first)
        self.history.insert(0, record)
        self.save_history()
        
        messagebox.showinfo("Success", "Metrics saved to history!")
    
    def show_history(self):
        """
        Display history records in a new window.
        
        Creates a scrollable list of all saved records with options to:
        - Load a previous configuration
        - Delete a record
        
        Shows informative message if no history exists.
        """
        if not self.history:
            messagebox.showinfo("History", "No history records found.")
            return
        
        # Create new window for history display
        history_window = tk.Toplevel(self.root)
        history_window.title("History")
        history_window.geometry("600x400")
        
        tk.Label(
            history_window,
            text="Sprint History",
            font=("Inter", 14, "bold")
        ).pack(pady=10)
        
        # Create scrollable frame for history list
        canvas = tk.Canvas(history_window)
        scrollbar = ttk.Scrollbar(history_window, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
        
        # Configure scrolling behavior
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Create record entry for each history item
        for idx, record in enumerate(self.history):
            record_frame = tk.Frame(
                scrollable_frame,
                relief=tk.RAISED,
                bd=2,
                padx=10,
                pady=10
            )
            record_frame.pack(fill=tk.X, padx=10, pady=5)
            
            # Format display text with increment, sprint, and timestamp
            info_text = f"Increment {record['increment']} - Sprint {record['current_sprint']}\n"
            info_text += f"{datetime.fromisoformat(record['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}"
            
            tk.Label(
                record_frame,
                text=info_text,
                font=("Inter", 10)
            ).pack(side=tk.LEFT)
            
            # Load button - restores this configuration
            tk.Button(
                record_frame,
                text="Load",
                command=lambda r=record: self.load_from_history(r, history_window),
                bg="#007bff",
                fg="white",
                cursor="hand2"
            ).pack(side=tk.RIGHT, padx=5)
            
            # Delete button - removes this record
            tk.Button(
                record_frame,
                text="Delete",
                command=lambda i=idx: self.delete_history_item(i, history_window),
                bg="#dc3545",
                fg="white",
                cursor="hand2"
            ).pack(side=tk.RIGHT)
        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def load_from_history(self, record, window):
        """
        Load a historical configuration into the current form.
        
        Args:
            record (dict): Historical record containing all configuration
            window (tk.Toplevel): History window to close after loading
        
        Restores all values from the selected historical record and updates
        the form fields accordingly.
        """
        # Restore configuration values
        self.increment.set(record['increment'])
        self.current_sprint.set(record['current_sprint'])
        self.sprint_range.set(record['sprint_range'])
        
        # Restore all metrics for each category
        for key, values in record['metrics'].items():
            self.metrics[key]['delivered'].set(values['delivered'])
            self.metrics[key]['total'].set(values['total'])
            self.metrics[key]['health'].set(values['health'])
        
        # Update sprint dropdown to match loaded increment
        self.update_sprint_dropdown()
        
        # Close history window and show success message
        window.destroy()
        messagebox.showinfo("Success", "Configuration loaded from history!")
    
    def delete_history_item(self, index, window):
        """
        Delete a history record after user confirmation.
        
        Args:
            index (int): Index of record to delete in history list
            window (tk.Toplevel): History window to refresh after deletion
        """
        if messagebox.askyesno("Confirm", "Delete this history record?"):
            self.history.pop(index)
            self.save_history()
            window.destroy()
            # Reopen history window to show updated list
            self.show_history()
    
    def generate_files(self):
        """
        Generate HTML dashboard and a PNG image, and prompt user to save them.
        
        Creates a complete HTML file and a PNG image with:
        - Current increment and sprint information
        - All metrics from the four categories
        - Professional styling matching the original design
        
        Opens a file save dialog for the user to choose location and filename.
        """
        inc = self.increment.get()
        sprints = [f"{inc}.{i}" for i in range(1, 7)]
        current = self.current_sprint.get()
        
        # Extract current metrics into plain dictionary
        metrics_data = {
            key: {
                'delivered': var['delivered'].get(),
                'total': var['total'].get(),
                'health': var['health'].get()
            }
            for key, var in self.metrics.items()
        }
        
        # Generate HTML content
        html = self._generate_html_content(inc, current, sprints, metrics_data)
        
        # Prompt user for save location
        filename = filedialog.asksaveasfilename(
            defaultextension=".html",
            filetypes=[("HTML files", "*.html"), ("PNG files", "*.png")],
            initialfile=f"sprint-dashboard-{inc}-{current}.html"
        )
        
        if filename:
            # Ensure the filename has the correct extension
            if not filename.endswith(".html"):
                filename += ".html"

            # Write HTML to selected file
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html)
            
            # Generate image in a separate thread
            image_filename = filename.replace(".html", ".png")
            thread = threading.Thread(target=self._generate_image_in_thread, args=(filename, image_filename))
            thread.start()

    def _generate_image_in_thread(self, html_path, image_path):
        """
        Generate a PNG image from an HTML file.
        
        Args:
            html_path (str): Path to the input HTML file.
            image_path (str): Path to save the output PNG image.
        """
        try:
            self._generate_image_from_html(html_path, image_path)
        except Exception as e:
            print(f"Could not generate image: {e}")


    def _generate_image_from_html(self, html_path, image_path):
        """
        Generate a PNG image from an HTML file.
        
        Args:
            html_path (str): Path to the input HTML file.
            image_path (str): Path to save the output PNG image.
        """
        try:
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')

            driver = webdriver.Chrome(options=options)
            
            # Get the absolute path to the HTML file
            abs_html_path = os.path.abspath(html_path)
            driver.get(f"file://{abs_html_path}")
            
            # Give the browser a moment to render
            driver.implicitly_wait(2)

            # Get the height of the container element
            total_height = driver.execute_script("return document.querySelector('.container').scrollHeight")
            
            # Set the window size to capture the full height
            driver.set_window_size(1400, total_height)
            
            # Take a screenshot of the container element
            driver.find_element("class name", "container").screenshot(image_path)
            
            driver.quit()
        except Exception as e:
            messagebox.showerror("Image Generation Error", f"Could not generate image: {e}")

    
    def _generate_html_content(self, increment, current_sprint, sprints, metrics):
        """
        Generate complete HTML content for the dashboard.
        
        Args:
            increment (int): Current increment number
            current_sprint (str): Active sprint identifier
            sprints (list): List of all sprint identifiers for progress bar
            metrics (dict): Dictionary containing all metric values
        
        Returns:
            str: Complete HTML document as string
        
        The generated HTML includes:
        - Inter font from Google Fonts
        - Exact color scheme matching original design
        - Responsive grid layout for cards
        - Progress bar with active sprint indicator
        - All metric values properly formatted
        """
        sprint_range = self.sprint_range.get()
        
        # Generate progress bar HTML segments
        progress_html = ''.join([
            f'<div class="progress-item {"active" if s == current_sprint else ""}">{s}</div>'
            for s in sprints
        ])
        
        # Return complete HTML document
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Technology - Increment {increment}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: Arial, sans-serif;
            background-color: #e8e8e8;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: rgb(224, 224, 224);
            padding: 30px;
            border-radius: 10px;
        }}
        
        .header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }}
        
        .title {{
            font-size: 55px;
            font-weight: 700;
            color: #003d5c;
        }}
        
        .title .increment {{
            font-weight: 700;
            color: #ff6633;
        }}
        
        .subtitle {{
            font-size: 30px;
            font-weight: 700;
            color: #ff6633;
            margin-bottom: 5px;
        }}
        
        .subtitle .sprintrange {{
            font-weight: 700;
            color: #003d5c;
        }}
        
        .logo {{
            font-size: 32px;
            font-weight: 700;
            color: #003d5c;
        }}
        
        .logo .industrial {{
            font-size: 14px;
            display: block;
            text-align: right;
            margin-top: -5px;
        }}
        
        .progress-container {{
            display: flex;
            background: #ffffff;
            border-radius: 25px;
            padding: 8px;
            margin-bottom: 10px;
            position: relative;
        }}
        
        .progress-item {{
            flex: 1;
            font-size: 20px;
            text-align: center;
            padding: 8px;
            color: #999;
            font-weight: 700;
            position: relative;
            z-index: 1;
        }}
        
        .progress-item.active {{
            background: #ff6633;
            color: white;
            font-size: 20px;
            border-radius: 20px;
            position: relative;
        }}
        
        .progress-item.active::after {{
            content: '';
            position: absolute;
            right: -15px;
            top: 50%;
            transform: translateY(-50%);
            width: 18px;
            height: 18px;
            background: #003d5c;
            border-radius: 50%;
            border: 3px solid white;
        }}
        
        .cards-container {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
        }}
        
        .card {{
            border: 3px solid #003d5c;
            border-radius: 15px;
            overflow: hidden;
            background: white;
        }}
        
        .card-header {{
            font-size: 40px;
            padding: 20px;
            color: white;
            min-height: 320px;
        }}
        
        .card-header-primary {{
            background: #003d5c;
            min-height: 320px;
            padding: 20px;
        }}
        
        .card-header-secondary {{
            padding: 20px;
            background: linear-gradient(135deg, #4a6c7d 0%, #003d5c 100%);
        }}
        
        .card-header h2 {{
            font-size: 36px;
            font-weight: 700;
            text-align: center;
            margin-bottom: 15px;
            line-height: 1.2;
        }}
        
        .item {{
            font-size: 14px;
            margin-bottom: 5px;
        }}
        
        .maincard-body {{
            padding: 30px 20px;
            text-align: center;
            background: white;
        }}
        .card-body {{
            padding: 30px 20px;
            text-align: center;
            background: linear-gradient(135deg, #4a6c7d 0%, #003d5c 100%);
        }}
        
        .metric-large {{
            font-size: 120px;
            font-weight: 700;
            color: #003d5c;
            line-height: 1;
            display: inline;
        }}
        .metric-largewhite {{
            font-size: 120px;
            font-weight: 700;
            color: white;
            line-height: 1;
            display: inline;
        }}
        
        .metric-divider {{
            height: 10px;
            background: #ff6633;
            margin: 10px 40px;
        }}
        
        .metric-label {{
            font-size: 20px;
            font-weight: 700;
            color: #003d5c;
            margin-top: 15px;
        }}
        
        .metric-labelwhite {{
            font-size: 20px;
            font-weight: 700;
            color: white;
            margin-top: 15px;
        }}
        .card-footer {{
            background: #ff6633;
            padding: 20px;
            text-align: center;
            color: white;
        }}
        
        .health-score {{
            font-size: 100px;
            font-weight: 700;
            display: inline;
        }}
        
        .health-divider {{
            height: 8px;
            background: #003d5c;
            margin: 8px 20px;
        }}
        
        .health-max {{
            font-size: 60px;
            font-weight: 700;
        }}
        
        .health-label {{
            font-size: 20px;
            font-weight: 700;
            margin-top: 8px;
            letter-spacing: 1px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div>
                <div class="title">DIGITAL TECHNOLOGY – <span class="increment">INCREMENT {increment}</span></div>
                <div class="subtitle">Delivery metrics for <span class="sprintrange">Sprint {sprint_range}</span></div>
            </div>
            <div class="logo">
                SIME
                <span class="industrial">INDUSTRIAL</span>
            </div>
        </div>
        
        <div class="progress-container">{progress_html}</div>
        
        <div class="cards-container">
            
        <div class="card">
            <div class="card-header card-header-primary">
                <h2>DIGITAL TECHNOLOGY</h2>
                <div class="item">✓ DIGITAL</div><div class="item">✓ ENTERPRISE APPLICATIONS</div><div class="item">✓ TECHNOLOGY OPERATIONS</div>
            </div>
            <div class="maincard-body">
                <div class="metric-large">{metrics['digitalTechnology']['delivered']}</div>
                <div class="metric-divider"></div>
                <div class="metric-large">{metrics['digitalTechnology']['total']}</div>
                <div class="metric-label">FEATURES DELIVERED</div>
            </div>
            <div class="card-footer">
                <div class="health-score">{metrics['digitalTechnology']['health']:.2f}</div>
                <div class="health-divider"></div>
                <div class="health-max">4.00</div>
                <div class="health-label">HEALTH METRICS</div>
            </div>
        </div>
        
        <div class="card">
            <div class="card-header card-header-secondary">
                <h2>DIGITAL</h2>
                <div class="item">✓ AVATARS</div><div class="item">✓ DESTINO</div><div class="item">✓ SDI WEBSITE</div><div class="item">✓ XENO</div>
            </div>
            <div class="card-body">
                <div class="metric-largewhite">{metrics['digital']['delivered']}</div>
                <div class="metric-divider"></div>
                <div class="metric-largewhite">{metrics['digital']['total']}</div>
                <div class="metric-labelwhite">FEATURES DELIVERED</div>
            </div>
            <div class="card-footer">
                <div class="health-score">{metrics['digital']['health']:.2f}</div>
                <div class="health-divider"></div>
                <div class="health-max">4.00</div>
                <div class="health-label">HEALTH METRICS</div>
            </div>
        </div>
        
        <div class="card">
            <div class="card-header card-header-secondary">
                <h2>ENTERPRISE APPLICATIONS</h2>
                <div class="item">✓ AX GUARDIANS</div><div class="item">✓ DELTA 365</div><div class="item">✓ ENTERPRISE AUTOMATION</div><div class="item">✓ WARETEC</div>
            </div>
            <div class="card-body">
                <div class="metric-largewhite">{metrics['enterpriseApplications']['delivered']}</div>
                <div class="metric-divider"></div>
                <div class="metric-largewhite">{metrics['enterpriseApplications']['total']}</div>
                <div class="metric-labelwhite">FEATURES DELIVERED</div>
            </div>
            <div class="card-footer">
                <div class="health-score">{metrics['enterpriseApplications']['health']:.2f}</div>
                <div class="health-divider"></div>
                <div class="health-max">4.00</div>
                <div class="health-label">HEALTH METRICS</div>
            </div>
        </div>
        
        <div class="card">
            <div class="card-header card-header-secondary">
                <h2>TECHNOLOGY OPERATIONS</h2>
                <div class="item">✓ CSI</div><div class="item">✓ CYBER DEFENCE</div><div class="item">✓ CYBER OPERATIONS</div><div class="item">✓ ENTERPRISE ARCHITECTURE</div><div class="item">✓ GRC</div><div class="item">✓ JSOC</div><div class="item">✓ MATRIX</div>
            </div>
            <div class="card-body">
                <div class="metric-largewhite">{metrics['technologyOperations']['delivered']}</div>
                <div class="metric-divider"></div>
                <div class="metric-largewhite">{metrics['technologyOperations']['total']}</div>
                <div class="metric-labelwhite">FEATURES DELIVERED</div>
            </div>
            <div class="card-footer">
                <div class="health-score">{metrics['technologyOperations']['health']:.2f}</div>
                <div class="health-divider"></div>
                <div class="health-max">4.00</div>
                <div class="health-label">HEALTH METRICS</div>
            </div>
        </div>
        
        </div>
    </div>
</body>
</html>'''


# ============================================================================
# UNIT TESTS
# ============================================================================

class TestSprintMetricsApp(unittest.TestCase):
    """
    Comprehensive unit tests for Sprint Metrics Dashboard Generator.
    
    Tests cover:
    - Sprint dropdown generation
    - History management (load, save, delete)
    - HTML generation
    - Data validation
    """
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Create mock root window for testing
        self.root = tk.Tk()
        self.root.withdraw()  # Hide window during tests
        self.app = SprintMetricsApp(self.root)
        
        # Clean up any existing test history file
        self.test_history_file = Path("test_sprint_history.json")
        if self.test_history_file.exists():
            self.test_history_file.unlink()
        
        # Override history file path for testing and ensure it's empty
        self.app.history_file = self.test_history_file
        self.app.history = []
        self.app.save_history()
    
    def tearDown(self):
        """Clean up after each test method."""
        # Destroy tkinter window
        self.root.destroy()
        
        # Clean up test files
        if self.test_history_file.exists():
            self.test_history_file.unlink()
    
    def test_initial_values(self):
        """Test that application initializes with correct default values."""
        self.assertEqual(self.app.increment.get(), 17)
        self.assertEqual(self.app.current_sprint.get(), "17.1")
        self.assertEqual(self.app.sprint_range.get(), "17.1 - 17.1")
        
        # Test default metrics
        self.assertEqual(self.app.metrics['digitalTechnology']['delivered'].get(), 5)
        self.assertEqual(self.app.metrics['digital']['total'].get(), 39)
        self.assertAlmostEqual(self.app.metrics['enterpriseApplications']['health'].get(), 3.58)
    
    def test_sprint_dropdown_generation(self):
        """Test that sprint dropdown generates correct values for different increments."""
        # Test increment 17
        self.app.increment.set(17)
        self.app.update_sprint_dropdown()
        expected_sprints = ["17.1", "17.2", "17.3", "17.4", "17.5", "17.6"]
        self.assertEqual(list(self.app.sprint_dropdown['values']), expected_sprints)
        
        # Test increment 18
        self.app.increment.set(18)
        self.app.update_sprint_dropdown()
        expected_sprints = ["18.1", "18.2", "18.3", "18.4", "18.5", "18.6"]
        self.assertEqual(list(self.app.sprint_dropdown['values']), expected_sprints)
        
        # Test that current sprint resets if invalid
        self.app.current_sprint.set("17.1")
        self.app.increment.set(19)
        self.app.update_sprint_dropdown()
        self.assertEqual(self.app.current_sprint.get(), "19.1")
    
    def test_save_and_load_history(self):
        """Test saving and loading history from JSON file."""
        # Override history file path for testing
        self.app.history_file = self.test_history_file
        
        # Save a record
        self.app.increment.set(17)
        self.app.current_sprint.set("17.3")
        self.app.metrics['digital']['delivered'].set(10)
        
        self.app.save_to_history()
        
        # Verify history was saved
        self.assertEqual(len(self.app.history), 1)
        self.assertEqual(self.app.history[0]['increment'], 17)
        self.assertEqual(self.app.history[0]['current_sprint'], "17.3")
        
        # Create new app instance and verify history loads
        new_app = SprintMetricsApp(self.root)
        new_app.history_file = self.test_history_file
        new_app.history = new_app.load_history()
        
        self.assertEqual(len(new_app.history), 1)
        self.assertEqual(new_app.history[0]['metrics']['digital']['delivered'], 10)
    
    def test_load_from_history(self):
        """Test loading configuration from a historical record."""
        # Create a test record
        test_record = {
            'increment': 18,
            'current_sprint': '18.4',
            'sprint_range': '18.1 - 18.4',
            'metrics': {
                'digitalTechnology': {'delivered': 8, 'total': 200, 'health': 3.5},
                'digital': {'delivered': 5, 'total': 50, 'health': 3.7},
                'enterpriseApplications': {'delivered': 2, 'total': 30, 'health': 3.2},
                'technologyOperations': {'delivered': 4, 'total': 80, 'health': 3.9}
            },
            'timestamp': datetime.now().isoformat()
        }
        
        # Create mock window
        mock_window = Mock()
        mock_window.destroy = Mock()
        
        # Load the record
        self.app.load_from_history(test_record, mock_window)
        
        # Verify all values were loaded correctly
        self.assertEqual(self.app.increment.get(), 18)
        self.assertEqual(self.app.current_sprint.get(), '18.4')
        self.assertEqual(self.app.sprint_range.get(), '18.1 - 18.4')
        self.assertEqual(self.app.metrics['digitalTechnology']['delivered'].get(), 8)
        self.assertEqual(self.app.metrics['digital']['health'].get(), 3.7)
        
        # Verify window was closed
        mock_window.destroy.assert_called_once()
    
    def test_html_generation_structure(self):
        """Test that HTML generation creates valid structure."""
        # Set test values
        self.app.increment.set(17)
        self.app.current_sprint.set("17.2")
        self.app.metrics['digitalTechnology']['delivered'].set(7)
        
        def run_thread_synchronously(target, args):
            target(*args)
            # Return a mock object that has a start method
            thread_mock = Mock()
            thread_mock.start = lambda: None
            return thread_mock

        # Mock the file dialog and threading
        with patch('tkinter.filedialog.asksaveasfilename', return_value="test.html"), \
             patch('threading.Thread', side_effect=run_thread_synchronously):
            # Generate files
            self.app.generate_files()

        # Verify HTML structure
        with open("test.html", "r") as f:
            html = f.read()

        self.assertIn('<!DOCTYPE html>', html)
        self.assertIn('INCREMENT 17', html)
        self.assertIn('DIGITAL TECHNOLOGY', html)
        self.assertIn('FEATURES DELIVERED', html)
        self.assertIn('HEALTH METRICS', html)
        
        # Verify metrics are included
        self.assertIn('7', html)  # delivered count
        self.assertIn('153', html)  # total count
        self.assertIn('3.38', html)  # health score
        
        # Verify active sprint is marked
        self.assertIn('class="progress-item active">17.2', html)

        # Verify that the image was created
        self.assertTrue(Path("test.png").exists())

        # Clean up the created files
        Path("test.html").unlink()
        Path("test.png").unlink()
    
    def test_html_formatting_precision(self):
        """Test that health scores are formatted to 2 decimal places."""
        metrics_data = {
            'digitalTechnology': {'delivered': 5, 'total': 153, 'health': 3.3847},
            'digital': {'delivered': 3, 'total': 39, 'health': 3.629},
            'enterpriseApplications': {'delivered': 0, 'total': 43, 'health': 3.5},
            'technologyOperations': {'delivered': 2, 'total': 71, 'health': 3.2145}
        }
        
        html = self.app._generate_html_content(17, "17.1", ["17.1"], metrics_data)
        
        # Verify health scores are rounded to 2 decimals
        self.assertIn('3.38', html)  # 3.3847 -> 3.38
        self.assertIn('3.63', html)  # 3.629 -> 3.63
        self.assertIn('3.50', html)  # 3.5 -> 3.50
        self.assertIn('3.21', html)  # 3.2145 -> 3.21
    
    def test_delete_history_item(self):
        """Test deleting a history record."""
        # Override history file for testing
        self.app.history_file = self.test_history_file
        
        # Add multiple records
        for i in range(3):
            self.app.increment.set(17)
            self.app.current_sprint.set(f"17.{i+1}")
            self.app.save_to_history()
        
        # Verify we have 3 records
        self.assertEqual(len(self.app.history), 3)
        
        # Delete middle record (index 1)
        self.app.history.pop(1)
        self.app.save_history()
        
        # Reload and verify
        self.app.history = self.app.load_history()
        self.assertEqual(len(self.app.history), 2)
    
    def test_empty_history_handling(self):
        """Test that application handles empty history gracefully."""
        # Override history file to non-existent file
        self.app.history_file = Path("non_existent_history.json")
        
        # Load history from non-existent file
        history = self.app.load_history()
        
        self.assertEqual(history, [])
        self.assertIsInstance(history, list)
    
    def test_corrupted_history_handling(self):
        """Test that application handles corrupted history file gracefully."""
        # Create corrupted JSON file
        self.app.history_file = self.test_history_file
        with open(self.test_history_file, 'w') as f:
            f.write("This is not valid JSON{[]}")
        
        # Load history should return empty list
        history = self.app.load_history()
        self.assertEqual(history, [])
    
    def test_metrics_update(self):
        """Test updating metric values through the application."""
        # Update metrics
        self.app.metrics['digital']['delivered'].set(15)
        self.app.metrics['digital']['total'].set(100)
        self.app.metrics['digital']['health'].set(3.95)
        
        # Verify updates
        self.assertEqual(self.app.metrics['digital']['delivered'].get(), 15)
        self.assertEqual(self.app.metrics['digital']['total'].get(), 100)
        self.assertAlmostEqual(self.app.metrics['digital']['health'].get(), 3.95)


def run_tests():
    """
    Run all unit tests and display results.
    
    Returns:
        bool: True if all tests passed, False otherwise
    """
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestSprintMetricsApp)
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return success status
    return result.wasSuccessful()


def main():
    """
    Main entry point for the application.
    
    Provides option to run tests before starting the GUI application.
    """
    import sys
    
    # Check if running in test mode
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        print("\n" + "="*70)
        print("RUNNING UNIT TESTS")
        print("="*70 + "\n")
        success = run_tests()
        sys.exit(0 if success else 1)
    
    # Start GUI application
    root = tk.Tk()
    app = SprintMetricsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()