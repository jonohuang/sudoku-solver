
### UI Implementation with `tkinter`

import tkinter as tk
from tkinter import messagebox

def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def solve():
    board = [[0] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            value = entries[i][j].get()
            if value.isdigit() and value != "":
                board[i][j] = int(value)
            else:
                board[i][j] = 0

    if solve_sudoku(board):
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, str(board[i][j]))
    else:
        messagebox.showinfo("Result", "No solution exists.")

# Create the main window
root = tk.Tk()
root.title("Sudoku Solver")

# Create a 9x9 grid of entry boxes
entries = [[None] * 9 for _ in range(9)]
for i in range(9):
    for j in range(9):
        entries[i][j] = tk.Entry(root, width=3, font=('Arial', 18), justify='center')
        entries[i][j].grid(row=i, column=j)

# Solve button
solve_button = tk.Button(root, text="Solve", command=solve, font=('Arial', 14))
solve_button.grid(row=9, column=0, columnspan=9)

# Run the application
root.mainloop()
