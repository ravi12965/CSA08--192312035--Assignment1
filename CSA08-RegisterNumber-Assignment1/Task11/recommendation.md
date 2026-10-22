# Task 11 - Recommended Final Design

## 1. Data types and rounding
* Money, rates, litres, fat, SNF -> `decimal.Decimal` built from strings (never from floats).
  Task 2 showed float drifted to 33400.30000000061; Decimal gave exactly 33400.30.
* Round each farmer's payment to 0.01 with ROUND_HALF_UP (what a bank slip shows).
  Task 10 showed rounding each payment differs from rounding the total by Rs 69.06 at 150,000
  entries, so the bank transfer must equal the sum of printed (rounded) slips.
* Step counts: whole integers via rounding (Task 4 shows int/floor cause wrong steps).
* IDs, shift: str. Validation flags: bool.

## 2. Safe rate revision
Keep all rates in one rate card (module constants, or rates.json). Change in one place,
keep old versions with an effective date (Git history / dated file), run the automated
tests (Task 9) after each change, and apply a revised card only to entries from its effective date.

## 3. Limitations
* Rates are assumed linear and fixed-step; no per-day pricing or bonus rules (see Task 12).
* No database, authentication, audit log, concurrency; input comes from a clerk at a keyboard.
* Decimal is ~2x slower than float (Task 10: 34 ms vs 18 ms for 150,000 additions).
* SNF range 7.0-10.0 is an assumption.

## 4. Scale: 150,000 farmers
Time is O(n): the measured Decimal summation of 150,000 payments took ~34 ms, and recalculating
150,000 rates took ~84 ms (13 ms using a rate table). Memory O(n) for stored entries, O(1) with a
running total. Even x20 entries per ten-day cycle (3 million) would run in seconds. The design
scales; the real bottleneck would be human data entry and storage (use files/DB), not computation.

## 5. Evidence summary
| Claim | Evidence |
|---|---|
| Float is unsafe | Task 2 output |
| Decimal is exact and affordable | Task 10 times |
| Per-payment rounding matters | Task 10 rounding table |
| Rate table speeds lookups ~6x | Task 10 dictionary test, extra space O(k) ~74 KB for k=1581 |

## Additional question: rate card in a text/JSON file
Program reads the file once at start-up (`json.load`), converts t values to Decimal.
Start-up time O(t) - microseconds for 5 values (see final_design.py output); space O(t).
Maintenance: a rate revision means editing the file only - no code change, no
redistribution of the program, so less risk of introducing a bug; risks: malformed/missing
file, so validate on load. Constants in code need code edits and a new release for every
revision but have no file-loading failure modes.
