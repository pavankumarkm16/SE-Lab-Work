# Static analysis issues

The original line numbers below refer to `Original Code.py` (the untouched repository starter file).

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Arbitrary code execution through `eval` | Security (medium) | 19-23 | Bandit reports the dynamic evaluation as B307. Evaluating caller-provided text as Python can execute code. | Replace expression evaluation with numeric inputs and a direct overlap calculation. |
| SQL injection through string interpolation | Security (medium) | 11 | Bandit reports B608 because show and host names are interpolated into SQL. | Use SQLite parameter placeholders and a tuple of values. |
| Hard-coded studio password | Security (low) | 5 | Bandit reports B105 for a credential stored in source even though the demonstration does not use it. | Remove the unused credential; load secrets from a protected configuration if needed later. |
| Global mutable database state | Maintainability | 3, 6, 10, 26-27 | Functions share a global connection and minutes counter, making behavior dependent on call history. | Create a connection in `main` and pass it explicitly to schedule operations. |
| Incorrect duration accounting after deletion | Bug | 6, 31-32 | Removing a slot does not subtract its duration, so the counter becomes stale. | Query the database for morning shows and remove the redundant counter. |
| Inconsistent naming and missing docstrings | Style | 9-35 | CamelCase function names and undocumented functions do not follow common Python conventions. | Use snake_case and add concise docstrings. |

## Verification summary

The final source uses parameterized SQL, contains no dynamic evaluation or embedded credential, validates slot data, and passes the demonstration and all three static analysis tools. See the after reports in this submission for the tool output.
