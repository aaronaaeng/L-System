import turtle
from turtle import *

import DrawSystem
import LSystem
import Rule

#Original plant, 4 iterations
#ruleSet = [Rule.Rule("F", "FF+[+F-F-F]-[-F+F+F]")]
#lsys = LSystem.LSystem("F", ruleSet)

#Classic plant, 6 iterations
ruleSet = [Rule.Rule("X", " F-[[X]+X]+F[+FX]-X"), Rule.Rule("F", "FF")]
lsys = LSystem.LSystem("X", ruleSet)

#Big plant, 5 iterations, change color rules
#ruleSet = [Rule.Rule("F", "FF-[-F+F+F]+[+F-F-F]")]
#lsys = LSystem.LSystem("F", ruleSet)

#Cool shape, 4 iterations
#ruleSet = [Rule.Rule("F-F-F-F-F", "F=F-F++F+F-F-F")]
#lsys = LSystem.LSystem("F", ruleSet)


def draw():
    x = 6
    for i in range (0, x):
        lsys.generate()
    drawer = DrawSystem.DrawSystem(lsys.getSentence(), 5, 25)
    drawer.render()

draw()