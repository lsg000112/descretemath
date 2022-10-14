from tkinter import * 
import tkinter.messagebox
cnt = 0
column = []
bt = []
button = []
win = tkinter.Tk()
n = 0

def isValid(row, col): #check clicked n cells and return True if it satisfy n-queen rule
    for i in range(0, row):
        if col[i] == col[row]:
            return False
        if abs(col[i]-col[row]) == abs(i-row):
            return False
    return True

def button_click(value):
    global cnt, n, column, bt
    sValue = value.split(',')
    row = int(sValue[0])
    col = int(sValue[1])
    print(value + ' clicked')
    if cnt == n-1 and bt[n*row+col]['text'] == 'X': # if n buttons are clicked, check validity
        column[row] = col
        if isValid(n-1, column) and (-1 not in column):
            bt[n*row+col].configure(text='Queen')
            alert('Complete!')
            for i in range(n):
                bt[n*i + column[i]].configure(text='X')
            column = [-1] * n
            cnt = 0
        else:
            alert('try again')
    else:  #if not, make it queen or x
        if bt[n*row+col]['text'] == 'X':
            bt[n*row+col].configure(text='Queen')
            column[row] = col
            cnt += 1
        else:
            bt[n*row+col].configure(text='X')
            column[row] = 0
            cnt -= 1

def alert(msg):
    tkinter.messagebox.showinfo("ALERT", msg)

def pressed():
    n = int(textfield.get())

def set_n(num):
    global n, button
    n = num
    print(button)
    for i in range(4):
        for j in range(5):
            button[(i+1)*(j+1)].destroy()
    start_game()

def start_game():
    global bt, n, win, column
    win.title('N-Queen Game (' + str(n) + '*' + str(n) +')')
    column = [-1] * n
    bt = [0] * (n*n)
    for i in range(n): 
        for j in range(n):
            bt[n*i + j] = tkinter.Button(win, text = 'X', width=5, height=3, command= lambda value=str(i)+','+str(j): button_click(value))
            bt[n*i + j].grid(column=j, row=i)

if __name__ == "__main__":
    win.title('choose level (n)')
    button = [0] * 21
    for i in range(4): 
        for j in range(5):
            button[(i+1)*(j+1)] = tkinter.Button(win, text = (str)((i+1)*(j+1)), width=5, height=3, command= lambda value=(i+1)*(j+1): set_n(value))
            button[(i+1)*(j+1)].grid(column=j, row=i)
    win.mainloop()
