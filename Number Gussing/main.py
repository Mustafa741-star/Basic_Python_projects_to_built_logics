# module to generate random int, float, range, items form list and so on...
import random
# ------------Global variables---------------- 
guesses = 1

# Generate random integer numbers for guessing 
number_to_guess = random.randint(1, 100)

# guessing_game function that runs entire guessing game
def guessing_game():
    global guesses
    # Using loop to give user 10 Attempts
    for i in range(1, 11):
        # Taking user input
        user_input = input("Guess number between 1-100:) ")
        if user_input.isdigit():
            user_input = int(user_input)
            if not user_input <=0 and user_input > 100:
                print("Please type a number between 1-100!")
                exit()
        else:
            print("please type a number next time.")
            exit()
        # Checking user's guess 
        if user_input == number_to_guess:
            print(f"Your guess {user_input} is correct!")
            break
        elif user_input > number_to_guess:
            print("Your guess is high!")
            guesses +=1
            
        else:
            print("Your guess is low!")
            guesses +=1
            
    # print(guesses)
    if guesses == 10:
        print("--------Your lost!--------")
    else:
        print(f"----------You got it in {guesses} guesses------------")
        


# call the guessing_game function to start the game
guessing_game()

