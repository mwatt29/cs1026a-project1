'''
Murray Watt
mwatt29@uwo.ca
251341261
This code intends to fufill the first part of Assignment 1, creating a simple guessing game using an algorithim, 
while following a set table of values that must be outputed specifically. 
'''
def GuessNumber():
    print("Project One (01) : Guess a Number\n")

    #Get user input
    UserNumber = int(input("Enter a whole number between 1 and 100 (inclusive): "))

    #Set variables
    LowerBound = 1
    Upperbound = 100
    ComputerGuess = 50
    tries = 1

    #Start of main loop, to guess the number
    while True:

        #Display computers current guess
        print(f"\nThe Computer Guessed: {ComputerGuess}")

        #Check if guess is correct
        if ComputerGuess == UserNumber:
            print(f"Number {UserNumber} is the number I was thinking of.")
            print(f"You found this after {tries} tries.\n")
            # End of loop if guess is correct
            break
        # Adjust the range based on users response
        elif ComputerGuess < UserNumber:
            print(f"The number I am thinking of is higher than {ComputerGuess}\n")
            LowerBound = ComputerGuess + 1
        else:
            print(f"The number I am thinking of is less than {ComputerGuess}\n")
            UpperBound = ComputerGuess - 1

        # Calculate the next guess to follow the table of values
        if (UpperBound - LowerBound) % 4 == 0:
            ComputerGuess = (LowerBound + UpperBound) // 2
        else:
            ComputerGuess = (LowerBound + UpperBound) // 2 + 1

        #Increment number of tries
        tries += 1

    print("END: Project One (01)")

# Run the game
GuessNumber()

    
 
