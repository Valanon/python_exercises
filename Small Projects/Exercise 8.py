'''
https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
'''
Options = ["rock", "paper", "scissors"]
while True:
    player_1 = str(input("Player 1, input your play: ")).lower()
    player_2 = str(input("Player 2, input your play: ")).lower()
    if player_1 not in Options or player_2 not in Options:
        print("Bad game, try again with valid inputs.")
    elif player_1 == player_2:
        print("Tie game.")
    elif player_1 == "rock":
        if player_2 == "paper":
            print("Player 2 wins.")
        else:
            print("Player 1 wins.")
    elif player_1 == "paper":
        if player_2 == "rock":
            print("Player 1 wins.")
        else:
            print("Player 2 wins.")
    else:
        if player_2 == "rock":
            print("Player 2 wins.")
        else:
            print("Player 1 wins.")
    again = str(input("Would you like to play again? (Y/N): ")).lower()
    if again == "y":
        continue
    else:
        break