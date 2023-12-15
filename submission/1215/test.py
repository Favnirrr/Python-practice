def FizzBuzz(num):
    list = []
    for i in range(0, num):
        if i % 15 == 0:
            list[i] = "FizzBuzz"
        elif i % 3 == 0:
            list[i] = "Fizz"
        elif i % 5 == 0:
            list[i] = "Buzz"
        else:
            list[i] = str(i)
    
    return list

input_line = int(input())
print(FizzBuzz(input_line))