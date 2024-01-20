EMPTY = '-'
PLAYER_X = 'X'
PLAYER_O = 'O'

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell != EMPTY for row in board for cell in row)

def game_over(board):
    return is_winner(board, PLAYER_X) or is_winner(board, PLAYER_O) or is_draw(board)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

def minimax(board, depth, maximizing_player):
    if is_winner(board, PLAYER_X):
        return -1
    elif is_winner(board, PLAYER_O):
        return 1
    elif is_draw(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = PLAYER_O
            eval = minimax(board, depth + 1, False)
            board[i][j] = EMPTY
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = PLAYER_X
            eval = minimax(board, depth + 1, True)
            board[i][j] = EMPTY
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    best_move = None
    best_eval = float('-inf')
    for i, j in get_empty_cells(board):
        board[i][j] = PLAYER_O
        eval = minimax(board, 0, False)
        board[i][j] = EMPTY
        if eval > best_eval:
            best_eval = eval
            best_move = (i, j)
    return best_move

def main():
    board = [[EMPTY] * 3 for _ in range(3)]

    while not game_over(board):
        print_board(board)

        player_move = input("Enter your move (row and column separated by space): ")
        row, col = map(int, player_move.split())
        if board[row][col] == EMPTY:
            board[row][col] = PLAYER_X
        else:
            print("Cell already occupied. Try again.")
            continue

        if not game_over(board):
            print("Bot's move:")
            bot_move = get_best_move(board)
            board[bot_move[0]][bot_move[1]] = PLAYER_O

    print_board(board)
    winner = "You" if is_winner(board, PLAYER_X) else "Bot"
    print(f"{winner} wins!")

if __name__ == "__main__":
    main()