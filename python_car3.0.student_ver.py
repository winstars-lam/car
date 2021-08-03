from pyatcrobo2.parts import DCMotor, IRPhotoReflector
from pystubit.board import *
import time

left_wheel = DCMotor('M1')
right_wheel = DCMotor('M2')
ir = IRPhotoReflector('P0')


left_wheel.brake()
right_wheel.brake()

speed =

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

def tracing():
    if ir.get_value() < threshold:
        left_wheel.ccw()
        right_wheel.brake()
    else:
        left_wheel.brake()
        right_wheel.ccw()

#main program


while True:



