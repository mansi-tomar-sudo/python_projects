#student management system
def menu():
    print("welcome in student management system \n")
    print("where you can add , view,search,delete,update student\n")
    print("please pless \n")
    print("1. add student detail \n")
    print("2. view student detail \n")
    print("3. search student detail \n")
    print("4. update student detail \n")
    print("5. delete student detail \n")
def add_student():
    f=open("student.txt","a")
    # l=[]
    n=int(input("enter how many student data you want to add:"))
    for i in range(n):
        name=input("enter the name of student:")
        roll_no=int(input("enter the roll no of student:"))
        branch=input("enter the branch of student:")
        cgpa=float(input("enter the cgpa of student:"))
        # l.append([name,roll_no,branch,cgpa])
        # d=[name,roll_no,branch,cgpa]
        # f.write(d)
        f.write(f"{name},{roll_no},{branch},{cgpa}\n")
    f.close()


def view_student():
    f=open("student.txt","r")
    
    data=f.readlines()
    for line in data:
        print(line)
    f.close()


def search_student():
    f=open("student.txt","r")
    data=f.readlines()
    roll_student=input("enter the roll no to be search:")
    find=False
    for line in data:
        student=line.strip().split(",")
        if(student[1]==roll_student):
            print("student found")
            print(line)
        else:
            find=True
    if(find==True):
        print("student not found")
    f.close()
# search_student()

def update_student():
    f=open("student.txt","r")
    roll_student=input("enter the roll no to be update:")
    user=int(input("enter the number which you want to update:"))
    data=f.readlines()
    updated_data=[]
    for line in data:
        student=line.strip().split(",")
        if(student[1]==roll_student):
            print("student found")
            if(user==1):
                new_name=input("enter new name:")
                student[0]=new_name

            elif (user==2):
                new_rollno=input("enter new roll no:")
                student[1]=new_rollno
            elif(user==3):
                new_branch=input("enter new branch:")
                student[2]=new_branch
            else:
                new_cgpa=input("enter new cgpa:")
                student[3]=new_cgpa
            updated_data.append(",".join(student)+"\n")
        else:
            print("student not found")
        
    f.close()
    f=open("student.txt","w")
    f.writelines(updated_data)
    f.close()

def delete_student():
    f=open("student.txt","r")
    roll_student=input("enter the roll no to be update:")
    
    data=f.readlines()
    updated_data=[]
    found=False
    for line in data:
        student=line.strip().split(",")
        if(student[1]==roll_student):
            print("student found and delete")
            found=True
            continue
        else:
            print("student not found")
        updated_data.append(",".join(student)+"\n")
            
    f.close()
    f=open("student.txt","w")
    f.writelines(updated_data)
    f.close()


menu()
ch=int(input("enter the number you want:"))
if(ch==1):
    add_student()
elif(ch==2):
    view_student()
elif(ch==3):
    search_student()
elif(ch==4):
    update_student()
elif(ch==5):
    delete_student()
else:
    print("enter the correct number")














    







    

