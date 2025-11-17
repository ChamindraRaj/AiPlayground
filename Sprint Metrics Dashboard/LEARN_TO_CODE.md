# How the Sprint Dashboard Works: Your First Step into Coding

Hello! As an Iteration Manager or Agile Coach, you're an expert at managing processes, people, and projects. You might look at an application like the Sprint Dashboard and think the code behind it is a completely different world.

The goal of this document is to show you that it's not as mysterious as it looks. Code is simply a set of very specific instructions, like a detailed recipe for a computer to follow. We're going to look at the "recipe" for the Sprint Dashboard app you already use, and in doing so, take our first steps into the world of Python programming.

Don't worry about understanding everything at once. The goal is to recognize the basic building blocks and see how they come together to create a tool you're familiar with.

---

## Part 1: The Blueprint (What is a `class`?)

Think about the blueprint for a house. The blueprint isn't the house itself, but it defines everything a house should have: walls, a roof, rooms, doors, and windows.

In Python, a **`class`** is exactly like that: it's a blueprint for creating something. Our application's main blueprint is called `SprintMetricsApp`.

```python
class SprintMetricsApp:
    """
    Main application class for Sprint Metrics Dashboard Generator.
    ...
    """
```

When we start the program, we're telling the computer: "Build me one object using the `SprintMetricsApp` blueprint."

---

## Part 2: Laying the Foundation (The `__init__` method)

Every blueprint has a starting point. When you build a house, the first thing you do is lay the foundation and put up the main structure.

In a Python class, there's a special function called **`__init__`** (short for "initialize") that does exactly this. It's the setup phase that runs automatically as soon as the object is created.

Let's look at a few lines from our app's `__init__` method:

```python
def __init__(self, root):
    # ...
    self.history_file = Path("sprint_history.json")
    self.history = self.load_history()
    
    self.increment = tk.IntVar(value=17)
    self.current_sprint = tk.StringVar(value="17.1")
    # ...
```

This might look complex, but let's translate it:

1.  `self.history_file = Path("sprint_history.json")`
    *   **Translation:** "Hey app, remember the name of the file where we'll save our history. It's called `sprint_history.json`."
2.  `self.increment = tk.IntVar(value=17)`
    *   **Translation:** "We need a place to store the Increment number. Let's create a special variable for it and set its default value to `17`."

This introduces our next key concept: **variables**. A variable is just a labeled box where you can store a piece of information. Here, we've created a box labeled `increment` and put the number `17` inside.

---

## Part 3: Building the Rooms (What are "functions"?)

A house isn't just a foundation; it's made up of rooms, each with a specific purpose. A kitchen is for cooking, a bedroom is for sleeping.

In a class, **functions** (also called "methods") are the "rooms." They are named blocks of code that perform one specific task.

You've already used these functions by clicking buttons in the app!

#### Example 1: The "Save to History" Button

When you click the "Save to History" button, the app executes the `save_to_history` function.

```python
def save_to_history(self):
    # Create a "record" of the current data
    record = {
        'increment': self.increment.get(),
        'current_sprint': self.current_sprint.get(),
        # ... and so on for all the metrics
    }
    
    # Add this new record to our history list
    self.history.insert(0, record)
    
    # Now, save the entire list to the file
    self.save_history()
    
    messagebox.showinfo("Success", "Metrics saved to history!")
```

**Let's walk through this recipe:**

1.  It creates a `record`. Think of this like a digital index card.
2.  It gets the current values from the input fields (like `self.increment.get()`) and writes them onto the card.
3.  It takes this new card and adds it to the top of our `self.history` list.
4.  It then calls *another* function, `self.save_history()`, whose only job is to write the entire updated list to the `sprint_history.json` file.
5.  Finally, it shows you that friendly "Success" pop-up message.

See? It's a logical, step-by-step process.

---

## Part 4: Making Decisions (`if` statements)

A good recipe often has conditional steps. "If the batter is too thick, then add more milk."

Programs make decisions all the time using **`if` statements**.

Let's look at the `show_history` function, which runs when you click "View History". What happens if there's no history to show?

```python
def show_history(self):
    if not self.history:
        messagebox.showinfo("History", "No history records found.")
        return
    
    # ... if there IS history, the code continues here
    # to build the history window...
```

**Translation:**

-   `if not self.history:`
    -   This is the check. It asks the question: "Is the `history` list empty?" (The `not` keyword checks if something is empty or false).
