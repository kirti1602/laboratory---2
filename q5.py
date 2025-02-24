# Find the smallest of two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 < num2:
    print(f"{num1} is the smallest number.")
elif num2 < num1:
    print(f"{num2} is the smallest number.")
else:
    print("Both numbers are equal.")
