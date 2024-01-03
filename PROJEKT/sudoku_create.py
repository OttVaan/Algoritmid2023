import random
import copy

puzzle_list = []

def generate_sudoku_puzzle(difficulty):
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
    print("\nGenerated Sudoku Board:")
    print_sudoku_board(sudoku_board)

    # Print the Sudoku puzzle
    print(f"\nSudoku Puzzle (Difficulty: {difficulty}):")
    print_sudoku_puzzle(sudoku_puzzle)

    return sudoku_puzzle

# Example usage:
difficulty_level = input("--Select difficulty--\n easy, medium, hard\n---------------------\ndifficulty:")
sudoku_puzzle = generate_sudoku_puzzle(difficulty_level)

#Sudoku puzzle on embeded list, mida saab lahendus algoritmile sisse sööta.
print(sudoku_puzzle)

