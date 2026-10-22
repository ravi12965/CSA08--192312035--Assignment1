"""Task 12: seasonal rate cards, 2-decimal analyser readings, ten-day bonus.
Money and readings use Decimal so fractional steps stay exact."""
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
STEP = Decimal("0.1")
STD_FAT, STD_SNF = Decimal("3.5"), Decimal("8.5")
MIN_FAT, MAX_FAT = Decimal("2.0"), Decimal("7.0")
MIN_SNF, MAX_SNF = Decimal("7.0"), Decimal("10.0")
BONUS_THRESHOLD_LITRES = Decimal("500")
BONUS_PER_LITRE = Decimal("0.50")

RATE_CARDS = {
    "normal": {"base": Decimal("30.00"), "fat_step": Decimal("0.40"), "snf_step": Decimal("0.30")},
    "summer": {"base": Decimal("32.00"), "fat_step": Decimal("0.45"), "snf_step": Decimal("0.30")},
}
SEASON_BY_MONTH = {4: "summer", 5: "summer", 6: "summer"}     # April-June


def season_for_month(month):
    """Return 'summer' for April-June, otherwise 'normal'."""
    return SEASON_BY_MONTH.get(month, "normal")


def money(value):
    """Round a Decimal to paise (ROUND_HALF_UP)."""
    return value.quantize(CENT, ROUND_HALF_UP)


def validate(litres, fat, snf):
    """Raise ValueError for invalid readings."""
    if litres < 0:
        raise ValueError("litres cannot be negative")
    if not MIN_FAT <= fat <= MAX_FAT:
        raise ValueError("fat out of range")
    if not MIN_SNF <= snf <= MAX_SNF:
        raise ValueError("snf out of range")


def rate_per_litre(fat, snf, season="normal"):
    """Rate per litre; steps are FRACTIONAL (2-decimal readings), not rounded away."""
    card = RATE_CARDS[season]
    fat_steps = (Decimal(fat) - STD_FAT) / STEP          # e.g. 4.27 -> 7.7 steps
    snf_steps = (Decimal(snf) - STD_SNF) / STEP
    rate = card["base"] + fat_steps * card["fat_step"] + snf_steps * card["snf_step"]
    return money(rate)


def payout(litres, fat, snf, season="normal"):
    """Payment for one delivery (without bonus)."""
    litres, fat, snf = Decimal(litres), Decimal(fat), Decimal(snf)
    validate(litres, fat, snf)
    return money(litres * rate_per_litre(fat, snf, season))


def bonus(total_litres):
    """Rs 0.50 per litre on ALL litres if the ten-day supply exceeds 500 litres."""
    total_litres = Decimal(total_litres)
    if total_litres > BONUS_THRESHOLD_LITRES:
        return money(total_litres * BONUS_PER_LITRE)
    return Decimal("0.00")


def ten_day_total(entries, season="normal"):
    """entries: list of (litres, fat, snf) strings. Returns (payments, bonus, total)."""
    payments = Decimal("0.00")
    litres_sum = Decimal("0")
    for litres, fat, snf in entries:
        payments += payout(litres, fat, snf, season)
        litres_sum += Decimal(litres)
    b = bonus(litres_sum)
    return payments, b, payments + b


if __name__ == "__main__":
    print("fat 4.27 snf 8.73 normal :", rate_per_litre("4.27", "8.73", "normal"))
    print("fat 4.27 snf 8.73 summer :", rate_per_litre("4.27", "8.73", "summer"))
    print("old rounded-step method would give 30 + 8*0.40 + 2*0.30 =", 30 + 8*0.40 + 2*0.30)
    print("season for month 5:", season_for_month(5), "| month 9:", season_for_month(9))
