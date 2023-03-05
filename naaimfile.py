import random
class GuessNumber:
    def __init__(num):
        num.n = random.randrange(1,100)

    def start_game(num):
        guess = int(input("Enter any number: "))
        while num.n != guess:
            if guess < num.n:
                print("Too low")
                guess = int(input("Enter number again: "))
            elif guess > num.n:
                print("Too high!")
                guess = int(input("Enter number again: "))
            else:
                break
        print("you guessed it right!!")

game = GuessNumber()
game.start_game()