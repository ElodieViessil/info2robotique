#!/usr/bin/python
import turtle
import random

N=3
bo=[]

for i in range(N):
	bo.append(turtle.Turtle())

for i in range(N):
	bo[i].penup()
	bo[i].setposition(random.randint(-200,200),random.randint(200,200))
	bo[i].setheading(random.randint(0,359))
	bo[i].color(random.random(),random.random(),random.random())
	bo[i].pendown()
	#bo[i].forward(100)

raw_input()
