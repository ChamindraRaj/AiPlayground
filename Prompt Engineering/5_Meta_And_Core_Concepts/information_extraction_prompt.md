
# Information Extraction Prompt: The Data Extractor

This prompt is designed for accurately extracting and structuring specific pieces of information from a block of unstructured text. It's particularly useful for processing emails, reports, or any text where you need to pull out key-value data.

## The Prompt

```
**Objective:** You are a highly accurate data extraction tool. Your task is to extract specific pieces of information from the text provided below and format it as a JSON object.

**Schema Definition:**

You must follow this JSON schema precisely. Do not add any fields that are not defined here. If a piece of information cannot be found, use `null` as the value.

*   `invoice_id` (string): The unique identifier for the invoice.
*   `customer_name` (string): The full name of the customer.
*   `due_date` (string): The date the payment is due, formatted as "YYYY-MM-DD".
*   `total_amount` (float): The total amount due, as a floating-point number.
*   `items` (array of objects): A list of items on the invoice. Each object should have:
    *   `description` (string): The description of the item.
    *   `quantity` (integer): The quantity of the item.
    *   `unit_price` (float): The price of a single unit of the item.

**Instructions:**

1.  Read the text carefully.
2.  Identify the information that corresponds to each field in the JSON schema.
3.  Pay close attention to data types (e.g., convert the total amount to a float, quantity to an integer).
4.  Format dates strictly as YYYY-MM-DD.
5.  If a field is missing in the source text, you MUST use `null` for its value. Do not omit the key.

---

**Text for Extraction:**

"Dear John Doe,

Thank you for your recent purchase. This email serves as the receipt for invoice #INV-123-456. The total charge to your account is $145.50. Payment is expected by October 25, 2023.

Here is a summary of your order:
- 2 units of 'Premium Widget' at $50.00 each.
- 1 unit of 'Widget Accessory Pack' at $45.50.

Please let us know if you have any questions.

Sincerely,
The Merchant"
```

## Documentation

### Why this prompt is effective:

1.  **Clear Objective and Role:** It defines the AI's role as a "data extraction tool," focusing it on a specific, non-creative task.
2.  **Strict Schema Definition:** This is the most critical part of the prompt. Providing a clear JSON schema with field names and expected data types leaves no room for ambiguity. It tells the AI *exactly* what to look for and how to structure it.
3.  **Handling Missing Data:** The instruction to use `null` for missing information is crucial for creating consistent and predictable output. Without this, the AI might omit fields or use placeholders like "N/A," making the resulting JSON difficult to parse programmatically.
4.  **Specific Formatting Rules:** Rules for date formatting and data type conversion (e.g., string to float) ensure the output is immediately usable by other applications or scripts without needing further cleaning.
5.  **Separation of Instructions and Data:** The prompt clearly separates the instructions and schema from the actual text to be processed. This makes it easy to reuse the prompt with different input texts.

### How to use it:

1.  Define the `Schema Definition` to match the exact data structure you need. Be precise about field names and data types (string, integer, float, boolean, array).
2.  Update the `Instructions` with any specific formatting rules you require (e.g., date formats, currency conversion, etc.).
3.  Place the unstructured text you want to process in the `Text for Extraction` section.
4.  This prompt is ideal for automating data entry, processing emails, and converting unstructured reports into structured data that can be fed into a database or another system.
