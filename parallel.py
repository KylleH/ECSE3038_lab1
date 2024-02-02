def parallel(r):
    parallel_resistance = 1 / sum(1 / i for i in r)
    print( f"{round(parallel_resistance)}"+" ohms")
    
