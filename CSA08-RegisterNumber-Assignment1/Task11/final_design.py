"""Task 11: recommended design - Decimal money + rate card loaded from JSON."""
import json, time
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
STEP = Decimal("0.1")

def load_rate_card(path="rates.json"):
    """Read the rate card once at start-up; values stay as Decimal."""
    with open(path) as f:
        raw = json.load(f)
    return {k: Decimal(v) for k, v in raw.items()}

def rate_per_litre(card, fat, snf):
    fat_steps = ((Decimal(fat) - card["std_fat"]) / STEP).to_integral_value()
    snf_steps = ((Decimal(snf) - card["std_snf"]) / STEP).to_integral_value()
    rate = card["base_rate"] + fat_steps * card["fat_step_value"] + snf_steps * card["snf_step_value"]
    return rate.quantize(CENT, ROUND_HALF_UP)

def payout(card, litres, fat, snf):
    return (Decimal(litres) * rate_per_litre(card, fat, snf)).quantize(CENT, ROUND_HALF_UP)

if __name__ == "__main__":
    t0 = time.perf_counter()
    card = load_rate_card()
    print(f"rate card loaded in {(time.perf_counter()-t0)*1e6:.0f} microseconds:", card)
    print(payout(card, "10", "3.5", "8.5"), payout(card, "8.5", "4.2", "8.7"), payout(card, "12", "3.1", "8.3"))
