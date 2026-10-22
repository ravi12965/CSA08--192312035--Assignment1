"""Task 5: reading input and converting types safely."""

def read_float(text):
    """Return float(text) or None if the text is not a valid number."""
    try:
        return float(text)
    except ValueError:
        return None

def is_number_string(text):
    """String-method validation (look before you leap)."""
    t = text.strip()
    return t.replace(".", "", 1).isdigit()

def demo():
    print("input() always returns str because the keyboard supplies characters;")
    print("the program must decide the type via int() / float().")
    for text in ("8.5", " 8.5 ", "8,5", "eight", "10"):
        val = read_float(text)
        print(f"{text!r:8} try/except -> {val!s:5} | string-check(strip) -> {is_number_string(text)}")
    print("raw check without strip for ' 8.5 ':", " 8.5 ".replace(".", "", 1).isdigit())
    amount = 283.9
    print(f"Amount: {amount:8.2f} | litres: {8.5:6.1f} | id: {'F01':>6}")
    print(f"int('42') = {int('42')}  float('4.2') = {float('4.2')}")
    try:
        int("8.5")
    except ValueError as err:
        print("int('8.5') ->", err)

def read_entry():
    """Interactive loop - repeats until the clerk types a valid litre value."""
    while True:
        text = input("Litres: ")
        value = read_float(text)
        if value is not None and value >= 0:
            return value
        print("  Invalid litres, try again.")

if __name__ == "__main__":
    demo()
    # litres = read_entry()   # uncomment to try interactively
