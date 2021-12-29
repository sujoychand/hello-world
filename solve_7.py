"""Solve code with harry problem user wants others to guess a number he will give number and number of attempts
allowed others will guess number in those attempts && accordingly they will get congratulations method OR choice
exhausted message """
number_to_guess = int(input("Enter number you want your partner to guess \n"))
number_of_guess = int(input("Enter number of guesses allowed \n"))
item = 0
while True:
    if item <= number_of_guess:
        choice = int(input("Enter your choice \n"))
        if choice > number_to_guess:
            print(" Choice Number ", item)
            item = item + 1
            print(" \n Entered guess is greater than number your partner wants to guess ")

        elif choice < number_to_guess:
            print(" Choice Number ", item)
            item = item + 1
            print("\n Entered guess is less than number your partner wants to guess ")

        elif choice == number_to_guess:
            print(" Choice Number ", item)
            item = item + 1
            print("\n  Congrats number is equal to number your partner wants you to guess ")
            break
    else:
        print(" You have exhausted the choices ")
        break


