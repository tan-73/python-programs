import math
num = int(input("Enter a number : "))
original_num = num
arm = 0

while num > 0 : 
    digit = int(num % 10)
    arm += math.pow(digit, 3)
    num /= 10

if original_num == arm : 
    print("Armstrong number")
else : 
    print("Not an Armstrong number")