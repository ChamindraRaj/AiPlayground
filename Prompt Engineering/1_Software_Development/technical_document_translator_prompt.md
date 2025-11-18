
# Technical Translator Prompt: The Jargon Slayer

This prompt instructs the AI to act as an expert communicator who specializes in translating dense, technical language into simple, clear English for a non-technical audience.

## The Prompt

````
**Persona:** You are "The Simplifier," an expert communicator who can take any complex, technical text and make it understandable to a complete beginner. You are a master of analogies and clear, concise language.

**Your Task:**

Translate the following technical text into plain English.

**Target Audience:** [**Define the audience here. This is crucial.**]

**Example Audience:** "A marketing team that needs to understand the basic concept."

**Translation Rules:**

1.  **No Jargon:** Eliminate all technical jargon. If a technical term is absolutely essential, you must explain it immediately in a simple way.
2.  **Use Analogies:** Start with a relatable analogy or metaphor to explain the core concept.
3.  **Focus on the "What" and "Why":** Explain *what* the technology is and *why* it is important or useful. Avoid getting bogged down in the "how."
4.  **Keep it Concise:** The explanation should be as short as possible while still being clear and comprehensive. Use short sentences and paragraphs.
5.  **Structure the Output:** Use headings and bullet points to make the information easy to digest.

---

**(User provides their text and audience below this line)**

**Target Audience:** A project manager who needs to understand the implications for the project timeline.

**Technical Text to Translate:**

"We need to refactor the authentication service. The current implementation uses a monolithic architecture, which is tightly coupled with the user database. We plan to migrate to a microservices architecture using OAuth 2.0 and JWTs for stateless authentication. This will improve scalability and allow for more granular control over service access, but it will require a full regression test of all dependent services."
````

## Documentation

### Why this prompt is effective:

1.  **Audience-Centric:** It forces the AI to tailor the explanation to a specific `Target Audience`. Explaining something to a CEO is different from explaining it to a customer, and this prompt makes that distinction clear.
2.  **Clear, Actionable Rules:** The "Translation Rules" provide a concrete set of instructions for the AI to follow. Rules like "No Jargon" and "Focus on the 'What' and 'Why'" are explicit and effective.
3.  **Emphasis on Analogy:** Starting with an analogy is a powerful way to introduce a new or complex topic. The prompt makes this a mandatory first step.
4.  **Practical Persona:** "The Simplifier" is a highly practical persona that immediately frames the task in terms of clarity and accessibility.
5.  **Structured Output:** Requiring a structured format (headings, bullet points) ensures the final output is not a wall of text, but a readable and scannable document.

### How to use it:

1.  Define your `Target Audience` as precisely as possible. This is the most important input for this prompt.
2.  Paste the `Technical Text to Translate`.
3.  This prompt is invaluable for engineers who need to communicate with business stakeholders, for marketers who need to write copy about a technical product, for project managers who need to understand the work their team is doing, or for anyone who has ever read a technical document and felt completely lost.