-   `messagebox.showinfo(...)`
    -   **If the answer is yes** (the list is empty), it executes this line to show you the "No history records found" pop-up.
-   `return`
    -   This keyword means "stop right here." Since there's no history, there's no point in continuing.
-   If the history list is *not* empty, the `if` block is skipped, and the code continues on to build and display the history window.

---

## Part 5: A Guided Tour of the Code

Now that you know the basic concepts, let's take a high-level tour of the entire `sprint_metrics_python.py` file from top to bottom.

### The Imports (The Toolbox)

At the very top of the file, you see lines starting with `import`.

```python
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os
# ... and others
```

Think of `import` as grabbing a pre-packed toolbox. Python comes with many toolboxes for common tasks. Instead of writing code from scratch to create a window or read a JSON file, we can just `import` a toolbox that already has the tools we need.

-   `import tkinter`: This is the main toolbox for building the graphical user interface (GUI).
-   `import json`: This toolbox gives us the tools to read and write data in the JSON format, which we use for our history file.
-   `import selenium`: This is the powerful toolbox we use to control a web browser to take a screenshot for the PNG export.

### The `SprintMetricsApp` Class (The Blueprint Revisited)

As we discussed, this is the main blueprint for our application. Almost all the code is inside this class.

### The `__init__` function (The Constructor)

This is the starting point. It sets up all the application's initial variables and memory. It defines the default values for the increment, sprint, and all the metrics. It also calls `self.setup_ui()` to actually build the visual part of the app.

### The `setup_ui` function (The Interior Designer)

This is a large function, but its job is singular: to create and arrange all the visual elements on the screen. It creates the header, the configuration section, the four metric cards, and the action buttons at the bottom. It's like an interior designer placing furniture in the rooms of a house.

### History Management Functions (The Librarian)

This is a group of functions dedicated to managing the `sprint_history.json` file.

-   `load_history()`: Reads the disk and loads the `sprint_history.json` file into the app's memory.
-   `save_history()`: Takes the current history from memory and writes it to the disk.
-   `save_to_history()`: The function that runs when you click the "Save" button. It creates a new record and adds it to the history.
-   `show_history()`, `load_from_history()`, `delete_history_item()`: These functions manage the "View History" window, allowing you to see, load, and delete old records.

### Dashboard Generation Functions (The Artist)

This group of functions works together to create the final HTML and PNG files.

-   `generate_files()`: This is the main function called when you click the "Generate" button. It asks you where to save the file and then kicks off the other two functions.
-   `_generate_html_content()`: This is the true artist. It takes all the current metrics and builds the beautiful, self-contained HTML file as a long string of text.
-   `_generate_image_from_html()`: This function takes the newly created HTML file, opens it in a hidden Chrome browser, and takes a screenshot, which it saves as the PNG image.

### The Ignition Switch (`if __name__ == "__main__":`)

At the very bottom of the file, you'll find this peculiar block:

```python
if __name__ == "__main__":
    main()
```

This is a standard piece of Python code that acts like the ignition switch in a car. It essentially says: "**If this file is the one being run directly**, then execute the `main()` function."

The `main()` function itself is very simple: it creates the main application window (`root = tk.Tk()`), creates an instance of our app from the blueprint (`app = SprintMetricsApp(root)`), and then tells the window to start running and listening for mouse clicks and keyboard presses (`root.mainloop()`).

---

## Your Journey Starts Here

Congratulations! You've just taken a tour of a real Python application and learned four fundamental concepts that are the bedrock of almost all programming:

1.  **Classes:** Blueprints for creating objects.
2.  **Variables:** Labeled boxes for storing information.
3.  **Functions:** Reusable blocks of code that perform specific tasks.
4.  **`if` Statements:** Code that makes decisions.

The next time you use the Sprint Dashboard, you'll know a little more about the "magic" happening behind the scenes.

If this has sparked your curiosity, here are some fantastic, beginner-friendly resources to continue your journey:

-   **[The Official Python Tutorial](https://docs.python.org/3/tutorial/)**: A great place to start, from the creators of Python.
-   **[freeCodeCamp's Python for Beginners](https://www.freecodecamp.org/learn/scientific-computing-with-python/)**: Free, hands-on video courses.
-   **[Real Python](https://realpython.com/)**: A treasure trove of articles and tutorials for all skill levels.

Happy coding!
