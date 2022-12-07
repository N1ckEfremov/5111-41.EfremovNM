
def calc_centr(n):
    centr=n//2
    return centr
def printMatrix(n):
    centr=calc_centr(n)
    for i in range(n):
        for j in range(n):
            if (i==centr) & (j ==centr):
                print(' ',end='')
            else: print('*',end='')
        print()
n=int(input())
if (n<3):
    print("введите другое число больше 3")
elif (n%2==0) :
    print("введите нечетное")
else:printMatrix(n)