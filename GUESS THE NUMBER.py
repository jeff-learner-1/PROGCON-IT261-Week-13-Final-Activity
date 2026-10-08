import random
def displayWelcome():
    print("=== WELCOME TO THE LUCKY NUMBER GAME ===")
    print("Guess a number between 1 and 10. You have 3 tries!")

def getSecretNumber():
    secret = int(random.random() * 10) + 1
    
    return secret

def playGame(secret):
    attempts = 0
    maxAttempts = 3
    hasWon = False
    while attempts < maxAttempts and hasWon == False:
        print("Hey bro, enter your move (1-9):")
        guess = int(input())
        attempts = attempts + 1
        if guess == secret:
            print("You win! You are the GOAT, you're so good!")
            hasWon = True
        else:
            if guess < secret:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
    if hasWon == False:
        print("Game Over! The secret number was: " + str(secret))

# Main
displayWelcome()
secretNumber = getSecretNumber()
playGame(secretNumber)
