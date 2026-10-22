# Task 4 - Notes
* Precedence high -> low: `**`, unary `-`, `* / // %`, `+ -`, comparisons, `not`, `and`, `or`.
  `-2 ** 2 == -4` because ** binds tighter than unary minus. `**` is right-associative
  (2**3**2 = 512); other arithmetic operators are left-associative.
* (4.2-3.5)/0.1 prints 7.000000000000001 or 7.000000000000002 depending on the Python build/platform (this run: 7.000000000000002), since 4.2, 3.5 and 0.1 are inexact in binary.
  round() recovers the intended whole step count (7).
* round -> nearest (ties to even), int -> truncates toward 0, math.floor -> toward -infinity.
  For (3.1-3.5)/0.1 = -3.999999999999999 (this run): round=-4, floor=-4, but int=-3 (WRONG, Rs 0.40/litre error).
  If a value lands just below a negative whole number (e.g. -4.000000000000001), floor gives -5 (WRONG). round() is right in all cases.
  Unexpected results demonstrated: 7.00000000000000x, -3.99999999999999x, 0.1*3 = 0.30000000000000004, int() truncation (compare_steps_output.txt).
* `2.0 <= fat <= 7.0` is chained comparison = (2.0 <= fat) and (fat <= 7.0), fat evaluated once.
  Boolean operators `and`, `or`, `not` combine conditions.
* Complexity of round/int/floor: O(1) time, O(1) space.
