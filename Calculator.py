import math
import time

num1 = int(input("Enter the number:: "))
num2 = int(input("Enter the number:: "))

m_ops = input("Enter the mathmatical operations (add/sub/divide/mult/pow/sqrt/e)")

if m_ops.lower( ) == "add":
    print(num1 + num2)
    print("ERROR :(")
elif m_ops.lower( ) == "sub":
    print(num1 - num2)
elif m_ops.lower( ) == "divide":
    print(num1/num2)
elif m_ops.lower( ) == "mult":
    print(num1*num2)
elif m_ops.lower( ) == "pow":
    ask = int(input("Enter the number:: "))
    x = input("Which number you want to solve to its power(num1/num2):: ")
    if x.lower( ) == "num1":
        print(num1**ask)
    elif x.lower( ) == "num2":
        print(num2**ask)
    else:
        print("ERROR :(")
elif m_ops.lower( ) == "sqrt":
    ask = input("Which number you want to solve to its sqrt(num1/num2):: ")
    if ask.lower( ) == "num1":
        a = math.sqrt(num1)
        print(round(a,2))
    elif ask.lower( ) == "num2":
        b = math.sqrt(num2)
        print(round(b,2))
    else:
        print("ERROR :(")
elif m_ops.lower( ) == "e":
    ask = input("Are you sure(y/n):: ")
    if ask.lower( ) == "y":
        print("Ok... I hope its make you calculation easy :)")
        time.sleep(2)
        exit( )
    elif ask.lower( ) == "n":
        print("Ok...")
        time.sleep(2)
    else:
        print("ERROR :(\nYou have to give answer in (y/n)")
else:
    print("ERROR :(")
