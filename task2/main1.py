vowels = "aouie"
simbol = input("введите букву")
if vowels.upper().__contains__(simbol.upper()):
    print("гласная")
elif simbol.upper() == 'Y':
    print("согласная и гласная")
else: print("согласная")
