def calculater():
    num1 = float(input("enter first number : "))
    num2 = float(input("enter second number : "))
    opt = input("enter any operator (such a +,-,*,/,%) :")
    if opt == '+':
        print(f"{num1} + {num2} = {num1+num2}")
    elif opt == '-':
        print(f"{num1} - {num2} = {num1-num2}")
    elif opt == '*':
        print(f"{num1} * {num2} = {num1*num2}")
    elif opt == '/':
        print(f"{num1} / {num2} = {num1/num2}")
    elif opt == '%':
        print(f"{num1} % {num2} = {num1%num2}")
    else:
        print("Invalid operator\n Try again...")

calculater()