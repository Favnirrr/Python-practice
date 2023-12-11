# FizzBuzz
for i in range(1,21):
    if i % 15 == 0:
        print('FizzBuzz')
        continue
    elif i % 5 == 0:
        print('Buzz')
        continue
    elif i % 3 == 0:
        print('Fizz')
        continue
    print(i)

