'''input a string of characters, convert each character to it's corresponding ascii, then convert ascii to binary. Then we have a list of binary of the particular string'''



def toAscii(message) : 
    ascii_message = [ord(ch) for ch in message]
    print(ascii_message)




#main
message = "Hello World"
toAscii(message)