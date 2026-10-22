"""Task 6: reusable functions with docstrings."""
BASE_RATE, FAT_STEP_VALUE, SNF_STEP_VALUE = 30.00, 0.40, 0.30
STD_FAT, STD_SNF, STEP = 3.5, 8.5, 0.1

def rate_per_litre(fat, snf):
    """Return the price per litre for the given fat and SNF percentages."""
    fat_steps = round((fat - STD_FAT) / STEP)   # reads global constants
    snf_steps = round((snf - STD_SNF) / STEP)
    return round(BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE, 2)

def payout(litres, fat, snf):
    """Return the payment for `litres` of milk with the given quality."""
    return round(litres * rate_per_litre(fat, snf), 2)

def ten_day_total(entries):
    """Return the total payment for a list of (litres, fat, snf) entries."""
    total = 0.0                                  # local variable
    for litres, fat, snf in entries:
        total += payout(litres, fat, snf)
    return round(total, 2)

def print_vs_return():
    value_returned = payout(10, 3.5, 8.5)        # can be reused
    value_printed = print("printing:", payout(10, 3.5, 8.5))   # returns None
    print("returned value reusable:", value_returned * 2)
    print("print() gives back:", value_printed)

counter = 0
def scope_demo():
    counter = 99                                 # local; hides global
    return counter

if __name__ == "__main__":
    entries = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]
    print("rate:", rate_per_litre(4.2, 8.7))
    print("ten-day total:", ten_day_total(entries))
    print_vs_return()
    print("local:", scope_demo(), "global:", counter)
    rate_lambda = lambda f, s: round(BASE_RATE + round((f-STD_FAT)/STEP)*FAT_STEP_VALUE
                                     + round((s-STD_SNF)/STEP)*SNF_STEP_VALUE, 2)
    print("lambda rate:", rate_lambda(4.2, 8.7))
