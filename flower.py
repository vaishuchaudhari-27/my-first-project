import colorsys
import turtle

screen = turtle . Screen()
screen.bgcolor("black")
t = turtle . Turtle()
t . speed(0)

n = 36
h = 0

for i in range(360):
    c = colorsys . hsv_to_rgb(h,1,1)
    t.color(c)
    h += 1 / n
    t.circle(180, 60)
    t. left(120)
    t.circle(180, 60)
    t. left(13)
    
turtle.done
