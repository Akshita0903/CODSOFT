
print("select the operation.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
choice = input("Please enter a choice (1/2/3/4): ")
a =int(input("enter first number: "))
b = int(input("enter second number: "))
if choice == '1':
    print(a,"+",b,"=",a+b)
elif choice == '2': 
    print(a,"-",b,"=",a-b)
elif choice == '3': 
    print(a,"*",b,"=",a*b)
elif choice == '4': 
    print(a,"/",b"=",a/b)
else:
    print("This is an invalid input")
    