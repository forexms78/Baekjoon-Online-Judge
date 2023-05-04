N,M = map(int,input().split())
my_list = sorted(map(int,input().split()))
near_number = M

for i in range(len(my_list)):
    count = 0
    for j in range(len(my_list)):
        for k in range(len(my_list)):
            if i == j or j == k or i == k:
                continue
            count = my_list[i] + my_list[j] + my_list[k]
            if count > M:
                continue
            number = M - count
            # if number == 0:
            #     print(count)
            # else:
            #     near_number = min(number,near_number)
            near_number = min(number,near_number)


print(M-near_number)