import sys
input = sys.stdin.readline

count = int(input())
my_array = []

while count:
    count -= 1

    text = sys.stdin.readline().rstrip('\n')

    if text.count(" ") > 0:
        text, M = text.split(" ")

        if text == "push_front":
            my_array.append(M)
        elif text == "push_back":
            my_array.insert(0, M)

    else:
        if text == "front":
            if len(my_array) == 0:
                print(-1)
            else:
                print(my_array[-1])
        elif text == "back":
            if len(my_array) == 0:
                print(-1)
            else:
                print(my_array[0])
        elif text == "size":
            print(len(my_array))
        elif text == "empty":
            if len(my_array) == 0:
                print(1)
            else:
                print(0)
        elif text == "pop_front":
            if len(my_array) == 0:
                print(-1)
            else:
                print(my_array[-1])
                del my_array[-1]
        elif text == "pop_back":
            if len(my_array) == 0:
                print(-1)
            else:
                print(my_array[0])
                del my_array[0]



