#it track the total daily expenses of a person
def menu():
    print("welcomw in expenses tracker !\n" \
    "please press\n" \
    "1. add expenses --price and product \n" \
    "2. view all expenses detail \n" \
    "3. total amount of expense \n")
def add_expenses():
    
    f=open("expenses.txt","a")
    no=int(input("How many expenses you want to add:"))
    for i in range(no):
        data=input("Add data--> product,rupees:")
        f.write(data +"\n")
    f.close()
# add_expenses()
def view_expenses():
    
    f=open("expenses.txt","r")
    d={}
    for i in f:
        i=i.strip()
        product,price=i.split(",")
        d[product]=int(price)
    print(d)
    f.close()
# view_expenses()
def total_expenses():
    f=open("expenses.txt","r")
    total=0
    d={}
    for i in f:
        i=i.strip()
        product, price = i.split(",", 1)
        d[product]=int(price)
    for k,v in d.items():
        total+=v
    print("total expenses are:",total)
    f.close()
while True:
    menu()
    no=int(input("enter no"))
    if(no==1):
        add_expenses()
    if(no==2):
        view_expenses()
    if(no==3):
        total_expenses()
    else:
        print("enter correct value")




