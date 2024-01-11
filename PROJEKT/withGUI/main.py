#import random
#import copy
import time

#puzzle_list = []

'''def generate_sudoku_puzzle(difficulty):
    def generate_sudoku_board():
        # Initialize a 9x9 Sudoku board with zeros
        board = [[0 for _ in range(9)] for _ in range(9)]

        # Fill the diagonal boxes with valid values
        fill_diagonal_boxes(board)

        # Fill the remaining cells
        fill_remaining_cells(board, 0, 3)

        return board

    def fill_diagonal_boxes(board):
        for i in range(0, 9, 3):
            fill_box(board, i, i)

    def fill_box(board, row, col):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(values)

        index = 0
        for i in range(3):
            for j in range(3):
                board[row + i][col + j] = values[index]
                index += 1

    def is_safe(board, row, col, num):
        # Check if the number is not present in the current row and column
        if num not in board[row] and all(board[i][col] != num for i in range(9)):
            # Check if the number is not present in the 3x3 box
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False
            return True

        return False

    def fill_remaining_cells(board, row, col):
        if row == 9:
            return True

        if col == 9:
            return fill_remaining_cells(board, row + 1, 0)

        if board[row][col] != 0:
            return fill_remaining_cells(board, row, col + 1)

        for num in range(1, 10):
            if is_safe(board, row, col, num):
                board[row][col] = num
                if fill_remaining_cells(board, row, col + 1):
                    return True
                board[row][col] = 0

        return False

    def create_puzzle(board, difficulty):
        global puzzle_list
        puzzle = copy.deepcopy(board)

        if difficulty == 'easy':
            num_cells_to_remove = 30
        elif difficulty == 'medium':
            num_cells_to_remove = 40
        elif difficulty == 'hard':
            num_cells_to_remove = 50
        else:
            raise ValueError("Invalid difficulty level. Choose 'easy', 'medium', or 'hard'.")

        remove_cells(puzzle, num_cells_to_remove)

        puzzle_list = puzzle
        return puzzle

    def remove_cells(puzzle, num_cells_to_remove):
        for _ in range(num_cells_to_remove):
            while True:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
                if puzzle[row][col] != 0:
                    puzzle[row][col] = 0
                    break

    def print_sudoku_board(board):
        for row in board:
            print(' '.join(map(str, row)))

    def print_sudoku_puzzle(puzzle):
        for row in puzzle:
            print(' '.join(map(lambda x: str(x) if x != 0 else '.', row)))
            

    # Generate a Sudoku board
    sudoku_board = generate_sudoku_board()

    # Create a Sudoku puzzle based on difficulty
    sudoku_puzzle = create_puzzle(sudoku_board, difficulty)

    # Print the original Sudoku board
    #print("\nGenerated Sudoku Board:")
    #print_sudoku_board(sudoku_board)

    # Print the Sudoku puzzle
    print(f"\nSudoku Puzzle (Difficulty: {difficulty}):")
    print_sudoku_puzzle(sudoku_puzzle)

    return sudoku_puzzle'''

def solve_sudoku(board):
    def is_valid(row, col, num):
        # Check if the number is not present in the current row, column, and 3x3 box
        return (
            num not in board[row] and
            all(board[i][col] != num for i in range(9)) and
            all(board[i][j] != num for i in range(3 * (row // 3), 3 * (row // 3 + 1))
                for j in range(3 * (col // 3), 3 * (col // 3 + 1))
            )
        )

    def find_empty_location():
        # Find the first empty location on the board with the minimum remaining values
        empty_locations = [(i, j, len([num for num in range(1, 10) if is_valid(i, j, num)]))
                           for i in range(9) for j in range(9) if board[i][j] == 0]
        if not empty_locations:
            return None, None
        return min(empty_locations, key=lambda x: x[2])[:2]

    row, col = find_empty_location()

    # If no empty location is found, the puzzle is solved
    if row is None:
        return board

    # Try numbers 1 to 9 for the empty location
    for num in range(1, 10):
        if is_valid(row, col, num):
            # Place the number on the board
            board[row][col] = num

             # Recursively solve the Sudoku puzzle
            result = solve_sudoku(board)
            
            if result is not None:
                return result  # Return the solved Sudoku board

            # If the current placement doesn't lead to a solution, backtrack
            board[row][col] = 0

    # If no number leads to a solution, backtrack
    return False

#def print_sudoku_grid(board):
    #for row in board:
        #print(' '.join(map(str, row)))

# Measure the time it takes to solve the Sudoku puzzle
start_time = time.time()

# Example usage:
#difficulty_level = input("--Select difficulty--\n easy, medium, hard\n---------------------\ndifficulty:")
#sudoku_puzzle = generate_sudoku_puzzle(difficulty_level)

# Print the original Sudoku puzzle
#print("\nSudoku Puzzle (Difficulty: {}):".format(difficulty_level))
#print(sudoku_puzzle)

# Solve the Sudoku puzzle
'''if solve_sudoku(sudoku_puzzle):
    print("\nSudoku Puzzle Solved:")
    print_sudoku_grid(sudoku_puzzle)
    #print(sudoku_puzzle)
    elapsed_time = time.time() - start_time
    print("\nTime taken to solve: {:.6f} seconds".format(elapsed_time))
else:
    print("\nNo solution found.")'''