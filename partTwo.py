import random

guessing_game = random.randint(1,10)

guess = int(input("Guess an number between 1 and 10: "))
if guess > guessing_game:
    print("Too high.")
elif guess < guessing_game:
    print("Too low.")
else:
    print("You guessed correctly!")