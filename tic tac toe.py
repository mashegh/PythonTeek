import tkinter as tk
from tkinter import messagebox
game_board =[['','','',],
                            ['','','',],
                            ['','','',]]
current_player='X'
def button_click(row,col):
    global current_player
    if game_board[row] [col] =='':
        buttons [row] [col].config(text=current_player)
        game_board [row] [col]=current_player
        if check_winner(current_player) :
            messagebox.showinfo('tic tac toe',f' player{current_player} wins')
        elif  check_tie():
            messagebox.showinfo('tic tac toe','dude you need to be op not to make a tie')
        elif current_player =='X':
            current_player ='O'
        elif current_player =='O':
            current_player ='X'

def check_winner(player):
    for row in range(3):
        if game_board[row][0] == player and game_board[row][1] == player and game_board[row][2] == player:
            return True
  
    for col in range(3):
        if game_board[0][col] == player and game_board[1][col] == player and game_board[2][col] == player:
            return True
        if game_board[0][0] == player and game_board[1][1] == player and game_board[2][2] == player:
            return True
        if game_board[0][2] == player and game_board[1][1] == player and game_board[2][0] == player:
            return True
            
def check_tie():
    for row in range(3):
        for col in range(3):
            if game_board[row][col] == '':
                return False
    return True
window = tk.Tk()
window.title('tic tac toe')
buttons = []
for row in range(3):
    row_buttons =[]
    for col in range(3):
        button = tk.Button(window, width=10, heigh=5, command=lambda r=row,c=col: button_click(r,c))
        button.grid(row=row,column=col)
        row_buttons.append(button)
    buttons. append(row_buttons)
tk.mainloop()
                
