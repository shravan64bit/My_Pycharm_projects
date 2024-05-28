import turtle as t
import random

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(number_sides):
    angle = 360 / number_sides
    t.color(random.choice(colours))
    for i in range(number_sides):
        t.forward(100)
        t.right(angle)



for number_sides in range(3, 11):
    draw_shape(number_sides)
t.exitonclick()