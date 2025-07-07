import random

def display_board(board):
    print("\n")
    print("-------------")
    for i in range(3):
        row = "|".join(f" {board[i][j]} " for j in range(3))
        print(f"|{row}|")
        print("-------------")

def update_board(board, row, col, player):
    board[row][col] = player

def check_win(board, player):
    # Check rows and columns
    for i in range(3):
        if all(cell == player for cell in board[i]) or \
                all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
            all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] not in ['X', 'O']

def get_computer_move(board):
    available = [(i, j) for i in range(3) for j in range(3) if board[i][j] not in ['X', 'O']]
    return random.choice(available) if available else (None, None)

def main():
    board = [[str(i * 3 + j + 1) for j in range(3)] for i in range(3)]
    user_symbol = 'X'
    comp_symbol = 'O'

    print("🎮 Welcome to Tic-Tac-Toe!")
    print("You are 'X' and the Computer is 'O'")
    display_board(board)

    while True:
        # User Move
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                row, col = divmod(move, 3)
                if is_valid_move(board, row, col):
                    update_board(board, row, col, user_symbol)
                    break
                else:
                    print("Invalid move, try again.")
            except (ValueError, IndexError):
                print("Please enter a valid number between 1 and 9.")

        display_board(board)

        if check_win(board, user_symbol):
            print("Congratulations! You won!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        # Computer Move
        print("Computer's turn...")
        row, col = get_computer_move(board)
        update_board(board, row, col, comp_symbol)
        print(f"Computer chose position {(row * 3 + col + 1)}")
        display_board(board)

        if check_win(board, comp_symbol):
            print("Computer wins! Better luck next time.")
            break
        if is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
