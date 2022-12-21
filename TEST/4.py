import random
n=int(input("введите колличечество 10,11,12,13 или 15"))
spisok=[]
for i in range (0,n):
    x=random.randint(-999999999,999999999)
    spisok.append(x)
print(spisok)    
B = [spisok.pop(i) for i in reversed(range(len(spisok))) if spisok[i] < 0 ]
print(B)
print(sum(B))
C = [spisok.pop(i) for i in reversed(range(len(spisok))) if spisok[i] > 0 ]
print(C)
print(sum(C))
