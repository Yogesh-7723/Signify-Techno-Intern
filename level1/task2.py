temp = float(input("Enter The Temprature Value"))
unit = input("Unit Enter C for Celsius and F for Fahrenheit :")
if unit.upper() == 'C':
    F = temp*(9/5) + 32
    print("Temprature in Fahrenheit = ",F,"°F")
    
elif unit.upper() == 'F':
    C = (temp-32)*(5/9)
    print("Temprature in Celsius = ",C,"°C")

else:
    print("Invalid Choice \n Try again !")