
# Code Generation Prompt: The Senior Software Engineer

This prompt frames the code generation task as a request to a senior software engineer. It emphasizes best practices, documentation, and testing, leading to higher-quality, production-ready code.

## The Prompt

```
**Persona:** You are a senior software engineer with 10+ years of experience, specializing in creating robust, well-documented, and highly efficient code. You adhere strictly to industry best practices.

**Task:** Write a Python function that accomplishes the following:

1.  **Function Name:** `find_most_common_word`
2.  **Objective:** The function should take a single string of text as input and return the most frequently occurring word.
3.  **Requirements:**
    *   The function should be case-insensitive (e.g., "The" and "the" are the same word).
    *   Punctuation should be ignored.
    *   If there is a tie for the most common word, return the one that appears first alphabetically.
    *   The function should handle empty or whitespace-only strings gracefully by returning `None`.

**Code Quality Standards:**

*   **Typing:** Use Python's type hints for all function arguments and return values.
*   **Docstrings:** Include a comprehensive docstring in Google Python Style that explains what the function does, its arguments, and what it returns. Include at least one example of its usage.
*   **Comments:** Add comments only for non-obvious parts of the code. The code should be largely self-documenting.
*   **Efficiency:** The solution should be efficient. Aim for a time complexity of O(n), where n is the number of words in the text.

**Testing:**

After writing the function, create a set of at least 5 unit test cases using the `unittest` framework to verify its correctness. The test cases should cover:
1.  A simple case.
2.  A case with mixed casing.
3.  A case with punctuation.
4.  A case with a tie, to check the alphabetical rule.
5.  An edge case, such as an empty string.

---

Please provide the complete Python code, including the function and the unit tests.
```

## Documentation

### Why this prompt is effective:

1.  **Expert Persona:** Assigning the "Senior Software Engineer" persona primes the model to produce code that is more than just functional; it's well-structured and professional.
2.  **Clear and Unambiguous Requirements:** The prompt breaks down the task into specific, numbered requirements. There is no ambiguity about how to handle cases, punctuation, or ties. This is crucial for getting the desired logic right on the first try.
3.  **Explicit Code Quality Standards:** Demanding type hints, specific docstring formats, and efficiency forces the model to adhere to best practices that are often overlooked in simpler prompts. This elevates the quality of the generated code from a "script" to "software."
4.  **Mandatory Testing:** This is a critical component. By requiring unit tests, you are asking the AI not just to *write* the code, but to *verify* it. This catches logical errors and ensures the code behaves as expected across a range of inputs.
5.  **Holistic Request:** The prompt asks for a complete solution: the function *and* its tests. This provides a full, ready-to-use code artifact.

### How to use it:

1.  Change the `Task` section to describe the function you need. Be as specific as possible in the `Objective` and `Requirements`.
2.  Adjust the `Code Quality Standards` to match the language and conventions of your project (e.g., specify JSDoc for JavaScript, or a different docstring style for Python).
3.  Modify the `Testing` section to specify the testing framework you prefer (e.g., `pytest`, `Jest`, `JUnit`).
4.  This prompt is highly effective for generating reliable and well-documented utility functions, algorithms, or small components.
