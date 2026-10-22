"""Second script: imports milkrate and calls payout()."""
import milkrate as mr
from milkrate import payout
import sys

print("payout via mr.payout   :", mr.payout(8.5, 4.2, 8.7))
print("payout via from-import :", payout(12, 3.1, 8.3))
print("milkrate cached in sys.modules:", "milkrate" in sys.modules)
print("module name when imported:", mr.__name__)
