# Task 6 - Notes
* return gives a value back to the caller (reusable, testable); print only shows text and
  the function then returns None.
* Local variables exist only inside the function; global ones live at module level.
  Functions can READ globals (rate constants) without `global`. Assigning inside a function
  creates a new local unless `global` is declared - avoid modifying constants (hidden side
  effects, hard to debug).
* One long script = repeated logic, O(n) lines; functions = write once, reuse, test;
  lambda = short anonymous function, good for sort keys, poor for docstrings/debugging.
  Function-call overhead is ~0.1 microsecond per call: O(1) per entry, O(n) overall, negligible
  compared with the maintainability gains.
