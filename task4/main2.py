word_dict ={}
word = input()
while word:
    if not word_dict.get(word):
        word_dict.update({word:word})
    word = input()
for i in word_dict.keys():
    print(i,end =" ")