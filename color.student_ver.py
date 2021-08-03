from pyatcrobo2.parts import DCMotor, IRPhotoReflector, ColorSensor
from pystubit.board import *
import time

left_wheel = DCMotor('M1')
right_wheel = DCMotor('M2')
ir = IRPhotoReflector('P0')
cs = ColorSensor('I2C')

left_wheel.brake()
right_wheel.brake()


speed =
slow_speed =
high_speed =



left_wheel.power(speed)
right_wheel.power(speed)
threshold = 800

#finding threshold
display.show("A") #white
while not button_a.is_pressed():
    pass
display.clear()
white = ir.get_value()

display.show("B") #black
while not button_b.is_pressed():
    pass
display.clear()
black = ir.get_value()
threshold = (white+black)/2


def move_forward():
    left_wheel.ccw()
    right_wheel.ccw()

def move_backward():
    left_wheel.cw()
    right_wheel.cw()

def turn_left():
    right_wheel.ccw()

def turn_right():
    left_wheel.ccw()

def spin_left():
    left_wheel.cw()
    right_wheel.ccw()

def spin_right():
    left_wheel.ccw()
    right_wheel.cw()

def stop():
    left_wheel.brake()
    right_wheel.brake()

def tracing():
    if ir.get_value() < threshold:
        left_wheel.ccw()
        right_wheel.brake()
    else:
        left_wheel.brake()
        right_wheel.ccw()

def colorget():

    if color == cs.COLOR_BLUE:
        left_wheel.power(slow_speed)
        right_wheel.power(slow_speed)
    elif color == cs.COLOR_GREEN:
        left_wheel.power(high_speed)
        right_wheel.power(high_speed)

while True:
    tracing()
    color = cs.get_colorcode()
    if color == cs.COLOR_BLUE:
        left_wheel.power(slow_speed)
        right_wheel.power(slow_speed)
    elif color == cs.COLOR_GREEN:
        left_wheel.power(high_speed)
        right_wheel.power(high_speed)
