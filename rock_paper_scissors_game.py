import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice, player_name):
    if (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return f"{player_name} win!"
    elif player_choice == computer_choice:
        return "It's a tie"
    else:
        return "Computer win!"

def one_round(player_score, computer_score, player_name):
    player_choice = input("Enter rock, paper, or scissors: ")
    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        return player_score, computer_score

    computer_choice = get_computer_choice()
    print(f"{player_name} chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(player_choice, computer_choice, player_name)
    print(result)

    if result == f"{player_name} win!":
        player_score += 1
    elif result == "Computer win!":
        computer_score += 1

    return player_score, computer_score

def best_of_three(player_score, computer_score, player_name):
    rounds_played = 0

    while rounds_played < 3:
        player_choice = input("Enter rock, paper, or scissors: ")
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"{player_name} chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice, player_name)
        print(result)

        if result == f"{player_name} win!":
            player_score += 1
        elif result == "Computer win!":
            computer_score += 1

        rounds_played += 1
        print(f"Round {rounds_played} Over.")

    if player_score > computer_score:
        print(f"{player_name} win the best of three!")
    elif computer_score > player_score:
        print("Computer wins the best of three!")
    else:
        print("It's a tie in the best of three!")

    return player_score, computer_score

def main():
    player_score = 0
    computer_score = 0
    player_name = input("Enter player name:")

    while True:
        print("Choose game mode:")
        print("1. Only One Round")
        print("2. Best of Three")
        mode = int(input("Enter your choice: "))

        if mode == 1:
            player_score, computer_score = one_round(player_score, computer_score, player_name)
        elif mode == 2:
            player_score, computer_score = best_of_three(player_score, computer_score, player_name)
        else:
            print("Invalid choice. Please try again.")
            continue

        print(f"Score - {player_name}: {player_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again != "yes":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()