# import random module to generate random num. and import tkinter for creating gui app.
import random
from tkinter import *
from tkinter import ttk
import turtle

#creating window of game
root = Tk()
root.title("Rock Paper Scissors Game")
root.maxsize(700,600)
root.config(bg="steelblue")
frame = Frame(root,width=600,height=380,bg="black")
frame.grid(row=0, column=0, padx=5, pady=5)
canvas=Canvas(root,width=600,height=200,bg="white")
canvas.grid(row=1, column=0, padx=5, pady=5)
turtle=turtle.RawTurtle(canvas)
turtle.ht()
turtle.penup()
turtle.goto(15,20)
turtle.pendown()
turtle.color("orange")
turtle.write("Rules:", align="center", font=("Arial", 13, "italic","bold"))
turtle.penup()
turtle.penup()
turtle.goto(30,-20)
turtle.pendown()
turtle.color("green")
turtle.write("Rock vs paper->paper wins, Rock vs scissor->Rock wins", align="center", font=("Arial", 13, "italic","bold"))
turtle.penup()
turtle.goto(0,-40)
turtle.pendown()
turtle.write(", paper vs scissor->scissor wins", align="center", font=("Arial", 13, "italic","bold"))
def Rock():
	turtle.clear()
	turtle.color("steelblue")
	choice=1
	choice_name='Rock'
	comp_choice = random.randint(1, 3) 
	
	# looping until comp_choice value 
	# is equal to the choice value 
	while comp_choice == choice: 
		comp_choice = random.randint(1, 3) 

	# initialize value of comp_choice_name 
	# variable corresponding to the choice value
	if comp_choice == 2:
		comp_choice_name = 'paper'
	else: 
		comp_choice_name = 'scissor'
	turtle.penup()
	turtle.goto(30, -30)
	turtle.pendown()
	# condition for winning
	if((choice == 1 and comp_choice == 2) or
	(choice == 2 and comp_choice ==1 )):
		turtle.write("paper win", align="center", font=("Arial", 13, "italic","bold"))
		result = "paper"

	elif((choice == 1 and comp_choice == 3) or
		(choice == 3 and comp_choice == 1)):
		turtle.write("rock win", align="center", font=("Arial", 13, "italic", "bold"))
		result = "Rock"
	else:
		turtle.write("scissor win", align="center", font=("Arial", 13, "italic","bold"))
		result = "scissor"
	turtle.penup()
	turtle.goto(0, -65)
	turtle.pendown()
	# Printing either user or computer wins
	if result == choice_name:
		turtle.write("<== User wins ==>", align="center", font=("Arial", 13, "italic","bold"))
	else:
		turtle.write("<== Computer wins ==>", align="center", font=("Arial", 13, "italic","bold"))


def Scissor():
	turtle.color("steelblue")
	turtle.clear()
	choice = 3
	choice_name = 'scissor'
	comp_choice = random.randint(1, 3)

	# looping until comp_choice value
	# is equal to the choice value
	while comp_choice == choice:
		comp_choice = random.randint(1, 3)

	# initialize value of comp_choice_name
	# variable corresponding to the choice value
	if comp_choice == 2:
		comp_choice_name = 'paper'
	else:
		comp_choice_name = 'Rock'
	turtle.penup()
	turtle.goto(30, -30)
	turtle.pendown()
	# condition for winning
	if ((choice == 1 and comp_choice == 2) or
			(choice == 2 and comp_choice == 1)):
		turtle.write("paper win", align="center", font=("Arial", 13, "italic", "bold"))
		result = "paper"

	elif ((choice == 1 and comp_choice == 3) or
		  (choice == 3 and comp_choice == 1)):
		turtle.write("rock win", align="center", font=("Arial", 13, "italic", "bold"))
		result = "Rock"
	else:
		turtle.write("scissor win", align="center", font=("Arial", 13, "italic", "bold"))
		result = "scissor"
	turtle.penup()
	turtle.goto(0, -65)
	turtle.pendown()
	if result == choice_name:
	    turtle.write("<== User wins ==>", align="center", font=("Arial", 13, "italic", "bold"))
	else:
	    turtle.write("<== Computer wins ==>", align="center", font=("Arial", 13, "italic", "bold"))


def Paper():
	turtle.color("steelblue")
	turtle.clear()
	choice = 2
	choice_name = 'paper'
	comp_choice = random.randint(1, 3)

	# looping until comp_choice value
	# is equal to the choice value
	while comp_choice == choice:
		comp_choice = random.randint(1, 3)

	# initialize value of comp_choice_name
	# variable corresponding to the choice value
	if comp_choice == 1:
		comp_choice_name = 'Rock'
	else:
		comp_choice_name = 'scissor'

	# condition for winning
	turtle.penup()
	turtle.goto(30, -30)
	turtle.pendown()
	# condition for winning
	if ((choice == 1 and comp_choice == 2) or
			(choice == 2 and comp_choice == 1)):
		turtle.write("paper win", align="center", font=("Arial", 13, "italic", "bold"))
		result = "paper"

	elif ((choice == 1 and comp_choice == 3) or
		  (choice == 3 and comp_choice == 1)):
		turtle.write("rock win", align="center", font=("Arial", 13, "italic", "bold"))
		result = "Rock"
	else:
		turtle.write("scissor win", align="center", font=("Arial", 13, "italic", "bold"))
		result = "scissor"
	turtle.penup()
	turtle.goto(0, -65)
	turtle.pendown()
	if result == choice_name:
	    turtle.write("<== User wins ==>", align="center", font=("Arial", 13, "italic", "bold"))
	else:
	    turtle.write("<== Computer wins ==>", align="center", font=("Arial", 13, "italic", "bold"))

button=Button(frame, text="Rock", fg="white", command=Rock, bg="black").grid(row=1, column=1,padx=5,pady=5)
button=Button(frame, text="Paper", fg="white", command=Paper, bg="black").grid(row=1, column=2,padx=5,pady=5)
button=Button(frame, text="Scissor", fg="white", command=Scissor, bg="black").grid(row=1, column=3,padx=5,pady=5)
root.mainloop()