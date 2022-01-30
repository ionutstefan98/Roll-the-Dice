from ctypes import alignment
from tkinter import *
import random
import time
from turtle import left


dice_faces = (1, 2, 3, 4, 5, 6)
score_list = ["- ", "- ", "- ", "- ", "- ", "- ", "- ", "- ", "- ", "- "]


def roll():

    roll_time = 2
    rolled_time = 0

    while rolled_time < roll_time:
        time.sleep(0.001)
        dice_one = random.choice(dice_faces)
        dice_two = random.choice(dice_faces)
        total = dice_one + dice_two
        

        #print("Total: "+str(total))
        #print("D1: "+str(dice_one))
        #print("D2: "+str(dice_two))
        

        if dice_one == 1:
            dice1_face.config(image=dice_face1)
        elif dice_one == 2:
            dice1_face.config(image=dice_face2)
        elif dice_one == 3:
            dice1_face.config(image=dice_face3)
        elif dice_one == 4:
            dice1_face.config(image=dice_face4)
        elif dice_one == 5:
            dice1_face.config(image=dice_face5)
        elif dice_one == 6:
            dice1_face.config(image=dice_face6)

        if dice_two == 1:
            dice2_face.config(image=dice_face1)
        elif dice_two == 2:
            dice2_face.config(image=dice_face2)
        elif dice_two == 3:
            dice2_face.config(image=dice_face3)
        elif dice_two == 4:
            dice2_face.config(image=dice_face4)
        elif dice_two == 5:
            dice2_face.config(image=dice_face5)
        elif dice_two == 6:
            dice2_face.config(image=dice_face6)

        dice1_number.config(text=str(dice_one))
        dice2_number.config(text=str(dice_two))
        dices_total.config(text="Total: "+str(total))

        rolled_time += 0.1
        window.update()

    score_list.append(total)
    print(score_list)

    scoreboard()

    return total



def scoreboard():

    s1.set("1. " + str(score_list[-1]))
    s2.set("2. " + str(score_list[-2]))
    s3.set("3. " + str(score_list[-3]))
    s4.set("4. " + str(score_list[-4]))
    s5.set("5. " + str(score_list[-5]))
    s6.set("6. " + str(score_list[-6]))
    s7.set("7. " + str(score_list[-7]))
    s8.set("8. " + str(score_list[-8]))
    s9.set("9. " + str(score_list[-9]))
    s10.set("10. " + str(score_list[-10]))

    score1.config(textvariable=s1)
    score2.config(textvariable=s2)
    score3.config(textvariable=s3)
    score4.config(textvariable=s4)
    score5.config(textvariable=s5)
    score6.config(textvariable=s6)
    score7.config(textvariable=s7)
    score8.config(textvariable=s8)
    score9.config(textvariable=s9)
    score10.config(textvariable=s10)

    del score_list[0]



window = Tk()
window.geometry("640x400")

#SCORES

s1 = StringVar()
s2 = StringVar()
s3 = StringVar()
s4 = StringVar()
s5 = StringVar()
s6 = StringVar()
s7 = StringVar()
s8 = StringVar()
s9 = StringVar()
s10 = StringVar()
#-----------------------------------------------------------------------------------------------------------------

#DICE FACE PICTURES
dice_face1 = PhotoImage(file="C:\\Users\\Stefan\\Desktop\\Python Learning\\Roll the dice\\img\\dice_faces\\dice 1.png")
dice_face2 = PhotoImage(file="C:\\Users\\Stefan\\Desktop\\Python Learning\\Roll the dice\\img\\dice_faces\\dice 2.png")
dice_face3 = PhotoImage(file="C:\\Users\\Stefan\\Desktop\\Python Learning\\Roll the dice\\img\\dice_faces\\dice 3.png")
dice_face4 = PhotoImage(file="C:\\Users\\Stefan\\Desktop\\Python Learning\\Roll the dice\\img\\dice_faces\\dice 4.png")
dice_face5 = PhotoImage(file="C:\\Users\\Stefan\\Desktop\\Python Learning\\Roll the dice\\img\\dice_faces\\dice 5.png")
dice_face6 = PhotoImage(file="C:\\Users\\Stefan\\Desktop\\Python Learning\\Roll the dice\\img\\dice_faces\\dice 6.png")
#-----------------------------------------------------------------------------------------------------------------

#DICE FACE, NUMBER AND TOTAL FRAME
dice_frame = Frame(window, bd=3)
dice_frame.place(anchor="w", x=40, y=100)

dice1_face = Label(dice_frame, image=dice_face1)
dice2_face = Label(dice_frame, image=dice_face1)
dice1_face.grid(row=0, column=0)
dice2_face.grid(row=0, column=2)

dice1_number = Label(dice_frame, text="-", font=("Comic Sans", 15), width=10)
dice2_number = Label(dice_frame, text="-", font=("Comic Sans", 15), width=10)
dice1_number.grid(row=1, column=0)
dice2_number.grid(row=1, column=2)

dices_total = Label(dice_frame, text="Total: -", font=("Comic Sans", 15), width=10)
dices_total.grid(row=2, column=1)
#-----------------------------------------------------------------------------------------------------------------

#SCOREBOARD FRAME AND SCORES
scoreboard_frame = Frame(window, bd=3)
scoreboard_frame.place(anchor="e", y=150, x=600)

scoreblabel = Label(scoreboard_frame, text="SCOREBOARD", font=("Comic Sans", 12, "bold"))
scoreblabel.grid(row=0, column=0)

score1 = Label(scoreboard_frame, font=("Comic Sans", 12, "italic"), text="1. -  ", width=15)
score1.grid(row=2, column=0, columnspan=2)
score2 = Label(scoreboard_frame, font=("Comic Sans", 12, "italic"), text="2. -  ", width=15)
score2.grid(row=3, column=0, columnspan=2)
score3 = Label(scoreboard_frame, font=("Comic Sans", 12, "italic"), text="3. -  ", width=15)
score3.grid(row=4, column=0, columnspan=2)
score4 = Label(scoreboard_frame, font=("Comic Sans", 12, "italic"), text="4. -  ", width=15)
score4.grid(row=5, column=0, columnspan=2)
score5 = Label(scoreboard_frame, font=("Comic Sans", 12, "italic"), text="5. -  ", width=15)
score5.grid(row=6, column=0, columnspan=2)
score6 = Label(scoreboard_frame, font=("Comic Sans", 12, "italic"), text="6. -  ", width=15)
score6.grid(row=7, column=0, columnspan=2)
score7 = Label(scoreboard_frame, font=("Comic Sans", 12, "italic"), text="7. -  ", width=15)
score7.grid(row=8, column=0, columnspan=2)
score8 = Label(scoreboard_frame, font=("Comic Sans", 12, "italic"), text="8. -  ", width=15)
score8.grid(row=9, column=0, columnspan=2)
score9 = Label(scoreboard_frame, font=("Comic Sans", 12, "italic"), text="9. -  ", width=15)
score9.grid(row=10, column=0, columnspan=2)
score10 = Label(scoreboard_frame, font=("Comic Sans", 12, "italic"), text="10. -  ", width=15)
score10.grid(row=11, column=0, columnspan=2)
#-----------------------------------------------------------------------------------------------------------------


button_frame = Frame(window)
button_frame.place(x=200, y=220)

roll_button = Button(button_frame, text="ROLL!", command=roll)
roll_button.grid(row=3, column=1)


window.mainloop()

