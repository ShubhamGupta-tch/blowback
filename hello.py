from p5 import *
from base.cartesian import Grid
from base.text import Text
import time
import math

WIDTH = 1000
HEIGHT = 650

axis = Grid(WIDTH/2, HEIGHT/2, main=True)
r = 0

shear_done = False
rotate_done = False

def setup():
    size(WIDTH, HEIGHT)
    lora = create_font("fonts/static/Lora-Regular.ttf", 30)
    text_font(lora)


def draw():
    global r, shear_done, rotate_done;
    axis.create()

    if axis.animation_done:
        rect(0, 0, 100, 100)

        if not shear_done:
            axis.shear = (radians(r), 0)
            if r == 45:
                shear_done = True
                r = 0

        else:
            if not rotate_done:
                axis.rotate = radians(r)

                if r == 45:
                    rotate_done = True


        if not rotate_done or not shear_done:
            r += 1



    # save_frame(filename="photos/screen.png")


try:
    run(frame_rate=1000)

except:
    pass
