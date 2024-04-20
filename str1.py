#reversing the string and reversing each word of the string
str1 = str(input("Enter a string : "))

length = len(str1)
s = str1.split()[::-1]
l = []
#print(type(s))
#print(" ".join(s))
length = len(s)
i = 0
while i < length : 
    reversed_str = s[i][::-1]
    print(reversed_str, end=" ")
    i += 1