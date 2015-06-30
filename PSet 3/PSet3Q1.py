def radiationExposure(start, stop, step):
        
    total = 0.0
    i = start
    while(i<stop): 
        total += step * f(i)
        i = i + step
    return total 