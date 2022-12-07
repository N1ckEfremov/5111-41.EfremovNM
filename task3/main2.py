import random
chain = ['o','p']
s = 0
for i in range(0,10):
    d=0
    b=0 #счетчик орлов
    c=0 #счетчик решек
    while (b<3) and (c<3):
        a=random.choice(chain)
        print(a, end = ' ')
        if(a=='o'):
            b += 1
            c = 0
        elif(a=='p'):
            b = 0
            c += 1
        d +=1
    print(d)
    s += d
print ("среднее значение:", s/10)

