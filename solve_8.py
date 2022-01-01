""" Solution for problem 4 Code with Harry
Learning from the problem was boolean works of "int" with input, but it will have only if /else
"""
print("Enter value of n")
n = int(input())
print("Determine Star Pattern by using either\n 1- True \n 0- False ")
bool_var = int(input())
if bool(bool_var):
    for j in range(0, n):
        j = j + 1
        for i in range(0, j):
            print("*", end=" ")
        print("\n")
else:
    for j in range(n, 0, -1):
        for i in range(0, j):
            print("*", end=" ")
        print("\n")

#
# """More Concrete solution but not with boolean """
# print("Enter value of n")
# n = int(input())
# print("Determine Star Pattern by using either\n 1- True \n 0- False ")
# bool_var = str(int(input()))
# if bool_var == "1":
#     for j in range(0, n):
#         j = j + 1
#         for i in range(0, j):
#             print("*", end=" ")
#         print("\n")
# elif bool_var == "0":
#     for j in range(n, 0, -1):
#         for i in range(0, j):
#             print("*", end=" ")
#         print("\n")
# else:
#     print("Enter Correct Value !!!")
