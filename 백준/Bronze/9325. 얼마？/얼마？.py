N = int(input())

for _ in range(N):

    car_price = int(input())

    option_cnt = int(input())

    if option_cnt == 0:
        print(car_price)
        continue
    else:
        for _ in range(option_cnt):
            number_of_options, option_price = map(int, input().split())

            car_price += (number_of_options * option_price)

        print(car_price)


