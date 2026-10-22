# Task 5 - Notes
* input() returns str because the terminal delivers text; the program cannot know intent.
* Validation approaches:

| Input | String methods (isdigit etc.) | try/except float() |
|---|---|---|
| "8,5" | rejected (comma) | ValueError -> rejected |
| " 8.5 " | rejected unless strip() used | accepted (float ignores outer spaces) |
| "eight" | rejected | ValueError -> rejected |
| "-1", "1e3", "inf" | tricky (isdigit fails) | accepted by float (inf/nan need extra checks!) |

Both are O(L) for string length L (O(1) per entry in practice). try/except is shorter and
more reliable (EAFP); string checks need many special cases. Best: try/except, then range
checks (and math.isfinite).
