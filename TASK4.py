def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))

def find_empty_location(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None, None

def is_valid(board, num, row, col):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for x in range(3):
        for y in range(3):
            if board[start_row + x][start_col + y] == num:
                return False
    return True

def solve_sudoku(board):
    row, col = find_empty_location(board)
    if row is None:
        return True
    
    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    
    return False

if __name__ == "__main__":
    
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve_sudoku(puzzle):
        print("Sudoku puzzle solved successfully:")
        print_board(puzzle)
    else:
        print("No solution exists for the Sudoku puzzle.")
