def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        return "Error :- cannot divide by zero"
    return x / y

print("Welcome to simple calculator")
print("Choose an operation from the following")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice=input("Enter your choice (1/2/3/4) :")

    if choice in ('1','2','3','4'):
        num1=int(input("Enter first number"))
        num2=int(input("Enter Second number"))

        if choice =='1':
            print("Result;" ,add(num1,num2))

        elif choice =='2':
            print("Result;" ,sub(num1,num2))

        elif choice =='3':
            print("Result;" ,multiply(num1,num2))

        elif choice =='4':
            print("Result;" ,divide(num1,num2))

    else:
        print("Invalid choice")

    continue_calculation=input("Do you want to continue calculation? (yes/no)")
    
    if continue_calculation.lower() == 'no':
        print("Thank you for using simple calculator")
        break

    