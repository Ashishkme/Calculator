#calculator

first = input("Enter First number : ")
operator = input("Enter Operator (+,-,*,/,%) : ")
second = input("Enter Second number : ")

first = int(first)
second = int(second)

if operator == "+":
    print("Soln.=", first + second)
elif operator == "-":
    print("Soln.=", first - second)
elif operator == "*":
    print("Soln.=", first * second)
elif operator == "/":
    print("Soln.=", first / second)
elif operator == "%":
    print("Soln.=", first % second)
else:
    print("Invalid Operation")