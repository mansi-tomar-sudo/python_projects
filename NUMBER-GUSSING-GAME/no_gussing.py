import random
no=random.randint(1,10)
count=0

while True:
    user_no=int(input("guess a number between 1 to 10:"))
    count+=1
    if(user_no>no):
        print("too high")
        
    elif(user_no<no):
        print("too low")
    else:
        print("You guessed successfully 🎉")
        print("You guessed the number in", count, "attempts")
        break
    

