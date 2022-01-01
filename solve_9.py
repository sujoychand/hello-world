""" Solution for Exercise 5 Health mgmt. System | thank you Harry Bhai """

def getdate():
    """This function gets the current time """
    import datetime
    return datetime.datetime.now()


# noinspection PyUnusedLocal
def get_food_details():
    """This function gets details around
     when did user had his food
     what did he have for  his food"""
    print("Enter time of day \n 1 for Breakfast \n 2 for Lunch \n 3 for Dinner")
    food_time = int(input())
    print("Enter number of items user had ")
    items = int(input())
    item_details = " "
    for item in range(0, items):
        print("Enter item details : ")
        food_item = input()
        item_details = item_details + ' ' + str(food_item)
    return str(food_time), str(items), str(item_details)


def get_ex_details():
    """This function gets details around
     when did user did his exercise
     what did he do during the exercise"""
    print("Enter time of day \n 1 for Morning \n 2 for Afternoon \n 3 for Evening")
    ex_time = int(input())
    print("Enter number of exercises user had ")
    ex_items = int(input())
    ex_item_details = " "
    for ex_item in range(0, ex_items):
        print("Enter exercise details : ")
        ex_done = input()
        ex_item_details = ex_item_details + ' ' + str(ex_done)
    return str(ex_time), str(ex_items), ex_item_details


def open_file_logging():
    """This function logs the data about
    who is the user
    what activity is for
    what to track for the activity"""
    print("Enter who is it for \n 1 - Hammad \n 2 - Harry \n 3- Rohan")
    person_name = int(input())
    print("Enter what it is for \n 1- Exercise \n 2- Diet")
    event_type = int(input())
    if person_name == 1 and event_type == 1:
        with open("hammad_exercise.txt", "a") as f:
            f.write("\n" + str(getdate()) + ' ' + str(get_ex_details()))

    if person_name == 2 and event_type == 1:
        with open("Harry_exercise.txt", "a") as f:
            f.write("\n" + str(getdate()) + ' ' + str(get_ex_details()))

    if person_name == 3 and event_type == 1:
        with open("rohan_exercise.txt", "a") as f:
            f.write("\n" + str(getdate()) + ' ' + str(get_ex_details()))

    if person_name == 1 and event_type == 2:
        with open("Hammad_diet.txt", "a") as f:
            f.write("\n" + str(getdate()) + ' ' + str(get_food_details()))

    if person_name == 2 and event_type == 2:
        with open("Harry_diet.txt", "a") as f:
            f.write("\n" + str(getdate()) + ' ' + str(get_food_details()))

    if person_name == 3 and event_type == 2:
        with open("rohan_diet.txt", "a") as f:
            f.write("\n" + str(getdate()) + ' ' + str(get_food_details()))


def open_retrieve_logging():
    """This function retrieves information about
    who is the user
    what activity was tracked
    What was performed in that activity """
    print("Whose it for \n 1 - Hammad \n 2 - Harry \n 3- Rohan")
    person_name = int(input())
    print("What is it for \n 1- Exercise \n 2- Diet")
    event_type = int(input())
    if person_name == 1 and event_type == 1:
        with open("hammad_exercise.txt", "rt") as f:
            print(f.read())

    if person_name == 2 and event_type == 1:
        with open("Harry_exercise.txt", "rt") as f:
            print(f.read())

    if person_name == 3 and event_type == 1:
        with open("rohan_exercise.txt", "rt") as f:
            print(f.read())

    if person_name == 1 and event_type == 2:
        with open("Hammad_diet.txt", "rt") as f:
            print(f.read())

    if person_name == 2 and event_type == 2:
        with open("Harry_diet.txt", "rt") as f:
            print(f.read())

    if person_name == 3 and event_type == 2:
        with open("rohan_diet.txt", "rt") as f:
            print(f.read())


if __name__ == '__main__':
    print("********* \n Welcome to Healthcare Facility \n Owner : xxxx Family \n *********")
    while True:
        print("You want to use the system \n Press Y to proceed \n Press N to exit")
        system_use = input()
        if system_use.upper() == "Y" or system_use.lower() == "y":
            count = 0
            count = count + 1
            print("Enter your choice \n 1: Logging Data  \n 2: Retrieving Data")
            print("choice is ")
            choice = int(input())
            if choice == 1:
                open_file_logging()
                print("System was used", count, " times")
                continue
            elif choice == 2:
                open_retrieve_logging()
                print("System was used", count, " times")
                continue
        elif system_use.upper() == "N" or system_use.lower() == "n":
            count = 0
            count = count + 1
            print("You now exiting ...")
            print("System was NOT used ", count, " times")
            break
        else:
            print("Incorrect Entry ! Please enter correct choice")

    print("****** \n Program Credits : Sujoy Chand \n Created for Practice \n Below is list of functions displayed \n ")
    print("open_file_logging: " + open_file_logging.__doc__ + "\n")
    print("open_retrieve_logging: " + open_retrieve_logging.__doc__+ "\n")
    print("get_ex_details: " + get_ex_details.__doc__ + "\n")
    print("get_food_details: " + get_food_details.__doc__ + "\n")
    print("getdate: " + getdate.__doc__ + "\n")






