# Task 1 - Understand the Problem and Identify the Data

## Inputs
| Input | Python type | Example | Validation rule |
|---|---|---|---|
| Farmer ID | str | "F0123" | non-empty, no spaces |
| Litres | float | 8.5 | >= 0 (0 allowed = no milk) |
| Fat % | float | 4.2 | 2.0 <= fat <= 7.0 |
| SNF % | float | 8.7 | 7.0 <= snf <= 10.0 (assumption) |
| Shift | str | "M" / "E" | must be morning or evening |

## Outputs
| Output | Type | Meaning |
|---|---|---|
| Rate per litre | float (Decimal in final design) | BASE + fat adj + SNF adj |
| Payment amount | float / Decimal | litres x rate, 2 decimals |
| Ten-day total | float / Decimal | sum of payments in a 10-day cycle |

## Named constants
BASE_RATE = 30.00, STD_FAT = 3.5, STD_SNF = 8.5, STEP = 0.1,
FAT_STEP_VALUE = 0.40, SNF_STEP_VALUE = 0.30, MIN_FAT = 2.0, MAX_FAT = 7.0,
MIN_SNF = 7.0, MAX_SNF = 10.0, PAYMENT_CYCLE_DAYS = 10, SHIFTS_PER_DAY = 2.

## Data-type classification
- int: PAYMENT_CYCLE_DAYS, SHIFTS_PER_DAY, number of fat/SNF steps
- float: litres, fat, snf, rates (money should become Decimal, see Task 2)
- bool: result of validation (is_valid)
- str: farmer ID, shift

## Assumptions (with justification)
1. SNF valid range is 7.0-10.0 % (assignment gives only the fat range; milk SNF lies in this band).
2. Steps are counted in whole 0.1 % units, using round() to remove float noise (Task 4).
3. Money is rounded to 2 decimals (paise) per payment.
4. A ten-day cycle has 10 days x 2 shifts = 20 entries per farmer maximum.
5. Litres = 0 is valid (farmer supplied nothing), negative is invalid.

## Additional Question - separate variables vs list/tuple (n = 300)
Separate variables (litres1, fat1, snf1, litres2 ...) need 3 x 300 = 900 variable
names written by hand; loops are impossible, so the code must be repeated for each
farmer, and adding a farmer means editing the program.
A list of tuples `[(litres, fat, snf), ...]` is processed by ONE loop.

| | Separate variables | List of tuples |
|---|---|---|
| Time to process n entries | O(n) (n copy-pasted statements) | O(n) (one loop) |
| Space | O(n) | O(n) |
| Code size | O(n) lines | O(1) lines |
| Scalability | Not scalable (6,000 / 150,000 impossible to write) | Scales; data can come from a file |

Both are O(n) in running time and memory, but the list approach is far more
scalable because code size is constant and the data is separate from the logic.
