import math
print("Enter the value of 3 coefficients")
a = float(input())
b = float(input())
c = float(input())

d = float((b*b) - (4*a*c))
if d > 0 : 
    print("Roots are real and different")
    r1 = (-b - math.sqrt(d)) / (2*a)
    r2 = (+b - math.sqrt(d)) / (2*a)
    print(r1)
    print(r2)
elif d == 0 : 
    print("Roots are equal")
    r1 = -b/(2*a)
    r2 = r1
    print(r1)
    print(r2)
else : 
    print("Roots are imaginary and different")
    real = -b/(2*a)
    imag = math.sqrt(-d)/(2*a)
    print(str(real)+"+i"+str(imag))
    print(str(real)+"-i"+str(imag))

