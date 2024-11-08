from art import logo
from random import randint

num = randint(1, 100)
lives = 10

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
still_playing = True

if difficulty == 'hard':
    lives = 5

while lives > 0 and still_playing:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess > num:
        print("Too high.")
        lives -= 1
    elif guess < num:
        print("Too low.")
        lives -= 1
    else:
        print(f"You got it! The answer was {num}.")
        still_playing = False

if lives == 0:
    print("You lose. The answer was {num}.")
