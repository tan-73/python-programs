import random

start_val = int(input("Enter the starting value : "))
end_val = int(input("Enter the ending value : "))
num = random.randrange(start_val, end_val)
print(num)

print("RANDOM NUMBER GENERATED")

i = 0
while i == 0 : 
    guess_num = int(input("TAKE A GUESS : "))
    if guess_num == num : 
        print("HOORAY! You guessed it right")
        break
    elif guess_num > num : 
        print("OOPS! You guessed too high")
        continue
    else : 
        print("OOPS! You guessed too low")
    
