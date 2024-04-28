import numpy as np
import matplotlib.pyplot as plt
import time
from random import choice, randint


# fonction a tester
def facto(x: int) -> int:
    
    res = 1
    for i in range(0, x+1):
        res *= i
    return res 

def fibo(x: int) -> int:
    if x <= 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)




# fonction utilisable
def complex_int(fonction, iteration) -> None:  

    lst_res = [] 

    for i in range(iteration):
        min_temps = 999999999999
        for j in range(1000):
            debut = time.perf_counter()
            fonction(i)
            fin = time.perf_counter()
            temps_execution = fin - debut
            if temps_execution < min_temps:
                min_temps = temps_execution
        lst_res.append(round(min_temps, 10))

    fig, ax = plt.subplots()
    ax.plot(range(iteration), lst_res)
        
    plt.show()













# test
complex_int(facto, 500)
complex_int(fibo, 25)

