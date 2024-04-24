import math
import random

def isPrime(number) : 
    for i in range(2, number) : 
        if number % i == 0 : 
            return False
    return True

def generate_prime() : 
    prime = random.randint(7813, 78263)
    while not isPrime(prime) : 
        prime = random.randint(7813, 78263)
    return prime



str1 = "Hello World"
# lst_str1 = [ch for ch in str1]
# print(lst_str1)
lst_ascii = [ord(ch) for ch in str1]
print(lst_ascii)

p = generate_prime()
q = generate_prime()

