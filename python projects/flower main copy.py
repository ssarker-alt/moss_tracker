# Name: Suporna Sarker (Noel)
# Email: SUPORNA.SARKER87@myhunter.cuny.edu
# Date: September 10, 2024
# This program draws a flower 

import turtle

# Create a turtle object
tur = turtle.Turtle()
tur.speed(9)  #speed 

# Function to draw stems of the flower
def draw_flower():
    tur.forward(100)  # Walk forward 100 steps
    tur.left(145)     # Turn left 145 degrees
    tur.forward(10)   # Walk forward 10 steps
    tur.right(90)     # Turn right 90 degrees
    tur.forward(10)   # Walk forward 10 steps
    tur.left(135)     # Turn left 135 degrees
    tur.forward(100)  # Walk forward 100 steps
    
# Repeat 36 times to create 36 stems
for _ in range(36):
    draw_flower()

# Hide the turtle and display the result
turtle.done()
