# Check if a number is prime
number = int(input("Enter a number to check if it is prime: "))

if number > 1:
    for i in range(2, int(number ** 0.5) + 1):  # Check divisibility up to the square root of the number
        if number % i == 0:
            print(f"{number} is not a prime number.")
            break
    else:
        print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
