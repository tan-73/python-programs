'''input a string of characters, convert each character to it's corresponding ascii, then convert ascii to binary. Then we have a list of binary of the particular string'''



def toAscii(message) : 
    binary_digits = []
    ascii_message = [ord(ch) for ch in message]
    print(ascii_message)
    toBinary(ascii_message)

def toBinary(ascii_message) :
    binary_digits = []
    binary = ""
    for i in range(0, len(ascii_message)) : 
        while ascii_message[i] > 0 :
            remainder = ascii_message[i] % 2 
            binary = str(remainder) + binary
            ascii_message[i] //= 2
            binary_digits.append(binary)
    print(binary_digits)



#main
message = "Hello World"
toAscii(message)