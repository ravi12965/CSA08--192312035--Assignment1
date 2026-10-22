"""Task 1: shows both data designs for farmer entries."""
# Approach A: separate variables (does not scale)
litres1, fat1, snf1 = 10, 3.5, 8.5
litres2, fat2, snf2 = 8.5, 4.2, 8.7
total_litres_a = litres1 + litres2          # must add each variable by hand

# Approach B: list of tuples (scales)
entries = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]
total_litres_b = 0
for litres, fat, snf in entries:            # one loop for any n
    total_litres_b += litres

print("Separate variables total litres (2 entries):", total_litres_a)
print("List of tuples total litres (3 entries)    :", total_litres_b)
