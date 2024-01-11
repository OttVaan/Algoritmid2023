import tkinter as tk
from main import solve_sudoku

'''def print_sudoku(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(grid[i][j], end=" ")
        print()'''

def is_valid_input(value, row, col):
    if not value.isdigit() or not (1 <= int(value) <= 9):
        return False

    for i in range(9):
        if i != col and entries[row][i].get() == value:
            return False  # Check the row

        if i != row and entries[i][col].get() == value:
            return False  # Check the column

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if (i != row or j != col) and entries[i][j].get() == value:
                return False  # Check the 3x3 section

    return True

def get_user_input():
    input_grid = []
    for i in range(9):
        row = []
        for j in range(9):
            entry = entries[i][j].get()
            if is_valid_input(entry, i, j):
                row.append(int(entry))
            else:
                row.append(0)
                entries[i][j].delete(0, tk.END)  # Clear invalid input
        input_grid.append(row)
    return input_grid

def show_sudoku():
    user_input = get_user_input()
    solved_board = solve_sudoku(user_input)

    # Check if the puzzle has a solution
    if solved_board is not None:
    # Update the entries with the solved values
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, str(solved_board[i][j]))
            
    else:
        # Display a message if the puzzle has no solution
        tk.messagebox.showinfo("Sudoku Solver", "The Sudoku puzzle has no solution.")

# Create the main window
root = tk.Tk()
root.title("Sudoku Solver")

# Create an array to hold the Entry widgets
entries = [[None for _ in range(9)] for _ in range(9)]

# Create and place the Entry widgets in a 9x9 grid with 3x3 subgrids
for i in range(9):
    for j in range(9):
        validate_entry = root.register(lambda value, row=i, col=j: is_valid_input(value, row, col))
        entries[i][j] = tk.Entry(root, width=3, font=("Arial", 14), justify='center', bd=3, validate='key', validatecommand=(validate_entry, '%P'))
        entries[i][j].grid(row=i, column=j, padx=1, pady=1)
        if (i // 3 + j // 3) % 2 == 1:
            entries[i][j].configure(bg="#e0e0e0")  # Set a light background for better visibility

# Create and place the "Show Sudoku" button
show_button = tk.Button(root, text="Solve Sudoku", command=show_sudoku)
show_button.grid(row=10, columnspan=9)

# Run the Tkinter event loop
root.mainloop()
