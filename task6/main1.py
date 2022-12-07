import numpy as np
import math as mt
import random
N = int(input("ВВЕДИТЕ ЧИСЛО: "))
a = np.ndarray(N)
def calc_geom(arr: np.ndarray):
    mult = 1
    for num in arr:
        mult *= num
    return mt.pow(mult, 1/arr.size)
for i in range(0,N):
    a[i] = random.randint(1,100)   
arg_geom=calc_geom(a)
print("массив:",a)
print("среднее геометрическое:", arg_geom)