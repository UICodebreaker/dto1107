import random
valid = False

#tutorial segment
print("Welcome to Odds or Evens!")
name = input("Please enter your name: ")
played_before = input("Have you played before? (Y/N): ").lower()

while not valid:
    try:
        #explaining game
        if played_before == "n" or played_before == "no":
            print("""The rules of the game are quite simple: You pick to be either Odds or Evens, and the computer picks the other side.
            When a round is run, you must pick between a range of numbers, and the computer will do the same.
            After which, both numbers added together, if the result is Odd, whoever picked Odd wins and vice versa.
            The game ends after 5 rounds or if the user quits.""")
            valid = True
        elif played_before == "y" or played_before == "yes":
            print("Ready for another round?")
            valid = True
        else:
            played_before = input("Invalid input: Please input Yes or No ").lower()
    except ValueError:
        print("Error, invalid input: Please input Yes or No ")
#choosing sides
valid = False
#breaks when pressing enter or inputting anything other than numbers, no idea how to fix
player_side = int(input("Please input 1 (Odds) or 2 (Evens) to continue. "))

while not valid:
    try:
        if player_side == 1:
            valid = True
        elif player_side == 2:
            valid = True
        else:
            print("Error, invalid number please input 1 or 2")
            player_side = int(input("Please input 1 (Odds) or 2 (Evens) to continue "))
    except ValueError:
        print("Error, invalid input, please input 1 or 2 ")

#playing rounds
#variables for while loop
rounds_played = 0
player_wins = 0
com_wins = 0
valid = False
wins = []
while not valid:
    #yet again, breaks when pressing enter. i don't really care enough to fix it.
    roll_round = int(input("Input a number between 1 and 10 or 0 to quit "))

    if 1 <= roll_round <= 10:
        rounds_played += 1
        #computer choice
        com_choice = random.randint(1, 10)

        #adding and checking results
        result = roll_round + com_choice
        if result % 2 == 0:
            print("Round {}".format(rounds_played))
            print("{} picked {}, and the computer picked {}, resulting in {}".format(name, roll_round, com_choice, result))
            #checks to see if the player side is even or odd
            if player_side == 2:
                print("You win, {}!".format(name))
                wins.insert(0, "{} won round {}".format(name, rounds_played))
                player_wins += 1
            else:
                print("Computer wins!")
                wins.insert(0, "Computer won round {}".format(rounds_played))
                com_wins += 1
        #game ends past round 5 and subtracts from "rounds_played" for consistency
        elif rounds_played >= 5:
            rounds_played -= 1
            print("Maximum rounds reached!")
            break
        else:
            print("Round {}".format(rounds_played))
            print("{} picked {}, and the computer picked {}, resulting in {}".format(name, roll_round, com_choice, result))
            if player_side == 1:
                print("You win, {}!".format(name))
                wins.insert(0, "{} won round {}".format(name, rounds_played))
                player_wins += 1
            else:
                print("Computer wins!")
                wins.insert(0, "Computer won round {}".format(rounds_played))
                com_wins += 1
    #exit code essentially
    elif roll_round == 0:
        break
    else:
        print("Error! Invalid input!")
        roll_round = int(input("Input a number between 1 and 10 or 0 to quit "))
print("The scores are as follows..")
wins.reverse()
#score display, im lazy as hell so this works fine.
print("The round results are in.. {}".format(wins))
print("In total, {} won {} times!".format(name, player_wins))
print("And the computer won {} times!".format(com_wins))
prizes = ['An Iphone', 'A Car', 'A Mountain bike', 'Some money', 'An overseas trip', 'Some movie tickets', 'A motorbike', 'Some westfield vouchers']
if player_wins > com_wins:
    #win against computer, win iphone, seems about right.
    print("Well done! You've beaten the computer!")
    print("That deserves a reward, don't you think?")
    print("""Possible rewards include:
    An Iphone
    A car
    A mountain bike
    Lots of money
    An overseas trip
    Some movie tickets
    A motorbike
    or Westfield Vouchers""")
    #this is incredibly ineffective, but i cant think of anything better.
    reward = random.randint(0, 7)
    if reward == 0:
        prize = prizes[0]
    elif reward == 1:
        prize = prizes[1]
    elif reward == 2:
        prize = prizes[2]
    elif reward == 3:
        prize = prizes[3]
    elif reward == 4:
        prize = prizes[4]
    elif reward == 5:
        prize = prizes[5]
    elif reward == 6:
        prize = prizes[6]
    else:
        prize = prizes[7]
    print("And your prize is.. {}!".format(prize))
else:
    print("Better luck next time!")
print("Thank you for playing, come again any time!")
