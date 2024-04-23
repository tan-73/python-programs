import math
import random

p = random.randrange(214783, 2147483)
q = random.randrange(214783, 2147483)
print(p)
print(q)

str1 = "Hello World"
# lst_str1 = [ch for ch in str1]
# print(lst_str1)
lst_ascii = [ord(ch) for ch in str1]
print(lst_ascii)


def gcd(num1, num2) :
    num1 = float(num1)
    num2 = float(num2) 
    i = 1
    while i < num1 or i < num2 : 
        if num1 % i == 0 and num2 % i == 0 : 
            gcd = i
        i += 1
    print(gcd)

print(4%2)

m = pow(37, 43) % 77
print(m)
gcd(p, q)
