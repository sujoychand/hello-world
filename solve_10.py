""" Solve Fabonnaci Series with recursive method"""


def fab_series(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fab_series(n - 1) + fab_series(n - 2)


number = int(input("Fab series : \n"))
print(fab_series(number))
