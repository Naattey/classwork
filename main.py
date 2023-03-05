# Code 111
#
# print("Welcome")
# print("My name is Dhonmohonu")
# print("I'm trainned BOT for calculation purpose")
# userans = int (input("Your Ans: "))
#
# def corans():
#     coranswer = 10
#     userans = coranswer
#
#     print("Correct answer is: ", coranswer )
#
# corans()
#
# Code 111
# code 000
#
import random
#limited try
max = 5

#welcome note
print('''Welcome to the guess GAME

Please mention your name''')
player_name = input("User name: ")

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Set the initial number of guesses to 0
num_guesses = 0

# Loop until the player guesses the number
while True and num_guesses < max:
    # Ask the player for a guess
    guess = int(input("Guess a number between 1 and 100: "))

    # Increase the number of guesses by 1
    num_guesses += 1

    # Check if the guess is correct
    if guess == number:
        print("Congratulations, player_name , you guessed the number in", num_guesses, "guesses!")
        break
    # Check if the guess is too low
    if guess < number:
        print("Too low, try again!")
    # The guess must be too high
    else:
        print("Too high, try again!")


#

#
# code 000


# guessseachrange = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# corrans = 9
#
# newans = int (input("User answer is: "))
#
# while newans != corrans:
#     int (input("Guess Again "))
#
# else:
#     print("Right answer is: ")

