'''input a string of characters, convert each character to it's corresponding ascii, then convert ascii to binary. Then we have a list of binary of the particular string'''


def encode(message) : 
    binary_message = []
    ascii_message = toAscii(message)
    for x in ascii_message : 
        binary_message.append(toBinary(x))
    print(ascii_message)
    print(binary_message)



def toAscii(message) : 
    binary_digits = []
    ascii_message = [ord(ch) for ch in message]
    return ascii_message

def toBinary(x) :
    binary = ""
    while x > 0 : 
        binary = str(x % 2) + binary
        x //= 2
    return binary



#main
message = "Hello World"
encode(message)