from p5 import *
import time
import math

class Grid:
    def __init__(self, translateX, translateY, main=False, rotate=0, background=(0, 0, 0), color=(192, 192, 192), mutedcolor=(117, 117, 117), gridspace=100, filler=True, boldstroke=2, lightstroke=1, animate=True, extra=300, animatespeed=8, shear=(0, 0), scale=1, keepcontained=False):
        self.translateX = translateX
        self.translateY = translateY
        self.background = background
        self.color = color
        self.gridspace = gridspace
        self.filler = filler
        self.boldstroke = boldstroke
        self.lightstroke = lightstroke
        self.mutedcolor = mutedcolor
        self.ix = 0
        self.iy = 0
        self.division = 100
        self.counter = 0
        self.speed = animatespeed
        self.rotate = rotate
        self.animate = animate
        self.extra = extra
        self.shear = shear
        self.scale = scale
        self.keepcontained = keepcontained
        self.main = main
        self.animation_done = False

    def drawY(self, x):
        scale = self.counter/self.division
        line((x, -(self.translateY + self.extra)*scale), (x, (height + self.extra - self.translateY)*scale))

    def drawX(self, y):
        scale = self.counter/self.division
        line((-(self.translateX + self.extra)*scale, y), ((width + self.extra - self.translateX)*scale, y))

    def create(self):
        background(self.background[0], self.background[1], self.background[2])
        stroke(self.color[0], self.color[1], self.color[2])

        translate(self.translateX, self.translateY)
        stroke_weight(self.boldstroke)
        point(0, 0)


        push_matrix()

        if self.main:
            scale(self.scale, -self.scale)

        rotate(self.rotate)
        shear_x(self.shear[0])
        shear_y(self.shear[1])



        # Main Lines: X Axis and Y Axis
        self.drawY(0) # Y Axis

        self.drawX(0) # X Axis

        stroke_weight(self.lightstroke)
        stroke(self.mutedcolor[0], self.mutedcolor[1], self.mutedcolor[2])

        if self.filler:

            # Y Axis Fillers
            for i in range(1, ((width+self.extra)//self.gridspace - 1)):
                self.drawY(self.gridspace*i)
                self.drawY(self.gridspace*-i)

            # X Axis Fillers
            for j in range(1, ((height+self.extra)//self.gridspace - 1)):
                self.drawX(self.gridspace*j)
                self.drawX(self.gridspace*-j)

        if self.animate:
            if self.counter <= self.division:
                self.counter += self.speed

            else:
                self.counter = self.division
                self.animation_done = True

        else:
            self.counter = self.division
            self.animation_done = True


        if self.keepcontained:
            pop_matrix()


