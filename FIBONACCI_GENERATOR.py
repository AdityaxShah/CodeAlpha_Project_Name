def fibonacci_generator(x):
    a, b = 0, 1
    count = 0
    while count < x :
        yield a
        a, b = b, a + b
        count += 1

n = int(input("Enter the number of Fibonacci terms: "))
print(", ".join(str(num) for num in fibonacci_generator(n)))

