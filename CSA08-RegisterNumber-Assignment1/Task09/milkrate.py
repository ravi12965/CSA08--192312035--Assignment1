"""Rate card of the village milk co-operative."""

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
STD_FAT = 3.5
STD_SNF = 8.5
STEP = 0.1


def rate_per_litre(fat, snf):
    """Return the price per litre, rounded to two decimals."""
    fat_steps = round((fat - STD_FAT) / STEP)     # nearest whole 0.1 % step
    snf_steps = round((snf - STD_SNF) / STEP)
    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    return round(rate, 2)


def payout(litres, fat, snf):
    """Return the payment amount rounded to two decimals."""
    return round(litres * rate_per_litre(fat, snf), 2)


if __name__ == "__main__":
    for litres, fat, snf in [
        (10, 3.5, 8.5),
        (8.5, 4.2, 8.7),
        (12, 3.1, 8.3)
    ]:
        rate = rate_per_litre(fat, snf)
        pay = payout(litres, fat, snf)
        print(
            f"{litres:5} L fat {fat} snf {snf}"
            f" rate {rate:6.2f} pay {pay:8.2f}"
        )
