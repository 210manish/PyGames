from tkinter import *
from subprocess import call
import os
from PIL import Image, ImageTk;

###################################################

currentWorkingDir = os.getcwd()

###################################################

def begin():
    
    class CallPy7(object):
        
        def __init__(self,path=currentWorkingDir+"/snek_game.py"):
            self.path=path
            
        def call_python7(self):
            call(["Python3","{}".format(self.path)])
            
    
    if __name__=="__main__":
        
        m2=CallPy7()
        m2.call_python7()

###################################################

root = Tk()
root.title("Snake Game Rules")
root.resizable(False,False)
root.geometry("900x400")

imHelp1 = Image.open(r'helpZakGam1.jpg')
phHelp1 = ImageTk.PhotoImage(imHelp1)

label1 = Label(root,text="Hello there !\nMove the snake using the arrow keys\nIt becomes one unit longer each time it eats the red food\nBut make sure you dont bump it into the side of the window or into itself\nThis will end the game\nNow press the start button to play :)",fg='white', font='Mistral 18 bold', compound='center',image=phHelp1).pack(side='top')
start_button = Button(root,text="Start!",font=('consolas',40),command=begin).place(x='390',y='300')

root.mainloop()

###################################################