
# Chain of Thought (CoT) Prompt: The Logical Problem Solver

Chain of Thought (CoT) prompting guides the AI to break down a problem into a series of intermediate steps before arriving at a final answer. This mimics human reasoning and significantly improves performance on tasks requiring logic, math, and complex reasoning.

## The Prompt

```
**Objective:** Solve the following problem by thinking step-by-step. Your reasoning process is more important than the final answer.

**Problem:** [**Insert the complex problem here.**]

**Example Problem:** "A grocery store has a special offer: buy 3 apples and get 1 free. If a single apple costs $0.50, and you need 10 apples, how much will you have to pay?"

**Instructions:**

1.  **Deconstruct the Problem:** First, break the problem down into smaller, manageable sub-questions. Identify the key pieces of information and the goal.
2.  **Think Step-by-Step:** Address each sub-question sequentially. Show your work and explain your reasoning for each step. Do not perform calculations in your head; write them down.
3.  **Intermediate Conclusions:** State the conclusion of each step clearly.
4.  **Synthesize the Final Answer:** Once you have worked through all the steps, combine your intermediate conclusions to formulate the final answer.
5.  **Final Answer Formulation:** Present the final answer clearly and concisely, starting with "The final answer is:".

---

**(User provides their problem below this line)**

**Problem:** You are building a fence around a rectangular garden. The garden is 10 feet long and 5 feet wide. The fence posts need to be placed every 2.5 feet. How many fence posts do you need?
```

## Documentation

### Why this prompt is effective:

1.  **Explicit Instruction to "Think Step-by-Step":** The prompt's core instruction is to externalize the reasoning process. This is the fundamental principle of CoT.
2.  **Deconstruction Phase:** It forces the AI to first analyze and understand the problem before attempting to solve it. This prevents it from jumping to incorrect conclusions.
3.  **Sequential Reasoning:** The prompt enforces a logical flow, where each step builds upon the previous one. This structured approach reduces the likelihood of errors.
4.  **Showing Work:** By requiring the AI to "show its work," you can trace its logic and identify where it might have gone wrong. This is invaluable for debugging both the AI's reasoning and your own prompt.
5.  **Clear Separation of Reasoning and Answer:** The prompt structure separates the step-by-step thinking process from the final, clean answer. This makes the output highly readable and useful.

### How to use it:

1.  Replace the example problem with your own complex question or problem.
2.  The problem can be mathematical, logical, a riddle, or any task that requires multiple steps to solve.
3.  The AI will output a detailed, step-by-step breakdown of its thought process, followed by the final, synthesized answer. This allows you to verify its logic and trust the result.
