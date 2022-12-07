symbol = float(input("введите магнитуду землетрясения"))
if (symbol < 2.0):
    print("минимальное")
elif (symbol >= 2.0) and (symbol < 3.0):
    print("очень слабое")
elif (symbol >= 3.0) and (symbol < 4.0):
    print("слабое")
elif (symbol >= 4.0) and (symbol < 5.0):
    print("промежуточное")
elif (symbol >= 5.0) and (symbol < 6.0):
    print("умеренное")
elif (symbol >= 6.0) and (symbol < 7.0):
    print("сильное")
elif (symbol >= 7.0) and (symbol < 8.0):
    print("очень сильное")
elif (symbol >= 8.0) and (symbol < 10.0):
    print("огромное")
elif (symbol >= 10.0):
    print("разрушительное")