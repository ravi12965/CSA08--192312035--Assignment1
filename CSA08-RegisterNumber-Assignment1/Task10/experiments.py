"""Task 10: float vs Decimal totals, timing, rounding strategy, rate table."""
import random, time, timeit
from decimal import Decimal, ROUND_HALF_UP

random.seed(42)
CENT = Decimal("0.01")

def make_payments(n):
    """n unrounded payments as Decimal strings: litres(1 dp) x rate(2 dp) -> 3 dp."""
    out = []
    for _ in range(n):
        litres = Decimal(random.randint(10, 400)) / 10          # 1.0 .. 40.0
        rate = Decimal(random.randint(2500, 3800)) / 100        # 25.00 .. 38.00
        out.append(litres * rate)                               # exact, 3 decimals
    return out

print(f"{'n':>8} {'float total':>20} {'Decimal total':>16} {'float time ms':>14} {'Decimal time ms':>16}")
for n in (300, 6000, 150000):
    pays = make_payments(n)
    strs = [str(p) for p in pays]
    t0 = time.perf_counter(); f = 0.0
    for s in strs: f += float(s)
    tf = (time.perf_counter() - t0) * 1000
    t0 = time.perf_counter(); d = Decimal("0")
    for s in strs: d += Decimal(s)
    td = (time.perf_counter() - t0) * 1000
    print(f"{n:8} {f:20.10f} {d:16} {tf:14.3f} {td:16.3f}")

print("\n--- Rounding each payment vs rounding only the final total ---")
print(f"{'n':>8} {'exact total':>14} {'round total':>13} {'sum of rounded':>15} {'difference':>11}")
for n in (300, 6000, 150000):
    pays = make_payments(n)
    exact = sum(pays, Decimal("0"))
    final_round = exact.quantize(CENT, ROUND_HALF_UP)
    each_round = sum((p.quantize(CENT, ROUND_HALF_UP) for p in pays), Decimal("0"))
    print(f"{n:8} {exact:14} {final_round:13} {each_round:15} {each_round - final_round:11}")
print("Farmers are paid the ROUNDED amount of each slip, so summing rounded payments is the")
print("amount the bank must actually transfer; rounding only the final total would not match slips.")

print("\n--- Rate table (dict) vs recalculation ---")
def rate(fat, snf):
    return round(30.0 + round((fat - 3.5) / 0.1) * 0.40 + round((snf - 8.5) / 0.1) * 0.30, 2)

fats = [round(2.0 + i * 0.1, 1) for i in range(51)]        # 51 values
snfs = [round(7.0 + i * 0.1, 1) for i in range(31)]        # 31 values
table = {(f, s): rate(f, s) for f in fats for s in snfs}   # k = 1581 pairs
pairs = [(random.choice(fats), random.choice(snfs)) for _ in range(150000)]

t_calc = timeit.timeit(lambda: [rate(f, s) for f, s in pairs], number=3) / 3
t_look = timeit.timeit(lambda: [table[p] for p in pairs], number=3) / 3
print(f"k distinct pairs = {len(table)}")
print(f"recalculate 150000 entries: {t_calc*1000:8.2f} ms  ({t_calc/150000*1e9:6.0f} ns/entry)")
print(f"dictionary lookup         : {t_look*1000:8.2f} ms  ({t_look/150000*1e9:6.0f} ns/entry)")
import sys
print("table memory approx (dict only):", sys.getsizeof(table), "bytes; space O(k)")
