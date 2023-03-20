#This function multiplies two numbers
def multiply(x,y):
    return x*y

#this function provides two numbers
def divide(x,y):
    return x/y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    #Taking input from the user
    choice = input ("Enter choice(1/2/3/4): ")

    #checking if the choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1,num2))

    next_calculation = input("Lets do the next calculation? (yes/no): ")
    if next_calculation == "no":
        break
else:
    print("Invalid Input")
                         
