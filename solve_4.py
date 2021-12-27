# code with Harry : Solution -4

print("Enter first Number")
var_1 = int(input())
print("Enter second Number")
var_2 = int(input())
print("Enter Operator\n + for Addition \n - for subtraction \n * for multiplication \n / for division")
operator = input()
if operator == "+":
    if int(var_1) == 56 and int(var_2) == 9:
        result = 77
    else:
        result = int(var_1 + var_2)
    print("Result = ", result)
elif operator == "-":
    result = int(var_1-var_2)
    print("Result = ", result)
elif operator == "*":
    if int(var_1) == 45 and int(var_2) == 3:
        result = 555
    else:
        result = int(var_1 * var_2)
    print("Result = ", result)
elif operator == "/":
    if int(var_1) == 56 and int(var_2) == 6:
        result = 4
    else:
        result = int(var_1 / var_2)
    print("Result = ", result)
else:
    print("Invalid Operator entered")


