# Loop - a loop is a construct (special function) that repeats itself.
# In a programming, a loop allows to repeat code instructions.

# There are two types of loops: For loop and While loop

# While loop - a type of loop where so long as a condition is equal
# to true it will keep running "forever".

# the keyword is while --> do while

# syntax
num = 4
while 2+2 == num: # Condidtion --> operations - must be true
    print("the program is running...")
    num = int(input("Please type in a number"))

# While loops will ALWAYS run usless you change the condition!
# we can do this by writing instructions to manually change it.

def guessingGame():
    correctAnswer = 333
    attempts = 0

    print("GUESSING GAME HAS STARTED")
    userGuess = input("Please guess a number between 1 and 500.")

    while userGuess != correctAnswer:
        print("Incorrect. Please try again...")
        attempts +=1
        print("Guess attempts: " + str(attempts))
        userGuess = int(input("Please guess a number between 1 and 500."))

    print("Congrats!! you guessed the right number!!")
    
guessingGame()

