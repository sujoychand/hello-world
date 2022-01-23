# Code withHarry : Solve 6 :Number less than 100 print different message , greater than 100 different message

while True:
    print("Enter user input ")
    in_num = int(input())
    if in_num < 100:
        print("Entered number is less than 100", in_num)
        continue
    else:
        print("Entered number is greater than 100, hence stopping loop")
        break


# print("Enter user input ")
# in_num = int(input())
#
# while in_num < 100:
#     print("Entered number is less than 100", in_num)
#     break
# else:
#     print("Entered number is greater than 100, hence stopping loop")