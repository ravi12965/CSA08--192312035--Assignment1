"""Task 12 tests: original and seasonal rates, with and without bonus."""
from decimal import Decimal as D
from seasonal import rate_per_litre, payout, bonus, ten_day_total, season_for_month

def check(name, actual, expected):
    ok = actual == D(expected)
    print(f"{name:55} expected {expected:>10} actual {str(actual):>10}  {'PASS' if ok else 'FAIL'}")
    return ok

results = []
# original behaviour retained (one-decimal readings, normal season)
results.append(check("normal 3.5/8.5 rate", rate_per_litre("3.5", "8.5"), "30.00"))
results.append(check("normal 4.2/8.7 rate (original example)", rate_per_litre("4.2", "8.7"), "33.40"))
results.append(check("normal 8.5 L 4.2/8.7 payout", payout("8.5", "4.2", "8.7"), "283.90"))
# two-decimal readings: 4.27 -> 7.7 steps*0.40=3.08 ; 8.73 -> 2.3 steps*0.30=0.69
results.append(check("normal 4.27/8.73 rate", rate_per_litre("4.27", "8.73"), "33.77"))
# summer: base 32, fat step 0.45: 4.27 -> 32 + 7.7*0.45(=3.465) + 0.69 = 36.155 -> 36.16
results.append(check("summer 4.27/8.73 rate", rate_per_litre("4.27", "8.73", "summer"), "36.16"))
results.append(check("summer standard milk 3.5/8.5 rate", rate_per_litre("3.5", "8.5", "summer"), "32.00"))
# bonus
results.append(check("bonus 500 L (not more than 500)", bonus("500"), "0.00"))
results.append(check("bonus 500.5 L", bonus("500.5"), "250.25"))
# ten-day: normal season, no bonus: 20 deliveries x 20 L = 400 L at 30.00 -> 12000.00
entries_400 = [("20", "3.5", "8.5")] * 20
results.append(check("normal, 400 L, no bonus total", ten_day_total(entries_400, "normal")[2], "12000.00"))
# normal season with bonus: 20 x 30 L = 600 L -> 18000 + 300 bonus
entries_600 = [("30", "3.5", "8.5")] * 20
results.append(check("normal, 600 L, with bonus total", ten_day_total(entries_600, "normal")[2], "18300.00"))
# summer without bonus: 400 L x 32 = 12800
results.append(check("summer, 400 L, no bonus total", ten_day_total(entries_400, "summer")[2], "12800.00"))
# summer with bonus: 600 L x 32 = 19200 + 300
results.append(check("summer, 600 L, with bonus total", ten_day_total(entries_600, "summer")[2], "19500.00"))
# season selection
results.append(season_for_month(4) == "summer" and season_for_month(6) == "summer"
               and season_for_month(7) == "normal" and season_for_month(3) == "normal")
print("season_for_month boundaries (Mar, Apr, Jun, Jul):", results[-1])
# validation
try:
    payout("10", "7.01", "8.5"); results.append(False)
except ValueError:
    results.append(True); print("fat 7.01 rejected: PASS")
print("ALL PASSED" if all(results) else "SOME FAILED")
