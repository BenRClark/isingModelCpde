from graphics import *
import numpy as np
import random as ran
import math

particles = []
energy = 0

for i in range(0,50):
    row = []
    for j in range(0,50):
        #row.append((ran.randint(0,1)-.5)*2)
        row.append(-1)
    particles.append(row)


win = GraphWin("IsingModel", 900, 900)

for y in range(0,900,18):
    ln = Line(Point(0,y),Point(900,y))
    ln.draw(win)

for x in range(0,900,18):
    ln = Line(Point(x,0),Point(x,900))
    ln.draw(win)
def color():
    for x in range(0,900,18):
        for y in range(0,900,18):
            rec = Rectangle(Point(x,y),Point(x+18,y+18))
            rec.draw(win)
            l = int(y/18)
            m = int(x/18)
            if particles[l][m] == 1:
                rec.setFill('red')
            elif particles[l][m] == -1:
                rec.setFill('blue')
color()

def calculate():
    nrg = 0

    for i in range(0,50):
        for j in range(0,50):

            base = particles[i][j]

            if i == 0:
                left = particles[49][j]
            else:
                left = particles[i-1][j]
            if i == 49:
                right = particles[0][j]
            else:
                right = particles[i+1][j]
            if j == 49:
                bottom = [i][0]
            else:
                bottom = particles[i][j+1]
            if j == 0:
                top = particles[i][49]
            else:
                top = particles[i][j-1]
            nrg += (-base*bottom)+(-base*top)+(-base*left)+(-base*right)

    nrg = nrg/2

    return nrg

def color1():
    rec = Rectangle(Point(xCord*18, yCord*18), Point((xCord*18) + 18, (yCord*18) + 18))
    rec.draw(win)
    if particles[xCord][yCord] == 1:
        rec.setFill('red')
    elif particles[xCord][yCord] == -1:
        rec.setFill('blue')

energy = calculate()
print(energy)

one = 0
two = 0
three = 0
for l in range(0,5000):
    energy = calculate()
    xCord = int(ran.randint(0,49))
    yCord = int(ran.randint(0,49))

    particles[xCord][yCord] = particles[xCord][yCord]*-1
    color1()
    energyNew = calculate()

    if abs(energyNew) < abs(energy):
    #if (math.exp(-(energyNew-energy))>1):
        energy = energyNew
        one = one + 1
    else:
        if (ran.uniform(0.0, 1.0) <= math.exp(-(energy - energyNew))):
            energy = energyNew
            two = two + 1
        else:
            particles[xCord][yCord] = particles[xCord][yCord] * -1
            three=1+three
            rec = Rectangle(Point(xCord * 18, yCord * 18), Point((xCord * 18) + 18, (yCord * 18) + 18))
            rec.draw(win)
            if particles[xCord][yCord] == 1:
                rec.setFill('red')
            elif particles[xCord][yCord] == -1:
                rec.setFill('blue')

color()
print(calculate())
print(one)
print(two)
print(three)

win.getMouse()
win.close()