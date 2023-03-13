from random import randint

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game")
print("Good luck!")
print("")

secretNum = randint(1,100)
match = 0
tries = 0

while match == 0:
    try:
        print("What's your guess between 1 and 99?")
        num = input(">> ")
        if num == "exit":
            print ("Goodbye!")
            quit()
        num = int(num)
        if num < 1 or num > 99:
            print("Invalid number")
        elif num  == secretNum:
            match = 1
        elif num > secretNum:
            print("Too high!")
        else:
            print("Too low!")
        tries += 1

    except ValueError:
        print("That's not a number.")

if (secretNum == 42):
    print("The answer to the ultimate question of life, the universe and everything is 42.")

if (tries == 1):
    print("Congratulations! You got it on your first try!")
else:
    print("Congratulations, you've got it!")
    print("You won in", tries, "attempts!")
