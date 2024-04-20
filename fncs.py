def add(a, b) : 
    return a+b

def sub(a, b) : 
    return a-b
    
def prod(a, b) : 
    return a*b
    
def quo(a, b) : 
    return int(a/b)
    
def modulus(a, b) : 
    return int(a%b)
    
print("Enter 2 numbers : ")
num1 = int(input())
num2 = int(input())

choice = int(input("Enter your choice : "))
if choice == 1 : 
    print(add(num1, num2))
elif choice == 2 : 
    print(sub(num1, num2))
elif choice == 3 : 
    print(prod(num1, num2))
elif choice == 4 : 
    print(quo(num1, num2))
else : 
    print(modulus(num1, num2))
