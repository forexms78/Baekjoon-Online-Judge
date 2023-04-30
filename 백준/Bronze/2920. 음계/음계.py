mylist = list(map(int,input().split()))


sortlist = []

for i in mylist:
    sortlist.append(i)

if mylist[0] == 1:
    sortlist.sort()
    if mylist == sortlist:
        print("ascending")
    else:
        print("mixed")
elif mylist[0] == 8:
    sortlist.sort(reverse=True)
    if mylist == sortlist:
        print("descending")
    else:
        print("mixed")
else:
    print("mixed")



