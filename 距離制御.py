#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import uselect


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

#ここからプログラムを書き込む
ev3.speaker.beep()

#インスタンスの作成
color = ColorSensor(Port.S1)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
arm = Motor(Port.A)

#詳細
wheel_diameter = 56
axle_track = 150
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

#drive_timeの後の括弧はスピード(mm/s),ハンドルの角度？(deg/s),速度(ミリ秒つまり秒数×1000)

robot.drive_time(100,0,2000)
robot.drive_time(0,90,1000)
robot.drive_time(106,0,10000)
robot.drive_time(0,-90,1000)
robot.drive_time(100,0,4600)
arm.on_for_degrees(50,90)
arm.on_for_degrees(50,-90)
robot.drive_time(0,180,1000)
robot.drive_time(100,0,4600)
robot.drive_time(0,90,1000)
robot.drive_time(106,0,10000)
robot.drive_time(0,90,1000)
robot.drive_time(100,0,500)
arm.on_for_degrees(50,90)
arm.on_for_degrees(50,-90)