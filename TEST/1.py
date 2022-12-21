import math as mt
a=5 #α
b=1 #β
c=4 #γ
d=1 #θ
e=0 #μ
f=4 #ν
usl=int(pow(c,2)+pow(d,2))
if usl>1 :
    cosx=(mt.cos(a))
    apopolam=(a/2)
    per=(4**apopolam)
    vto=(3**cosx) #пусть e = 3
    y=per-vto
else :
    y=int(mt.tan(4*a)-c)
print(y)