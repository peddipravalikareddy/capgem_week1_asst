

for num in range(1, 10001):
    #  div by both 3 and 5

    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")

    #  div by 3
    elif num % 3 == 0:
        print("Fizz")

    # div by 5
    elif num % 5 == 0:
        print("Buzz")

    else:
        #  not div by 3/5 then print num
        print(num)
