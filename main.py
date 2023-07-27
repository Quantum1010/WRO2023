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
color = ColorSensor(Port.S2)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
arm = Motor(Port.A)

#詳細
wheel_diameter = 56
axle_track = 120
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

#drive_timeの後の括弧はスピード(mm/s),ハンドルの角度？(deg/s),速度(ミリ秒つまり秒数×1000)

#初期設定的なやつ
robot.drive_time(200,0,500)
while color.reflection() >= 12:
    robot.drive(200,0)
if color.reflection() < 12:
    robot.drive_time(0,90,500)

#白ブロック前の角まで
for i in range(5):
    ev3.screen.print(color.reflection())
    if color.reflection() < 12:
        robot.drive_time(0,-10,300)
        while color.reflection() >= 12:
            robot.drive(200,0)
    else:
        robot.drive_time(0,10,300)
        while color.reflection() < 12:
            robot.drive(200,0)

#白ブロック手前まで
for i in range(3):
    ev3.screen.print(color.reflection())
    if color.reflection() < 13:
        robot.drive_time(200,10,500)
        while color.reflection() >= 13:
            robot.drive(200,0)
    else:
        robot.drive_time(200,-10,500)
        while color.reflection() < 13:
            robot.drive(200,0)

robot.drive_time(0,180,500)
arm.run_angle()

for i in range(2):
    ev3.screen.print(color.reflection())
    if color.reflection() < 13:
        robot.drive_time(200,10,500)
        while color.reflection() >= 13:
            robot.drive(200,0)
    else:
        robot.drive_time(200,-10,500)
        while color.reflection() < 13:
            robot.drive(200,0)

robot.drive_time(0,90,500)

for i in range(5):
    ev3.screen.print(color.reflection())
    if color.reflection() < 13:
        robot.drive_time(200,10,500)
        while color.reflection() >= 13:
            robot.drive(200,0)
    else:
        robot.drive_time(200,-10,500)
        while color.reflection() < 13:
            robot.drive(200,0)
            