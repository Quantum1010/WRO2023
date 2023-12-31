#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
color_sensor=ColorSensor(Port.S2)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
arm = Motor(Port.A)

#詳細
wheel_diameter = 56
axle_track = 120
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

# Write your program here.
robot.drive_time(0,90,1000)
robot.drive_time(0,-90,1000)
robot.drive_time(0,180,1000)
robot.drive_time(0,-90,1000)

while True:
    robot.drive(200,0)
    print(color_sensor.color())
    if color_sensor.color == Color.BLACK:
        ev3.speaker.beep()
