# Name: Suporna Sarker
# Email: SUPORNA.SARKER87@myhunter.cuny.edu
# Date: September 10, 2024
# This program draws a flower

import turtle

# Setup turtle
t = turtle.Turtle()
t.speed(11)  # Max speed
turtle.bgcolor("white")

# Function to draw a single stem
def draw_stem():
    t.forward(100)  # Walk forward 100 steps
    t.left(145)     # Turn left 145 degrees
    t.forward(10)   # Walk forward 10 steps
    t.right(90)     # Turn right 90 degrees
    t.forward(10)   # Walk forward 10 steps
    t.left(135)     # Turn left 135 degrees
    t.forward(100)  # Walk forward 100 steps
    t.right(180)    # Make sure the turtle points outward after the stem

# Repeat 36 times to create the complete flower
for _ in range(36):
    draw_stem()      # Draw a single stem
    t.left(360)       # Rotate 10 degrees to space stems evenly (360/36 = 10)

# Hide the turtle and complete the drawing
t.hideturtle()
turtle.done()

