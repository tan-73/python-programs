arr = []

n = int(input("Enter number of elements : "))

print("Enter the elements : ")
for i in range (0, n) : 
    ele = int(input())
    arr.append(ele)
print(arr)

sum = 0
for i in range(0, n) : 
    sum += arr[i]
print(sum)