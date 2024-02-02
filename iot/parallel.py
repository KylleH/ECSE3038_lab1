def parallel(r):
    parallel_resistance = 1 / sum(1 / i for i in r)
    print( f"{round(parallel_resistance)}"+" ohms")
    
def potential_divider(volt, resistors):
    total_resistance = sum(resistors)
    voltage_drops = [volt * (r / total_resistance) for r in resistors]
    
    print("Voltage drop across resistors:")
    for voltage in voltage_drops:
        print(f"{voltage:.3f} V")
