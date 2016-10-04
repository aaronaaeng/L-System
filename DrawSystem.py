import turtle
from turtle import *

import State



class DrawSystem:
    todo = None
    len = None
    theta = None
    Stack = []

    def __init__(self, s, l, t):
        self.todo = s
        self.len = l
        self.theta = t

    def render(self):
        pen1 = Pen()
        pen1.hideturtle()
        pen1.speed(0)
        pen1.pensize(2)
        pen1.left(90)
        pen1.penup()
        pen1.goto(0, -400)
        pen1.pendown()
        pen1.screen.bgcolor("#ffffff")
        pen1.color("#996633")
        #turtle.tracer(0.0)
        turtle.resizemode("auto")
        for i in range (0, len(self.todo)):

            #if i+1 < len(self.todo):
            #    if self.todo[i+1] == "]":
            #        pen1.color("#009933")
            c = self.todo[i]
            if c == "F":
                pen1.forward(self.len)
            elif c == "+":
                pen1.right(self.theta)
            elif c == "-":
                pen1.left(self.theta)
            elif c == "[":
                self.Stack.append(State.State(pen1.xcor(), pen1.ycor(), pen1.heading()))
                print("push")
                self.len *= .9
            elif c == "]":
                pen1.penup()

                last = len(self.Stack) - 1
                pen1.goto(self.Stack[last].x, self.Stack[last].y)
                pen1.setheading(self.Stack[last].theta)
                self.Stack.pop()
                pen1.pendown()
                print ("pop")
                self.len *= 1/.9
            if len(self.Stack) > 4:
                pen1.color("#31932D")
            elif len(self.Stack) > 2:
                pen1.color("#478650")
            else:
                pen1.color("#996633")
        turtle.mainloop()
