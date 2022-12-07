import math
leg_a = int(input("ge"))
leg_b = int(input("eg"))
hypotenuse = lambda a,b: math.sqrt(a**2 + b**2)
print(hypotenuse(leg_a,leg_b))