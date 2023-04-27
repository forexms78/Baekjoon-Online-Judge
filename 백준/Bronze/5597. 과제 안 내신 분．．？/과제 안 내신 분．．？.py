count = 28

Array = [i+1 for i in range(30)]



while count:
    count -= 1
    k = int(input())
    Array.remove(k)


print(Array[0])
print(Array[1])