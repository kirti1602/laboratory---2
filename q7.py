# Print the Fibonacci series up to 13
n = 7  # Number of terms we want in the Fibonacci series
a, b = 1, 1  # Starting values

print(a, end=" ")
for i in range(1, n):
    print(b, end=" ")
    a, b = b, a + b  # Update values for next iteration
