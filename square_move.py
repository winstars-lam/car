from pyatcrobo2.parts import DCMotor
from pystubit.board import *
import time

left_wheel = DCMotor('M1')
right_wheel = DCMotor('M2')

speed = 100
left_wheel.power(speed)
right_wheel.power(speed)

def move_forward():
    left_wheel.ccw()
    right_wheel.ccw()

def move_backward():
    left_wheel.cw()
    right_wheel.cw()

def turn_left():
    right_wheel.cw()

def turn_right():
    left_wheel.cw()

def spin_left():
    left_wheel.cw()
    right_wheel.ccw()

def spin_right():
    left_wheel.ccw()
    right_wheel.cw()

def stop():
    left_wheel.brake()
    right_wheel.brake()

def square():
    move_forward()
    time.sleep(3)
    spin_left()
    time.sleep(1.5)
    move_forward()
    time.sleep(3)
    spin_left()
    time.sleep(1.5)
    move_forward()
    time.sleep(3)
    spin_left()
    time.sleep(1.5)
    move_forward()
    time.sleep(3)
    stop()

while True:
    if button_b.is_pressed():
        square()





