"""Task 9: complete milk payment calculator with validation."""
from milkrate import payout, rate_per_litre

MIN_FAT, MAX_FAT = 2.0, 7.0
MIN_SNF, MAX_SNF = 7.0, 10.0


def parse_float(text):
    """Convert text to float; raise ValueError for bad text (incl. nan/inf)."""
    value = float(text)                       # raises ValueError for "eight", "8,5"
    if value != value or value in (float("inf"), float("-inf")):
        raise ValueError("number must be finite")
    return value


def validate_entry(litres_text, fat_text, snf_text):
    """Return (litres, fat, snf) as floats or raise ValueError with a message."""
    litres = parse_float(litres_text)
    fat = parse_float(fat_text)
    snf = parse_float(snf_text)
    if litres < 0:
        raise ValueError("litres cannot be negative")
    if not MIN_FAT <= fat <= MAX_FAT:
        raise ValueError(f"fat must be between {MIN_FAT} and {MAX_FAT}")
    if not MIN_SNF <= snf <= MAX_SNF:
        raise ValueError(f"snf must be between {MIN_SNF} and {MAX_SNF}")
    return litres, fat, snf


def process_entry(litres_text, fat_text, snf_text):
    """Validate and return the payment, or None with a printed error."""
    try:
        litres, fat, snf = validate_entry(litres_text, fat_text, snf_text)
    except ValueError as err:
        print("  Rejected:", err)
        return None
    return payout(litres, fat, snf)


def ten_day_total(entries):
    """Sum payments of valid (litres, fat, snf) text entries."""
    total = 0.0
    for litres, fat, snf in entries:
        pay = process_entry(litres, fat, snf)
        if pay is not None:
            total += pay
    return round(total, 2)


def main():
    print("Ksheera Milk Co-operative - payment calculator (blank litres to finish)")
    entries = []
    while True:
        litres = input("Litres: ").strip()
        if litres == "":
            break
        fat = input("Fat %: ")
        snf = input("SNF %: ")
        pay = process_entry(litres, fat, snf)
        if pay is not None:
            print(f"  Rate {rate_per_litre(float(fat), float(snf)):6.2f}  Payment {pay:8.2f}")
            entries.append((litres, fat, snf))
    print(f"Ten-day total: {ten_day_total(entries):10.2f}")


if __name__ == "__main__":
    main()
