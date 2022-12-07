import random
def generate_pass():
    lenght = random.randint(7,10)
    password_char =""
    for i in range(0,lenght):
        password_char+= chr(random.randint(33,126))
    return password_char 
print(generate_pass())