>>> #Name: Suporna Sarker (Noel)
>>> #Email: SUPORNA.SARKER87@myhunter.cuny.edu
>>> #Date: September 9, 2024
>>> #This program draws an octagon
>>> 
>>> import turtle
>>> 
>>> #Screen and Turtle object
>>> screen = turtle.Screen()
>>> t  = turtle.Turtle()
>>> 
>>> #Set turtle speed
>>> t.speed(3)
>>> 
>>> #Function to draw an octagon
>>> def draw_octagon():
...     for _ in range(8): #Loop 8 times for 8 sides of an octagon
...         t.forward(100) #Move forward 100 units
...         t.left(45) #Turn left 45 degrees to make the next angle
... 
>>> #Call the function to draw the octagon
...         
>>> draw_octagon()

>>> #End of drawing
>>> turtle.done()

>>> 
