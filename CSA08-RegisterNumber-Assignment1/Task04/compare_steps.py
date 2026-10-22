"""Task 4 additional: round vs int vs floor for 4.2 and 3.1 fat."""
import math
BASE, FV = 30.0, 0.40
for fat in (4.2, 3.1):
    raw = (fat - 3.5) / 0.1
    print(f"fat {fat}: raw = {raw!r}")
    for name, fn in (("round", round), ("int", int), ("floor", math.floor)):
        s = fn(raw)
        print(f"   {name:5} steps={s:3}  rate with fat only = {BASE + s*FV:.2f}")
