"""Task 9: automated test table. Run: python test_calculator.py"""
from calculator import process_entry, ten_day_total

# (description, litres, fat, snf, expected)  expected None = must be rejected
CASES = [
    ("above standard", "10", "4.2", "8.7", 334.00),
    ("below standard", "10", "3.1", "8.3", 278.00),
    ("standard 3.5/8.5", "10", "3.5", "8.5", 300.00),
    ("lowest fat 2.0", "10", "2.0", "8.5", 240.00),
    ("highest fat 7.0", "10", "7.0", "8.5", 440.00),
    ("invalid text litres", "eight", "3.5", "8.5", None),
    ("comma decimal fat", "10", "3,5", "8.5", None),
    ("negative litres", "-5", "3.5", "8.5", None),
    ("fat below range 1.9", "10", "1.9", "8.5", None),
    ("fat above range 7.1", "10", "7.1", "8.5", None),
    ("zero litres", "0", "3.5", "8.5", 0.0),
]

failures = 0
print(f"{'Case':22}{'Input':22}{'Expected':>10}{'Actual':>10}  Result")
for name, l, f, s, expected in CASES:
    actual = process_entry(l, f, s)
    ok = actual == expected
    failures += not ok
    print(f"{name:22}{(l+'/'+f+'/'+s):22}{str(expected):>10}{str(actual):>10}  {'PASS' if ok else 'FAIL'}")

# five-entry manual total
five = [("10", "3.5", "8.5"), ("8.5", "4.2", "8.7"), ("12", "3.1", "8.3"),
        ("20", "4.0", "8.5"), ("5", "3.0", "8.0")]
# Manual working: 300.00 + 283.90 + 333.60
#   entry 4: rate 30 + 5*0.4 = 32.00 -> 20 L = 640.00
#   entry 5: rate 30 - 5*0.4 - 5*0.3 = 26.50 -> 5 L = 132.50
manual = 300.00 + 283.90 + 333.60 + 640.00 + 132.50
actual = ten_day_total(five)
ok = abs(actual - manual) < 0.005
failures += not ok
print(f"{'five-entry total':22}{'(5 entries)':22}{manual:10.2f}{actual:10.2f}  {'PASS' if ok else 'FAIL'}")

# assert-based version (additional question)
assert process_entry("10", "3.5", "8.5") == 300.00
assert process_entry("-1", "3.5", "8.5") is None
print("Failures:", failures)
