basket, numberOfChanges = map(int,input().split())

basketArray = [i+1 for i in range(basket)]

while numberOfChanges:
    numberOfChanges -= 1
    i, j = map(int, input().split())
    basketArray[i-1], basketArray[j-1] = basketArray[j-1], basketArray[i-1]
        
    
print(*basketArray)