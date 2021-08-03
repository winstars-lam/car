# Write your code here :-)
from pyatcrobo2.parts import DCMotor
from pystubit.board import *
import time

left_wheel = DCMotor('M1')
right_wheel = DCMotor('M2')

speed =
left_wheel.power(speed)
right_wheel.power(speed)

def move_forward():
    left_wheel.ccw()
    right_wheel.ccw()

while True:

