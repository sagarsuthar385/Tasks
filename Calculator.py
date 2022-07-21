print("                                 ")
a=float(input("Enter the first number= "))
opr=input("Enter the opr(+\-\*\/\%)= ")
b=float(input("Enter the second number= "))
if opr=="+" :
    print("Result=", a+b)
elif opr=="-" :
    print("Result=", a-b)
elif opr=="*" :
    print("Result=", a*b)
elif opr=="/" :
    print("Result=", a/b)
elif opr=="%" :
    print("Result=", ((a*b)/100))
else:
     print("invilid")