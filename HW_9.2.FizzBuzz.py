#Users enter a number bewteen 1 and 100
#FizzBuzz starts to count to that number
# In case the number is divisible with 3, it prints "fizz" instead of the number.
# If the number is divisible with 5, it prints "buzz". If it's divisible with both 3 and 5, it prints "fizzbuzz"

print("Hi, Welcome to FizzBuzz, we fizz, buzz or fizzbuzz numbers!")

while True:
    guess = int(input("You can start by entering a number between 1 and 100"))

    if guess % 3 == 0:
        print("fizz")
        break
    elif guess % 5 == 0:
        print("buzz")
        break
    elif guess % 3 == 0 and guess % 5 == 0:
        print("fizzbuzz")
        break
    else:
        print(guess)
        break