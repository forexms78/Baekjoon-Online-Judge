sentence = list(input())
array = []

for i in sentence:
    if i.islower():
        i = i.upper()
        array.append(i)
    else:
        i = i.lower()
        array.append(i)
        
array = "".join(array)
print(array)


