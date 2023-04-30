note = list(map(int,input().split()))

ascending = all(note[i] < note[i+1] for i in range(7))
descending = all(note[i] > note[i+1] for i in range(7))

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")
