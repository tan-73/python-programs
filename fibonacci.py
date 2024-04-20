fib = 0
fib1 = 1
fib2 = 1
i = 0
n = int(input("Enter a number : "))

while i < n : 
    print(fib, end="  ")
    fib1 = fib2
    fib2 = fib
    fib = fib1 + fib2
    i += 1
