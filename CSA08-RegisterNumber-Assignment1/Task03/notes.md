# Task 3 - Notes
Python has no `const` keyword; any name can be re-assigned. UPPER_CASE is a convention
(PEP 8) telling programmers "do not change this"; linters can flag re-assignment.

| Approach | Places to edit for a rate revision | Runtime / memory |
|---|---|---|
| Magic numbers | every expression using the value (easy to miss one -> the "incorrect totals" bug) | negligible |
| Named constants | exactly 1 line | O(1) |
| Dict RATE_CARD | 1 line; dict can be swapped per season / loaded from JSON | one O(1) lookup per use, a few hundred bytes |
Differences in speed and memory are insignificant; maintainability is the real gain.
Named constants are used for the base design; a dict rate card is used for seasons (Task 12).
