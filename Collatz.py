print("Hi there!, Welcome to Collatz conjecture program!")
print("What does it do? oh, just type a number it will end in 1 anyway")
n = int(input("Type a number(bigger than 1): "))

while True:
    if n == 1:
        break
    elif n % 2 == 0:
        n = n / 2
        print("n is now ->",n)
    else:
        n = (n * 3) + 1
        print("n is now ->",n)