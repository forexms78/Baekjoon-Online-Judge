n = int(input())

ending_numbers = []
for i in range(666, 10000000):
     if '666' in str(i):
          ending_numbers.append(i)
          if len(ending_numbers) == n:
               break
     

print(ending_numbers[n-1])
