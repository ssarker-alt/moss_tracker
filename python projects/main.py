# Name: Suporna Sarker (Noel)
# Email: SUPORNA.SARKER87@myhunter.cuny.edu
# Date: September 26, 2024
# This program asks the user for the hexcode of a color and then displays a turtle that color. 

import turtle

hex_color = input("Enter a hex string: ")

screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()

t.color(hex.color)

t.begin_fill()
t.circle(50)
t.end_fill()

screen.mainloop()
