"""Task 2: values, types, arithmetic, floating-point problem, Decimal."""
from decimal import Decimal

print("--- type() of values ---")
for v in (10, 10.0, "10", True, [10, 8.5]):
    print(f"{v!r:10} -> {type(v)}")

print("--- division operators ---")
print("7 / 2   =", 7 / 2)      # 3.5  true division
print("7 // 2  =", 7 // 2)     # 3    floor division
print("7 % 2   =", 7 % 2)      # 1    remainder
print("-7 // 2 =", -7 // 2)    # -4   floors toward minus infinity

print("--- 0.1 + 0.2 ---")
print(0.1 + 0.2, 0.1 + 0.2 == 0.3)

# 1,000 payments of Rs 33.40 and three adjustments of Rs 0.10
payments = ["33.40"] * 1000 + ["0.10"] * 3

def total_float(items):
    total = 0.0
    for amount in items:
        total += float(amount)
    return total

def total_decimal(items):
    """TODO 1 solved: add the amounts exactly using Decimal."""
    total = Decimal("0")
    for amount in items:
        total += Decimal(amount)       # Decimal built from the STRING
    return total

def total_decimal_from_float(items):
    """Variant: Decimal(float(amount)) - inherits the binary error."""
    total = Decimal("0")
    for amount in items:
        total += Decimal(float(amount))
    return total

print("float  :", total_float(payments))
print("Decimal:", total_decimal(payments))
print(0.1 + 0.2 == 0.3, Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
print("Decimal(float(amount)):", total_decimal_from_float(payments))
print("Decimal(float('33.40')) =", Decimal(float("33.40")))
