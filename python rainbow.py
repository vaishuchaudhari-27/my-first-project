import colorsys
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.width(2)

h = 0

for i in range(250):
    c = colorsys.hsv_to_rgb(h,1,1)
    t.color(c)
    h += 0.005
    t. forward(i * 1.5)
    t.left(59)
    
    
turtle.done()
