r = int(input("Enter the number of rows : "))
c = int(input("Enter the number of columns : "))
matrix = []

print("Enter the elements : ")

for i in range (0, r) : 
    for j in range (0, c) : 
        matrix.append(int(input()))


for i in matrix : 
    for j in matrix : 
        print(j, end="")
    print()
