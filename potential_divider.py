def potential_divider(volt, r):
    voltage_drop = [volt * (i / sum(r)) for i in r]
    return voltage_drop

voltage_source = 10.0  # Replace with your actual voltage source value
resistor_values = [100, 200, 300, 400, 10]  # Replace with your actual resistor values

vdrop = potential_divider(voltage_source, resistor_values)
print("Voltage drop across resistors:", vdrop)
