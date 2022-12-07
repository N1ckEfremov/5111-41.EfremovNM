
for value in range (1,101):
    res = value.__str__()
    if((value % 3==0) and (value % 5==0)):
        res += "FizzBuzz"
    elif (value % 3==0):
        res += "Fizz"
    elif(value % 5==0):
        res += "Buzz"
    print(res)
