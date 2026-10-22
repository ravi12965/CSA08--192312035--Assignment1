"""Task 2 additional question: Decimal vs integer paise vs float+round."""
import sys, time
from decimal import Decimal

payments = ["33.40"] * 1000 + ["0.10"] * 3

def with_decimal():
    t = Decimal("0")
    for a in payments:
        t += Decimal(a)
    return t

def with_paise():
    t = 0                                   # integer paise
    for a in payments:
        t += round(float(a) * 100)          # convert once to paise
    return t / 100, t                       # rupees for display, paise exact

def with_float_round():
    t = 0.0
    for a in payments:
        t = round(t + float(a), 2)          # round after every addition
    return t

for name, fn in (("Decimal", with_decimal), ("int paise", with_paise),
                 ("float+round", with_float_round)):
    s = time.perf_counter(); r = fn(); e = time.perf_counter() - s
    print(f"{name:12} result={r}  time={e*1000:.3f} ms")

print("sizeof(float)      =", sys.getsizeof(1.5))
print("sizeof(int paise)  =", sys.getsizeof(3340))
print("sizeof(Decimal)    =", sys.getsizeof(Decimal("33.40")))
