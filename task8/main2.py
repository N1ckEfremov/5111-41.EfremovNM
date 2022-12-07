import re
text=("в сравнение сравнение сравнение Сравнение с собаками, кошками Кошки не претерпели серьезных изменений в процессе одомашнивания")
def get_dublicates(text,word):
    return re.findall(f'{word} {word}', text, flags=re.IGNORECASE)
def splittext(text):
    return re.findall(r'\b(\w+)\b', text)
def re
    