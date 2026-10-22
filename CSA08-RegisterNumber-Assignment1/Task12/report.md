# Task 12 - Day-4 Design Challenge

## A. Impact analysis
**Changed:** (1) readings now have 2 decimals; (2) April-June has a different base rate (32.00)
and fat step (0.45); (3) a bonus of Rs 0.50/litre applies when ten-day litres exceed 500.
**Must change:**
* Constants - single BASE_RATE / FAT_STEP_VALUE become a rate card per season.
* Expressions - `round((fat-3.5)/0.1)` must no longer be rounded to whole steps.
* Functions - `rate_per_litre`/`payout` need a `season` parameter; new `bonus()`;
  `ten_day_total` must add the bonus (it needs total litres for the cycle).
**Two-decimal readings:** fat 4.27 is 7.7 steps above 3.5. Rounding to 8 steps would
overpay 0.3 x 0.40 = Rs 0.12/litre; truncating to 7 would underpay Rs 0.28/litre. Steps must be
fractional, which in float causes drift (e.g. 4.27-3.5 gives a value like 0.7699999999999996 instead of 0.77), so Decimal is used and
rounding happens only once, at the rate in paise.

## B. Evaluation of the original design
| Part | Verdict |
|---|---|
| Module structure (rate card + functions) | Retain - good separation |
| Named constants | Modify - need seasonal cards (dict of cards) |
| round() steps | Wrong for 2-decimal data: 4.27/8.73 -> 8 and 2 steps = 33.80 instead of the correct 33.77 |
| float | Replace by Decimal because fractional steps magnify float error |
| ten_day_total | Modify - must compute litres and bonus |
| Validation | Retain, still valid (fat 2.0-7.0, litres >= 0) |
Worked example, fat 4.27, snf 8.73, normal: original code -> 30 + 8*0.40 + 2*0.30 = 33.80;
new code -> 30 + 7.7*0.40 + 2.3*0.30 = 33.77. Summer: 32 + 7.7*0.45 + 0.69 = 36.155 -> 36.16.

## C. Adaptation (see seasonal.py)
* `RATE_CARDS = {"normal": {...}, "summer": {...}}` and `season_for_month(month)`.
* `rate_per_litre(fat, snf, season)` uses the chosen card with fractional steps in Decimal.
* `bonus(total_litres)` separate function; `ten_day_total` adds it.
* Rounding rule: round each payment to paise (ROUND_HALF_UP); bonus rounded separately.

## D. Defence
**Decision: MODIFY (not redesign).** Module layout, function names, validation, per-payment
rounding all survive; only the rate representation, step calculation and total function change.
A full redesign is not justified because requirements changed in parameters/rules, not in structure.
**Evidence:** test_seasonal.py covers original rates, summer rates, with/without bonus, boundary
(500 L gives no bonus, 500.5 L gives a bonus), month boundaries and invalid fat; all pass (see output.txt).
**Trade-offs:** Decimal is slower than float (Task 10, about 2x) but exactness matters for money and
the volumes are small; a rate-card dict is slightly more complex than two constants but supports
future seasons without code changes; bonus on all litres (not only the excess over 500) is an interpretation
of "more than 500 litres ... bonus of Rs 0.50 per litre" - state this assumption in your report.
