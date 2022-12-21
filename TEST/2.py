import math as mt
a=5 #α
b=1 #β
c=4 #γ
d=1 #θ
e=0 #μ
f=4 #ν
Az=c+d
x=a
while a<x<a+2:
    print(x)
    cosx=mt.cos(x)
    sinx=mt.sin(x)
    A_KUB=pow(Az,3)
    u1=pow(cosx,2)
    u2=A_KUB*pow(sinx,2)
    y=u1+u2
    print(y)
    x=x+0,5