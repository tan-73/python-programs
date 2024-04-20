str1 = str(input("Enter a string : "))

reversed_str1 = str1[::-1]

if reversed_str1 == str1 : 
	print(str1+" is a palindrome")
else : 
	print(str1+" is not a palindrome")