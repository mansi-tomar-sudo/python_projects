# quiz app
marks=0
print("====== QUIZ APP ======")
q1=int(input("q1- What does CPU stand for?\n"
               "Options are:\n"
               "1. Central Process Unit\n"
               "2. Central Processing Unit\n"
               "3. Computer Personal Unit\n"
               "4. Control Processing Unit\n"
               "Enter your answer: "))
q2=int(input("q2- Which language is mainly used for AI and ML?\n"
                "Options are:\n"
                "1. HTML\n"
                "2. CSS\n"
                "3. Python\n"
                "4. SQL\n"
                "Enter your answer: "))
q3=int(input("q3- Which symbol is used for comments in Python?\n"
               "1. //\n"
               "2. #\n"
               "3. <!-- -->\n"
               "4. **\n"
               "Enter your answer: "))
q4=int(input("q4- What does RAM stand for?\n" 
            "1. Read Access Memory\n"
            "2. Random Access Memory\n"
            "3. Run Access Memory\n"
            "4. Random Allocate Memory\n"
            "Enter your answer: "))
q5=int(input("q5- Which company developed Python?\n" 
            "1. Microsoft\n"
            "2. Apple\n"
            "3. Google\n"
            "4. None of these\n"
            "Enter your answer: "))
q6=int(input("q6- Which keyword is used to create a function in Python?\n" 
            "1. function\n"
            "2. define\n"
            "3. def\n"
            "4. fun\n"
            "Enter your answer: "))
q7=int(input("q7- Which data structure stores key-value pairs in Python?\n" 
            "1. List\n"
            "2. Tuple\n"
            "3. Set\n"
            "4. Dictionary\n"
            "Enter your answer: "))
q8=int(input("q8- What is the extension of a Python file??\n" 
            "1. .java\n"
            "2. .py\n"
            "3. .html\n"
            "4. .cpp\n"
            "Enter your answer: "))
q9=int(input("q9- Which operator is used for multiplication in Python?\n" 
            "1. x\n"
            "2. %\n"
            "3. *\n"
            "4. #\n"
            "Enter your answer: "))
q10=int(input("q10- What does HTML stand for?\n" 
            "1. Hyper Text Markup Language\n"
            "2. High Transfer Machine Language\n"
            "3. Hyper Tool Multi Language\n"
            "4. Home Text Machine Language\n"
            "Enter your answer: "))
if(q1==2):
    print("correct answer, so marks is increment by 1")
    marks+=1

else:
    print("wrong ans")
if(q2==3):
    print("correct answer, so marks is increment by 1")
    marks+=1

else:
    print("wrong ans")
if(q3==2):
    print("correct answer, so marks is increment by 1")
    marks+=1

else:
    print("wrong ans")
if(q4==2):
    print("correct answer, so marks is increment by 1")
    marks+=1

else:
    print("wrong ans")
if(q5==4):
    print("correct answer, so marks is increment by 1")
    marks+=1

else:
    print("wrong ans")
if(q6==3):
    print("correct answer, so marks is increment by 1")
    marks+=1

else:
    print("wrong ans")
if(q7==4):
    print("correct answer, so marks is increment by 1")
    marks+=1

else:
    marks-=1
if(q8==2):
    print("correct answer, so marks is increment by 1")
    marks+=1

else:
    print("wrong ans")
if(q9==3):
    print("correct answer, so marks is increment by 1")
    marks+=1

else:
    print("wrong ans")
if(q10==1):
    print("correct answer, so marks is increment by 1")
    marks+=1

else:
    print("wrong ans")

print("your marks out of 10 is:",marks)
if marks >= 8:
    print("Excellent")
if marks <8 and marks>=4:
    print("Good")
if marks<=4:
    print("you have to improve")
print("====== QUIZ FINISHED ======")

