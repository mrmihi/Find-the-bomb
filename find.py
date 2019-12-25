from tkinter import *
import tkinter.messagebox
import random

root = Tk()
root.title("Find The Bomb")
root.iconbitmap('bomb.ico')

frame = Frame(root).grid(row=5, column=1, columnspan=3)

x = random.randint(1, 9)



def bomb(bb ):
    global x
    if bb == x:
        win = Label(frame,
                    text=("IsIs: There goes my chance\n to go to Heaven !\n *sobs\n Start a new Game you won ! ")).grid(
            row=3, column=0)
        r = tkinter.messagebox.askyesno("You Won!", "You found the Bomb , Quit ? ")
        if  r == 1 :
            root.destroy()
        elif r == 0 :
            root.destroy()




    elif bb == 1 :
        press = Label(frame, text=("IsIs: Oops Not 1 !")).grid(row=1, column=0)
    elif bb == 2 :
        press = Label(frame, text=("IsIs: Oops Not 2 !")).grid(row=1, column=0)
    elif bb == 3 :
        press = Label(frame, text=("IsIs: Oops Not 3 !")).grid(row=1, column=0)
    elif bb == 4 :
        press = Label(frame, text=("IsIs: Oops Not 4 !")).grid(row=1, column=0)
    elif bb == 5 :
        press = Label(frame, text=("IsIs: Oops Not 5 !")).grid(row=1, column=0)
    elif bb == 6 :
        press = Label(frame, text=("IsIs: Oops Not 6 !")).grid(row=1, column=0)
    elif bb == 7 :
        press = Label(frame, text=("IsIs: Oops Not 7 !")).grid(row=1, column=0)
    elif bb == 8 :
        press = Label(frame, text=("IsIs: Oops Not 8 !")).grid(row=1, column=0)
    elif bb == 9 :
        press = Label(frame, text=("IsIs: Oops Not 9 !")).grid(row=1, column=0)



    x = random.randint(1, 9)



    #my = Label(root, text = x).grid(row= 4 , column = 1)

def cnt(c):
    global re
    cnt.counter += 1
    cntlebel = Label(frame,text =("IsIs: You only have "+str(10 - cnt.counter)+ " tries .")).grid(row = 2 , column = 0)
    if cnt.counter >= 10 :
       re = tkinter.messagebox.askokcancel("You Lose !","You couldn't find the bomb, Do you want to quit ?")


cnt.counter = 0


def restart():
    if re == 1:
        root.destroy()
    elif re == 0 :
        root.destroy()







button1 = Button(root, text=("1"), padx=40, pady=20, command=lambda: [bomb(1) , cnt(1) ,restart()])
button2 = Button(root, text=("2"), padx=40, pady=20, command=lambda: [bomb(2) , cnt(2) ,restart()])
button3 = Button(root, text=("3"), padx=40, pady=20, command=lambda: [bomb(3) , cnt(3) ,restart()])
button4 = Button(root, text=("4"), padx=40, pady=20, command=lambda: [bomb(4) , cnt(4) ,restart()])
button5 = Button(root, text=("5"), padx=40, pady=20, command=lambda: [bomb(5) , cnt(5) ,restart()])
button6 = Button(root, text=("6"), padx=40, pady=20, command=lambda: [bomb(6) , cnt(6) ,restart()])
button7 = Button(root, text=("7"), padx=40, pady=20, command=lambda: [bomb(7) , cnt(7) ,restart()])
button8 = Button(root, text=("8"), padx=40, pady=20, command=lambda: [bomb(8) , cnt(8) ,restart()])
button9 = Button(root, text=("9"), padx=40, pady=20, command=lambda: [bomb(9) , cnt(9) ,restart()])
creator = Label(root, text=('Mini game by m'), ).grid(row=6, column=3, columnspan=3)
story = Label(frame, text=("IsIs : My bomb travels to a another box \nonce you click a box ,\ntry to find the correct box !\n *evil laugh")).grid(row=0, column=0)

button1.grid(row=1, column=1)
button2.grid(row=1, column=2)
button3.grid(row=1, column=3)
button4.grid(row=2, column=1)
button5.grid(row=2, column=2)
button6.grid(row=2, column=3)
button7.grid(row=3, column=1)
button8.grid(row=3, column=2)
button9.grid(row=3, column=3)

root.mainloop()


