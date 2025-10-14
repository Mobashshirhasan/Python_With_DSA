""" Create a calculator """

''' + , - , / , % , * '''

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

operator = input("Enter an operator (+, -, /, %, *): ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "%":
    print(num1 % num2)
elif operator == "*":
    print(num1 * num2)
else:
    print("Invalid operator!")



# str = "1Y:0M:8W"

