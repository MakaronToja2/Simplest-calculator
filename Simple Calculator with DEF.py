def plus(x, y):
   #This function adds two numbers
   return x + y

def minus(x, y):
   #This function substract two numbers
   return x - y

def multiplying(x, y):
   #This function multiplies two numbers
   return x * y

def dividing(x, y):
   #Funcion for diving two number
   return x / y

class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    Magenta = '\033[35m'
while True:
    print(f"{bcolors.Magenta}SIMPLE CALCULATOR:{bcolors.ENDC}")
    print("Choose 1 to sum")
    print("Choose 2 for SUBTRACTION")
    print("Choose 3 to Multiplicate" )
    print("Choose 4 to Divide")
    print("Enter Exit to quit")

    choice = input("Enter your choice ")

    if choice == "Exit":
        print("Bye have a great time")
        break


    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1,"+",num2,"=", plus(num1,num2))

    elif choice == '2':
        print(num1,"-",num2,"=", minus(num1,num2))

    elif choice == '3':
        print(num1,"*",num2,"=", multiplying(num1,num2))

    elif choice == '4':
        if num2 ==0.0:
            print('Cannot divide by 0')
            continue
        else:
            print(num1,"/",num2,"=", dividing(num1,num2))
    else:
        print("Invalid input")

