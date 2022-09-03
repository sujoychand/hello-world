""" Solve Fibonacci Series with recursive method"""


def fab_series(n):  # Define Fibonacci Series
    if n <= 1:
        return n
    else:
        return fab_series(n - 1) + fab_series(n - 2)


print("How many values of Fibonacci series   ")
number = int(input())
if number <= 0:
    print("Enter Positive Number")
else:
    for i in range(number):
        print(fab_series(i), end=" ")
