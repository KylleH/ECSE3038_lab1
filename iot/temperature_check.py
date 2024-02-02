def temperature_check(temp, char):
    if char == "F":
        # Convert Fahrenheit to Celsius
        temp_celsius = (temp - 32) * 5/9
    elif char == "C":
        temp_celsius = temp
    else:
        print("Invalid temperature scale. Please use 'F' for Fahrenheit or 'C' for Celsius.")
        return

    if temp_celsius > 38:
        print("Person has a fever.")
    elif 36 <= temp_celsius <= 38:
        print("Normal temperature.")
    else:
        print("Person has hypothermia.")


