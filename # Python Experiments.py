# Right triangle mosaic generator

# ----Imports
import turtle
turtle.colormode(255)
import random
import time
import math
from random import randrange

# ----Var Declarations for script
rand = random.randint
trtl = turtle.Turtle()
trtl.speed(10)
trtl.shape("turtle")
rad2degrees = 180/math.pi


#------Prompting the player on the number of triangles they'd like
print("How many triangles would you like?")
triangles_desired = input()

#------Making sure the player gave a valid int with base 10
if triangles_desired.isnumeric() == True:
    triangles_desired = int(triangles_desired)
else:   
    print("Uh Oh! What you gave me is not a integer, please rerun the program and try again :/ ")
    exit()

#------Prompting the player on what color they'd like
print("What color would you like? If you'd like random colors, simply type 'random.'")
color_desired = input()
if color_desired != "random":
    trtl.color(color_desired)


#------Asking the player if they'd like their triangles filled
print("Would you like me to fill in the triangles as I draw them? -type yes or no-")
fill_desired = input()
if fill_desired != "yes" and fill_desired != "no":
    print("Uh Oh! You did not give me a valid response, please rerun the program and respond to the previous question with a yes or no.")
    exit()
else:
# -----Generate Triangle function
    def generate_triangle():
        x = rand(1,200)
        y = rand(1,200)
        x_squared = x ** 2
        y_squared = y ** 2
        q = x_squared + y_squared
        z = math.isqrt(q)
        theta = math.atan(y/x) * rad2degrees
        beta = math.atan(x/y) * rad2degrees
        if fill_desired == "yes":
            if color_desired == "random":
                trtl.fillcolor(rand_color)
                trtl.begin_fill()
            else:
                trtl.fillcolor(color_desired)
                trtl.begin_fill()
        trtl.left(90)
        trtl.forward(y)
        trtl.right(180 - beta)
        trtl.forward(z)
        trtl.right(180 - theta)
        trtl.forward(x)
        trtl.end_fill()


# -----Mosaic Generator using a 'while' loop
i = 0
while i < triangles_desired:
    if color_desired == "random":
        rand_color = random.choices(range(255), k=3)
        trtl.color(rand_color)
    x_cor = rand(-200,200)
    y_cor = rand(-200,200)
    trtl.penup()
    trtl.goto(x_cor,y_cor)
    trtl.right(rand(0,360))
    trtl.pendown()
    generate_triangle()
    i += 1
    print("This is triangle " + str(i) +"!")


#-----Ending the program
print("Thank you for using my script, credit goes to Tropica")
time.sleep(10)
exit()

