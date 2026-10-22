# Task 2 - Notes

## Why 0.1 + 0.2 == 0.3 is False
Floats are stored in binary (base 2). 0.1 and 0.2 have infinite binary expansions, so
they are stored as the nearest representable value. Their sum is 0.30000000000000004,
which is not the same double as 0.3. Decimal stores base-10 digits so the test is True.

## Why float is dangerous for money
Every addition may add a tiny representation error (about 1e-16 relative). Over thousands
of payments the error accumulates (33400.30000000061 instead of 33400.30). Equality
checks and rounding (e.g. round(2.675, 2) -> 2.67) also behave unexpectedly.

## Decimal(amount) vs Decimal(float(amount))
Decimal("33.40") is exactly 33.40. Decimal(float("33.40")) is the exact value of the
binary double nearest 33.40 (33.39999999999999857891452847979962825775146484375).
Summing these gives a total slightly off 33400.30, so Decimal's exactness is lost.
Rule: always build Decimal from strings (or ints).

## Comparison (money handling)
| Method | Exact? | Time per add | Memory | Notes |
|---|---|---|---|---|
| Decimal | Yes | O(1) (slower constant) | ~100+ bytes | rounding modes, best readability |
| Integer paise | Yes | O(1) fastest | ~28 bytes | must convert/format yourself |
| float + round after each add | Not guaranteed | O(1) | 24 bytes | hides but cannot remove error |
Use the real numbers from approaches_output.txt in your report.
