# Simple Pong in Python 3

import turtle

wn = turtle.Screen()
wn.title("Pong by @jldohmann")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Main game loop
while True:
    wn.update()
