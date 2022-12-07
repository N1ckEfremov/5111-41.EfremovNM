num = int(input())
num_list = []
while num!= 0 :
    num_list.append(num)
    num = int(input())
min = num_list[0]
max = num_list[0]
l = 0
for value in num_list:
    if value < min :
        min = value
        l += 1
for value in num_list:
    if value > max:
        max = value
        l += 1
print("min" ,min)
print("max" ,max)
for i in range(0,len(num_list)):
    for j in range(0,len(num_list)-1):
        if num_list[j] > num_list[j+1]:
            num_list[j], num_list[j+1]=num_list[j+1], num_list[j]
print(num_list)
print("каждый второй член удален", num_list[::2])