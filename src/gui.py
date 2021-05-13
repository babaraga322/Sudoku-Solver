import copy
import tkinter
from tkinter import Tk, StringVar, Button, Entry, messagebox
from sudoku import Sudoku
from boards import boards
import random

# GUI window
window = Tk()

window.title("Sudoku")
window.geometry("600x600+450+120")
window.configure(bg='bisque2')
window.resizable(False, False)


# empty arrays for your Entry and StringVars

def newgame():
    msgbox = messagebox.askyesno(title='New Game', message='Are you sure?')
    if msgbox:
        initialize()


def initialize():
    # Initial board
    x = random.randint(0, len(boards) - 1)
    global board
    board = boards[x]

    # Solved board
    global solved_board
    solved_board = copy.deepcopy(board)
    Sudoku(solved_board)
    draw()


def check():
    chk = True
    for i in range(9):
        for j in range(9):

            if text_var[i][j].get().strip() == solved_board[i][j]:

                entries[i][j].config(highlightbackground="green", highlightcolor="green")
            else:
                chk = False
                entries[i][j].config(highlightbackground="red", highlightcolor="red")

    if not chk:
        messagebox.showerror(title='Incorrect', message='Try again')
    else:
        messagebox.showinfo(title='Correct', message="Nice job")


def solve(delay=120, row=0, col=0):
    if col > 8:
        col = 0
        row += 1

    if row > 8:
        return
    if text_var[row][col].get().strip() != solved_board[row][col]:
        entries[row][col].delete(0, 'end')
        entries[row][col].insert(tkinter.END, solved_board[row][col])
    entries[row][col].config(highlightbackground="green", highlightcolor="green")
    window.after(delay, lambda: solve(delay, row, col + 1))


def draw():
    global text_var
    global entries
    text_var = []
    entries = []
    x2 = 0
    y2 = 0
    rows, cols = (9, 9)
    for i in range(rows):
        # append an empty list to your two arrays
        # so you can append to those later
        text_var.append([])
        entries.append([])
        for j in range(cols):
            # append your StringVar and Entry
            text_var[i].append(StringVar())
            entries[i].append(Entry(window, textvariable=text_var[i][j], width=2, highlightthickness=2))

            entries[i][j].place(x=100 + x2, y=60 + y2)
            entries[i][j].config(font=('Helvatical bold', 25))
            x2 += 47
            # inserting board
            if board[i][j] != '.':
                entries[i][j].insert(tkinter.END, board[i][j])
                entries[i][j].config(state='disabled')

        y2 += 50
        x2 = 0


button1 = Button(window, text="New game", bg='bisque3', width=10, command=newgame)
button1.place(x=100, y=20)

button2 = Button(window, text="Check", bg='bisque3', width=10, command=check)
button2.place(x=100, y=530)

button3 = Button(window, text="Solve!", bg='bisque3', width=10, command=solve)
button3.place(x=440, y=530)
window.mainloop()
