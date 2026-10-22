"""Task 8: prints the hand-trace table using the algorithm."""
entries = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]
total = 0.0
print("entry litres fat  snf  fatSt snfSt  rate   payment  total")
for i, (litres, fat, snf) in enumerate(entries, 1):
    fs, ss = round((fat - 3.5) / 0.1), round((snf - 8.5) / 0.1)
    rate = round(30.0 + fs * 0.40 + ss * 0.30, 2)
    pay = round(litres * rate, 2)
    total = round(total + pay, 2)
    print(f"{i:5} {litres:6} {fat:4} {snf:4} {fs:5} {ss:5} {rate:6.2f} {pay:8.2f} {total:8.2f}")
