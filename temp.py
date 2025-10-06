def categorize_temperature(temp_c):
    """
    Categorize temperature in Celsius:
     - “Cold” if below some threshold (e.g. < 15 °C)
     - “Normal” if in a middle range (e.g. 15-25 °C)
     - “Hot” if above some threshold (e.g. > 25 °C)
    You can adjust thresholds as needed.
    """
    if temp_c < 0 or temp_c > 1000:  # sanity check, adjust upper bound if needed
        return "Invalid temperature"
    if temp_c <= 15:
        return "Cold"
    elif temp_c <= 25:
        return "Normal"
    else:
        return "Hot"

def get_temperature_input():
    """
    Prompts user for temperature (in Celsius),
    validates input, returns float.
    """
    while True:
        s = input("Enter temperature (in °C): ")
        try:
            t = float(s)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        # You can impose some reasonable bounds
        # Let's accept −100 to 500 °C for example
        if t < -100 or t > 500:
            print("Temperature out of realistic range. Try again.")
            continue
        return t

def main():
    print("Temperature categorization")
    temp_c = get_temperature_input()
    category = categorize_temperature(temp_c)
    print(f"Temperature: {temp_c:.2f} °C → Category: {category}")

if name == "main":
    main()
def categorize_temperature(temp_c):
    """
    Categorize temperature in Celsius.
    Adjust thresholds as needed.
    """
    if temp_c <= 15:
        return "Cold"
    elif temp_c <= 25:
        return "Normal"
    else:
        return "Hot"

def get_temperature_and_unit():
    """
    Returns (temperature_value, unit) where unit is 'C' or 'F'.
    """
    while True:
        s = input("Enter temperature with unit (e.g. 25 C or 77 F): ")
        parts = s.strip().split()
        if len(parts) != 2:
            print("Please enter in format: <number> <unit> (C or F).")
            continue
        num_str, unit = parts
        unit = unit.upper()
        if unit not in ("C", "F"):
            print("Unit must be 'C' or 'F'. Try again.")
            continue
        try:
            val = float(num_str)
        except ValueError:
            print("Could not parse the number. Try again.")
            continue
        return val, unit

def fahrenheit_to_celsius(f):
    return (f - 32) * 5.0 / 9.0

def celsius_to_fahrenheit(c):
    return c * 9.0 / 5.0 + 32

def main():
    print("Temperature categorization (accepts C or F)")

    val, unit = get_temperature_and_unit()
    if unit == "F":
        temp_c = fahrenheit_to_celsius(val)
        print(f"Converted: {val:.2f} °F → {temp_c:.2f} °C")
    else:
        temp_c = val

    category = categorize_temperature(temp_c)
    temp_f_converted = celsius_to_fahrenheit(temp_c)

    print(f"Final: {temp_c:.2f} °C → Category: {category}")
    print(f"In Fahrenheit: {temp_f_converted:.2f} °F")

if name == "main":
    main()

