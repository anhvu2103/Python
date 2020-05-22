import random
from Assignment7 import *
#Gametime:
playGame = True
while playGame:
    print("Let's play a game about USA States Information!")
    print("Choose your type of question: ")
    print("1. State abbreviations")
    print("2. State capital")
    print("3. Name the state from it is abbreviation")
    print("Notes: you should turn off your caps lock and make sure your input is correct")
    print("Please enter your selection: ")
    iput = input()
    #Selection1
    if iput == "1":
        print("You selected option 1 to guess the state abbreviation")
        state_1 = random.choice(StatesName) 
        print("What is the abbreviation of: ", state_1)
        input_op1 = input()
        ab = state_to_abbrev(state_1)
        if input_op1 == ab:
            print("You are correct! The abbreviation of ", state_1, " is: ", input_op1)
        else:
            print("You guessed wrong. The correct abbreviation of ", state_1, " is: ", ab)
            
    #Selection2
    if iput == "2":
        print("You selected option 2 to guess the state's capital")
        state_2 = random.choice(StatesName)
        print("What is the capital of: ", state_2)
        cap = state_to_capital(state_2)
        input_op2 = input()
        if input_op2 == cap:
            print("Correct! The answer for the capital of ", state_2, " is: ", input_op2)
        else:
            print("Incorrect! The correct answer of the capital of ", state_2, " is: ", cap)

    #Selection3
    if iput == "3":
        print("You selected option 3 to guess the state name from it is abbreviation")
        state_3 = random.choice(StatesName)
        ab1 = state_to_abbrev(state_3)
        print("What is the full name of: ", ab1)
        input_op3 = input()
        if input_op3 == state_3:
            print("Correct!")
        else:
            print("Incorrect! The correct answer is: ", state_3)

    print("Do you want to play again? Answer Y/N or y/n")
    yes_no = input()
    if yes_no == "Y" or yes_no == "y":
        playGame = True
    elif yes_no == "N" or yes_no == "n":
        print("Bye")
        playGame = False


