from tkinter import *
import random
colours = ['Red','Blue','Green','Pink','Yellow','Orange','White','Purple','Brown','Grey']
score = 0
timeleft = 45
def start(event):  
    if timeleft == 45:
        time()
    next()
def next():
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0,END)
        random.shuffle(colours)
        label.config(fg = str(colours[1]), text = str(colours[0]))
        scoreLabel.config(text = "Score: " + str(score))
def time():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text = "Time left: "+ str(timeleft))
        timeLabel.after(1000, time)
    elif timeleft==0:
        Label1=Label(text="Thank you for playing the game \n Your score is "+str(score),font=(20)).pack()
        e.destroy()
root=Tk()
root.title("COLORGAME")
instructions =Label(root, text = "Type in the colour of the words!\nYou have 45seconds\nGet the right answer and increase your score",font=16)
instructions.pack()
scoreLabel=Label(root, text = "Press enter to start",font=24)
scoreLabel.pack()
timeLabel=Label(root, text = "Time left: " + str(timeleft),font=24)
timeLabel.pack()
label=Label(root,font=('Algerian',60),background="black")
label.pack()
e=Entry(root)
root.bind('<Return>', start)
e.pack()
e.focus_set()
root.mainloop()
