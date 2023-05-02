while 1:
     number = int(input())
     ok = ""

     if number == 0:
          break
     else:
          number = str(number)
          my_array = []
          for char in number:
               my_array.append(int(char))

          while len(my_array) >= 1:
               if len(my_array) == 1:
                    my_array.pop()
                    ok = "yes"
               elif my_array[0] != my_array[-1]:
                    my_array.clear()
                    ok = "no"
               elif my_array[0] == my_array[-1]:
                    my_array.pop(0)
                    my_array.pop(-1)
                    ok = "yes"
          print(ok)