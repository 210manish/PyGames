import tkinter;
from PIL import Image, ImageTk;
import random;

rootzg2 = tkinter.Tk()
rootzg2.title('Guess the number!')
#rootzg2eval('tk::PlaceWindow . center')
#rootzg2iconbitmap()
rootzg2.geometry('600x400')
rootzg2.resizable(width=False,height=False)
imB = Image.open(r'bgzg2.jpg')
phB = ImageTk.PhotoImage(imB)

labelBG = tkinter.Label(rootzg2, image=phB)
labelBG.place(x=0, y=0)

TARGET = random.randint(0, 20)
RETRIES = 20
 

def update_result(text):
    result.configure(text=text)
    currentScore.configure(text="Score: {}".format(RETRIES))

def new_game():
    global TARGET, RETRIES
    TARGET = random.randint(0, 20)
    RETRIES = 20
    update_result(text="Guess a number between\n 1 and 20")

def play_game():
    global RETRIES
 
    choice = int(number_form.get())
     
    if choice != TARGET:
        RETRIES -= 1
        if RETRIES==0:
            open_popup_loss();
            new_game();
        else:
            result = "Wrong Guess!! Try Again"
            if TARGET < choice:
                hint = "The required number lies between 0 and {}".format(choice)
            else:
                hint = "The required number lies between {} and 20".format(choice)
            result = result + "\n\nHINT :\n" + hint
    else:
        result = "Your score is {}".format(RETRIES)
        result += "\n" + "Start a new game"
     
    update_result(result)

title = tkinter.Label(rootzg2,text="Guess The Number",font=("Arial",24),fg="#fffcbd",bg="#065569")

result = tkinter.Label(rootzg2, text="Guess a Number between 1 and 20!", font=("Arial", 12, "normal", "italic"),fg = "White", bg="#065569", justify=tkinter.LEFT)

imN = Image.open(r'newzg2.png')
phN = ImageTk.PhotoImage(imN)
play_button = tkinter.Button(rootzg2, image=phN, font=("Arial", 14, "bold"), fg = "Black", bg="black", command=new_game)

imG = Image.open(r'checkzg2.png')
phG = ImageTk.PhotoImage(imG)
guess_button = tkinter.Button(rootzg2,image=phG,font=("Arial",13), fg="#13d675",bg="Black", command=play_game)


guessed_number = tkinter.StringVar()
number_form = tkinter.Entry(rootzg2,font=("Arial",11),textvariable=guessed_number)

title.place(x=170, y=50)
result.place(x=180, y=210)

guess_button.place(x=350, y=147) 
play_button.place(x=250, y=320)

currentScore= tkinter.Label(rootzg2,text="Score: {}".format(RETRIES),font=("Arial", 12, "normal", "italic"),fg = "White", bg="#065569")
currentScore.place(x=170,y=100)

number_form.place(x=180, y=160)

imC = Image.open(r'confzg1.jpg')
phC = ImageTk.PhotoImage(imC)

def open_popup_loss():
    topR23= tkinter.Toplevel(rootzg2)
    topR23.geometry("300x50")
    topR23.title("Result")
    topR23.transient(rootzg2)
    topR23.lift(rootzg2)
    rootzg2_x = rootzg2.winfo_rootx()
    rootzg2_y = rootzg2.winfo_rooty()
    win_x = rootzg2_x + 300
    win_y = rootzg2_y + 100
    topR23.geometry(f'+{win_x}+{win_y}')
    tkinter.Label(topR23, text= "You lose! Try again!", font=('Mistral 18 bold'), fg='white', compound='center',
                  image=phC).pack(side=tkinter.TOP)

imHelp1 = Image.open(r'helpZakGam1.jpg')
phHelp1 = ImageTk.PhotoImage(imHelp1)

def open_help_popup_23():
    topHelp23= tkinter.Toplevel(rootzg2)
    topHelp23.geometry("650x160")
    topHelp23.resizable(width=False,height=False)
    topHelp23.title("How To Play?")
    topHelp23.transient(rootzg2)
    topHelp23.lift(rootzg2)
    rootzg2_x = rootzg2.winfo_rootx()
    rootzg2_y = rootzg2.winfo_rooty()
    win_x = rootzg2_x + 300
    win_y = rootzg2_y + 100
    topHelp23.geometry(f'+{win_x}+{win_y}')
    tkinter.Label(topHelp23, text= "You are to guess a number between 1 and 20.\nYou start with a score of 20.\nFor every wrong guess, the score decreases by '1'.\nThe sooner you guess the number, the higher the score.", font=('Mistral 18 bold'),
     fg='white', compound='center',image=phHelp1).pack(side=tkinter.TOP)

open_help_popup_23()

rootzg2.mainloop()