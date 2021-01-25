import random

randomval = random.randint(1, 3)


def randomString(i):
    switcher = {
        1: "Rock",
        2: "Paper",
        3: "Scissors"
    }
    return (switcher.get(randomval, "Invalid day of week"))


#print(randomval)


#User Guess Input variable
guessString = input("Guess Rock / Paper / Scissors: ")
if guessString == "Rock" or guessString == "Paper" or guessString == "Scissors":
    #   print("Input Correct!")

    if randomString(randomval) == guessString:
        print("It's a draw :O");

    elif randomString(randomval) == "Rock" and guessString == "Paper":
        print("Congratulations! You won!");

    elif randomString(randomval) == "Rock" and guessString == "Scissors":
        print("You lose!");

    elif randomString(randomval) == "Paper" and guessString == "Rock":
        print("You lose!");

    elif randomString(randomval) == "Paper" and guessString == "Scissors":
        print("Congratulations! You won!")

    elif randomString(randomval) == "Scissors" and guessString == "Rock":
        print("Congratulations! You won!")

    elif randomString(randomval) == "Scissors" and guessString == "Paper":
        print("You lose!")
    else:
        print("Error!")

else:
    print("Error! Incorrect Input")

print('Opponent chose: '+ randomString(randomval))