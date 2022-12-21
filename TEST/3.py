mylist=list(map(str,input().split()))
longest=""
for element in mylist:
    if len(element)>len(longest):
        longest=element
print(longest)