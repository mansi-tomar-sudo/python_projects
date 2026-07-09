#password generator 
print("Give me the information to get strong password")
import random
symbol=input("are you want special symbol -- y/n? :")
number=input("are you want numbers -- y/n? :")
symbol = symbol.lower()
number = number.lower()

def generate_password():
    all_ch="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if symbol == "y" and number == "y":
        all_ch += "@#$%&*!0123456789"

    elif number == "y" and symbol == "n":
        all_ch += "0123456789"

    elif symbol == "y" and number == "n":
        all_ch += "@#$%&*!"
    for i in range(no):
        password=""
        for j in range(length):
            


            ch=random.choice(all_ch)
            password+=ch
        print(password)

while True:
    length=int(input("Enter the length of password:"))
    no=int(input("enter how many password do you want:"))
    if(length>0 and no>0):
        generate_password()
        break
    else:
        print("please enter the valid number:")





