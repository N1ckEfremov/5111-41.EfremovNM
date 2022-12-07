import math as mt
year = int(input("введите год"))

day_of_the_week = (year + mt.floor((year - 1)/4) - mt.floor((year - 1)/100) + mt.floor((year - 1)/400))%7
if day_of_the_week == 0 :
    print("воскресенье")
elif day_of_the_week == 1 :
    print("понедельник")
elif day_of_the_week == 2 :
    print("вторник")
elif day_of_the_week == 3 :
    print("среда")
elif day_of_the_week == 4 :
    print("четверг")
elif day_of_the_week == 5 :
    print("пятница")
elif day_of_the_week == 6 :
    print("суббота")