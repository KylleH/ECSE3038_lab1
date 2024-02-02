def parallel(r):
    parallel_resistance = 1 / sum(1 / i for i in r)
    print( f"{round(parallel_resistance)}"+" ohms")
    
def potential_divider(volt, resistors):
    total_resistance = sum(resistors)
    voltage_drops = [volt * (r / total_resistance) for r in resistors]
    
    print("Voltage drop across resistors:")
    for voltage in voltage_drops:
        print(f"{voltage:.3f} V")
        
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
