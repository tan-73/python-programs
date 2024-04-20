#printing words with even number of letters in a string
str1 = str(input("Enter a string : "))
s = str1.split()[::1]
length = len(s)
for i in range (0,length) : 
	length_of_word = int(len(s[i]))
	if length_of_word % 2 == 0 : 
		print(s[i])