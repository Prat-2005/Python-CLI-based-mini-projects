board = [" " for _ in range(9)]

def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("—+—+—")

def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in win_conditions:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_draw():
    return " " not in board

def play_game():
    current_player = "X"
    print("Tic-Tac-Toe Game!")
    print("Positions are numbered 0 to 8 as follows:")
    print("0|1|2")
    print("—+—+—")
    print("3|4|5")
    print("—+—+—")
    print("6|7|8\n")

    print_board()

    while True:
        try:
            move = int(input(f"\nPlayer {current_player}, enter your move (0–8): "))
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move! Try again.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        board[move] = current_player
        print_board()

        if check_winner(current_player):
            print(f"\n🎉 Player {current_player} wins!")
            break
        elif is_draw():
            print("\n🤝 It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()