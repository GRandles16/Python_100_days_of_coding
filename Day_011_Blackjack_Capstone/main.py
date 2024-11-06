from art import logo
import random

should_continue = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_blackjack():
    print("\n" * 20)
    print(logo)

    # setting up intial hands
    player_hand = [random.choice(cards), random.choice(cards)]
    computer_hand = [random.choice(cards), random.choice(cards)]
    player_score = player_hand[0] + player_hand[1]
    computer_score = computer_hand[0] + computer_hand[1]

    # Drawing cards for player
    continue_drawing = True
    while continue_drawing:
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        choice = input("Type 'y' to get another card: type 'n' to pass: ")
        if choice == 'n':
            continue_drawing = False

        elif choice == 'y':
            player_hand.append(random.choice(cards))
            player_score += player_hand[-1]

        # Adjust ace value from 11 to 1 if needed
        if player_score > 21:
            for card in range(0, len(player_hand)):
                if player_hand[card] == 11:
                    player_hand[card] = 1
                    player_score -= 10
                    break

            if player_score > 21:
                continue_drawing = False

    # Draw cards for computer
    if player_score < 21:
        while computer_score < 17:
            computer_hand.append(random.choice(cards))
            computer_score += computer_hand[-1]

            # Adjust ace value from 11 to 1 if needed
            if computer_score > 21:
                for card in range(len(computer_hand)):
                    if computer_hand[card] == 11:
                        computer_hand[card] = 1
                        computer_score -= 10
                        break

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

    # Compare score to find out result
    if computer_score == 21 and len(computer_hand) == 2:
        print("You lost to Blackjack!")
    elif player_score == 21 and len(player_hand) == 2:
        print("You won with Blackjack!")
    elif player_score > 21 or player_score < computer_score  <= 21:
        print("You Lose!")
    elif computer_score > 21 or player_score > computer_score:
        print("You Win!")
    else:
        print("It's a Draw!")

# play the game
while should_continue:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if play == 'n':
        should_continue = False
    elif play == 'y':
        play_blackjack()
    else:
        print("Invalid response! Try again.\n")
