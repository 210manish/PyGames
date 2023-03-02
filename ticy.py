from tkinter import *
from tkinter import messagebox
import random

###########################################################################

def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))
                messagebox.showinfo(title="Result : ",message=players[0]+" wins")

            elif check_winner() == "Tie":
                label.config(text="Tie!")
                messagebox.showinfo(title="Result : ",message="Tie!")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))
                messagebox.showinfo(title="Result : ",message=players[1]+" wins")

            elif check_winner() == "Tie":
                label.config(text="Tie!")
                messagebox.showinfo(title="Result : ",message="Tie!")

###########################################################################

def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False

###########################################################################

def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

###########################################################################

def new_game():

    global player

    player = random.choice(players)

    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")

###########################################################################

def manGam1Help():
    topManGame1=Toplevel(rootmg2ticy)
    topManGame1.title("Help")
    topManGame1.resizable(False,False)
    ManLabel1=Label(topManGame1, text= "Welcome to Tic-Tac_Toe").pack(side=TOP)
    ManLabel2=Label(topManGame1, text= "The game is played on a grid thats 3 squares by 3 squares.").pack(side=TOP)
    ManLabel3=Label(topManGame1, text= "One player is X and the other is O.").pack(side=TOP)
    ManLabel4=Label(topManGame1, text= "Players take turns putting their marks in empty squares.").pack(side=TOP)
    ManLabel5=Label(topManGame1, text= "The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner").pack(side=TOP)  
    ManLabel6=Label(topManGame1, text= "Otherwise when all 9 squares are full, the game is over and it is a Tie!").pack(side=TOP)                              


###########################################################################

rootmg2ticy = Tk()
rootmg2ticy.title("Tic-Tac-Toe")
rootmg2ticy.resizable(False,False)
players = ["x","o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=player + " turn", font=('consolas',40))
label.pack(side="top")

help_button = Button(text="Rules",font=('consolas',20), command=manGam1Help).pack(side="top")

reset_button = Button(text="Restart", font=('consolas',20), command=new_game)
reset_button.pack(side="top")

frame = Frame(rootmg2ticy)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

rootmg2ticy.mainloop()

