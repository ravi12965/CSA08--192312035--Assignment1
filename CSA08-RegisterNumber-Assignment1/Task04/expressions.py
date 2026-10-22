"""Task 4: expressions for steps, rate and payment."""
import math

BASE_RATE, FAT_STEP_VALUE, SNF_STEP_VALUE = 30.0, 0.40, 0.30
STD_FAT, STD_SNF, STEP = 3.5, 8.5, 0.1

def steps(value, standard):
    return round((value - standard) / STEP)

fat, snf, litres = 4.2, 8.7, 8.5
fat_steps = steps(fat, STD_FAT)
snf_steps = steps(snf, STD_SNF)
rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
print("fat steps", fat_steps, "snf steps", snf_steps)
print("rate", round(rate, 2), "payment", round(litres * rate, 2))

print("--- unexpected results ---")
print("(4.2 - 3.5) / 0.1 =", (4.2 - 3.5) / 0.1)
print("(3.1 - 3.5) / 0.1 =", (3.1 - 3.5) / 0.1)
print("int((8.2-8.5)/0.1) =", int((8.2 - 8.5) / 0.1), "(expected -3)")
print("math.floor((3.1-3.5)/0.1) =", math.floor((3.1 - 3.5) / 0.1), "(expected -4)")
print("0.1 * 3 =", 0.1 * 3)

print("--- precedence / associativity ---")
print("-2 ** 2 =", -2 ** 2, "  (-2) ** 2 =", (-2) ** 2)
print("2 ** 3 ** 2 =", 2 ** 3 ** 2, "(right-assoc)  vs (2**3)**2 =", (2 ** 3) ** 2)
print("10 - 4 - 3 =", 10 - 4 - 3, "(left-assoc)")
print("2 + 3 * 4 =", 2 + 3 * 4)

print("--- round vs int vs floor on negatives ---")
for v in (-2.5, -2.7, -3.5, 2.5):
    print(f"{v:5}: round={round(v):3} int={int(v):3} floor={math.floor(v):3}")

print("--- chained comparison ---")
for f in (1.9, 2.0, 4.2, 7.0, 7.1):
    print(f, 2.0 <= f <= 7.0, "| same as", (2.0 <= f) and (f <= 7.0))
