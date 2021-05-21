from p5 import *

class Text:
    def __init__(self, text, position, animate=True, scale=(1, -1), shear=(0, 0), rotate=0):
        self.text = text
        self.position = position
        self.animate = animate
        self.scale = scale
        self.shear = shear
        self.rotate = rotate


        self.draw()

    def draw(self):
        push_matrix()

        scale(self.scale[0], self.scale[1])
        shear_x(self.shear[0])
        shear_y(self.shear[1])
        rotate(self.rotate)

        text(self.text, (self.position[0], -self.position[1]))


        pop_matrix()
