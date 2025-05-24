
import random
import time
import os

def create_board(rows, cols):
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            board[row][col] = random.choice([0, 1])
    return board

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in board:
        print(' '.join(['*' if cell else ' ' for cell in row]))

def count_neighbors(board, row, col):
    rows, cols = len(board), len(board[0])
    neighbors = 0
    for r in range(max(0, row-1), min(rows, row+2)):
        for c in range(max(0, col-1), min(cols, col+2)):
            neighbors += board[r][c]
    neighbors -= board[row][col]
    return neighbors

def next_generation(board):
    rows, cols = len(board), len(board[0])
    new_board = [[0 for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            live_neighbors = count_neighbors(board, row, col)
            if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                new_board[row][col] = 0
            elif board[row][col] == 0 and live_neighbors == 3:
                new_board[row][col] = 1
            else:
                new_board[row][col] = board[row][col]
    return new_board

def game_of_life(rows, cols, generations):
    board = create_board(rows, cols)
    for _ in range(generations):
        print_board(board)
        board = next_generation(board)
        time.sleep(0.5)

if __name__ == "__main__":
    game_of_life(20, 50, 100)
