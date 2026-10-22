"""Task 3: named constants, dynamic typing, multiple assignment."""
BASE_RATE = 30.00
STD_FAT = 3.5
STD_SNF = 8.5
STEP = 0.1
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
MIN_FAT, MAX_FAT = 2.0, 7.0
MIN_SNF, MAX_SNF = 7.0, 10.0
PAYMENT_CYCLE_DAYS = 10

# Alternative: dictionary rate card
RATE_CARD = {"base": 30.0, "fat": 0.40, "snf": 0.30}

# Python does not enforce constants:
BASE_RATE = 31.0            # legal! only the UPPER_CASE convention warns readers
print("BASE_RATE accidentally changed to", BASE_RATE)
BASE_RATE = 30.00

# Dynamic typing
x = 5
print(x, type(x))
x = "five"
print(x, type(x))

# Multiple assignment and swap
a, b = 3, 7
a, b = b, a
print("after swap:", a, b)
fat = snf = 0.0
print(fat, snf)

# Three ways to compute a rate
rate_magic = 30.0 + 7 * 0.40 + 2 * 0.30                      # magic numbers
rate_const = BASE_RATE + 7 * FAT_STEP_VALUE + 2 * SNF_STEP_VALUE
rate_dict = RATE_CARD["base"] + 7 * RATE_CARD["fat"] + 2 * RATE_CARD["snf"]
print(rate_magic, rate_const, rate_dict)
