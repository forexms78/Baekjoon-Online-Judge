count = int(input())
words = []

while count:
     count -= 1
     words.append(input())

words = list(set(words))
words.sort()
words = sorted(words, key=len)

for i in words:
    print(i)