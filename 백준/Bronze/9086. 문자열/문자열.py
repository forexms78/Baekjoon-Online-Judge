repeat = int(input())

while repeat:
    repeat -= 1
    mylist = list(input())
    print(mylist[0],mylist[-1], sep="")