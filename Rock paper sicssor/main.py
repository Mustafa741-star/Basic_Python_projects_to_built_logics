# importing modules built in python
import random

#  ------------------Global varibles---------------------  
# Options
options = ("rock", "paper", "scissor")
player = None
running = True

# Loops the whole game to give expirence to play again and again 
while running:
    # reseting the player value to play again
    player = None
    # loop to take only valid input 
    while player not in options:
        # Taking user's move
        player = input("Rock, Paper, and Scissor - choose your option: ").lower()
    print(f"Player: {player}")

    # Program generating move against the user
    computer = random.choice(options)
    print("Computer choose: ",computer)

    def play_game():
        check_if_game_over()

    # checking for winner or tie
    def check_if_game_over():
        check_for_winner(player, computer)
        


    # check who won
    def check_for_winner(p, c):
        if p == c:
            print("GAME DRAW!")
        elif p == "rock" and c == "scissor":
            print("YOU WON!")
        elif p == "paper"  and c == "rock":
            print("YOU WON!")
        elif p == "scissor" and c == "paper":
            print("YOU WON!")
        else:
            print("COMPUTER WON!")
        return
    
    # Calls the play_game function 
    play_game()

    # Ask player is he want to play again or not
    if not input("Play again? (n/y): ").lower() == "y":
        running = False


print("Thank you for playing!")

