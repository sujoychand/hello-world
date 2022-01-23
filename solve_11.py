""" Code with Harry :  Snake Water Gun game
    play game 10 times with while
    choose snake water gun
    depending on who is winner get points
    get scores … overall scores are calculated and displayed
"""

import random

print("****** \nWelcome to Snake , Water , Gun Game\nCreated by tester testing\n****** ")
player_1 = "Human"
print("How many chances exist per game")
chances_per_game = int(input())
i = 1  # initialize number of times games will be played
overall_tie = 0
count_player_1_wins = 0
count_comp_wins = 0
while i <= chances_per_game:
    i = i + 1
    print("Choose your choice %s \nS for Snake\nW for Water\nG for Gun" % player_1)
    choose = input()
    comp_choice_list = ("Snake", "Water", "Gun")
    comp_choice = random.choice(comp_choice_list)
    print("Computer choose: ", comp_choice)
    if choose == "S" and comp_choice == "Snake":
        print("It's a tie !")
        overall_tie = overall_tie + 1
    elif choose == "W" and comp_choice == "Water":
        print("It's a tie !")
        overall_tie = overall_tie + 1
    elif choose == "G" and comp_choice == "Gun":
        print("It's a tie !")
        overall_tie = overall_tie + 1
    elif choose == "S" and comp_choice == "Water":
        print(f"{player_1} wins !")
        count_player_1_wins = count_player_1_wins + 1
    elif choose == "W" and comp_choice == "Snake":
        print("Computer wins !")
        count_comp_wins = count_comp_wins + 1
    elif choose == "W" and comp_choice == "Gun":
        print(f"{player_1} wins !")
        count_player_1_wins = count_player_1_wins + 1
    elif choose == "G" and comp_choice == "Water":
        print("Computer wins !")
        count_comp_wins = count_comp_wins + 1
    elif choose == "G" and comp_choice == "Snake":
        print(f"{player_1} wins !")
        count_player_1_wins = count_player_1_wins + 1
    elif choose == "S" and comp_choice == "Gun":
        print("Computer wins !")
        count_comp_wins = count_comp_wins + 1
    else:
        print("you have entered wrong input")
        continue
if count_player_1_wins >= overall_tie and count_player_1_wins > count_comp_wins:
    print(f"\nOverall %s wins" % player_1, {count_player_1_wins}, " over computer")
elif count_comp_wins >= overall_tie and count_comp_wins > count_player_1_wins:
    print(f"\nOverall Computer win ", {count_comp_wins}, " over human ")
else:
    print(f"\nIts a TIE between human and computer for all chances played")





