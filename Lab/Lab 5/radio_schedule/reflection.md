# Reflection

The provided handout refers to four reflection questions but does not include their wording. These responses address the lab's stated learning outcomes.

1. **What is static code analysis, and how did it help?**
   Static analysis examines source code without running it. Pylint highlighted quality and correctness problems, Flake8 reported formatting issues, and Bandit identified risky coding patterns. Together they helped prioritize changes before relying on runtime behavior alone.

2. **Which issue was most important, and why?**
   The use of `eval` was the most serious because a value passed to the function could execute arbitrary Python code. Replacing it with a numeric comparison removed code execution while retaining the intended overlap check.

3. **How did the fixes improve the program?**
   Parameterized SQL prevents show and host values from changing the query. Removing global state makes the database lifecycle explicit. Input validation rejects invalid hours and durations, and removing the unused password avoids publishing a secret in source.

4. **What are the limitations of static analysis, and what did you learn?**
   A clean report does not prove that program behavior is correct or that every security issue has been found. The tools needed context to distinguish important risks from style findings. I learned to use their reports as review guidance, apply fixes that preserve intended behavior, and then rerun the tools to verify the result.
