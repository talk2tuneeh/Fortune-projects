import functools as ft

num = int(input("Enter your desired value: "))
lst = [x for x in range(1, num+1)]
factorial = ft.reduce(lambda x,y:x*y, lst)

if num == 1 or num == 0:
    print("The Factorial is 1")
else:
    print("The Factorial is: {}".format(factorial))