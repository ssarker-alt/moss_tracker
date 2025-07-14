#Name: Suporna Sarker
#Email: SUPORNA.SARKER87@myhunter.cuny.edu
#Date: September 10, 2024
#This program draws a flower

import turtle

# Setup turtle
t = turtle.Turtle()
t.speed(7)  # Max speed
turtle.bgcolor("white")

# Function to petal drawing
def draw_petal():
    t.forward(100)  # Walk forward 100 steps
    t.left(145)     # Turn left 145 degrees
    t.forward(10)   # Walk forward 10 steps
    t.right(90)     # Turn right 90 degrees
    t.forward(10)   # Walk forward 10 steps
    t.left(135)     # Turn left 135 degrees
    t.forward(100)  # Walk forward 100 steps

# Repeat 36 times to create the complete shape
for _ in range(36):
  draw_petal()
  t.left(180)   

# Hide the turtle and finish
t.hideturtle()
turtle.done()


