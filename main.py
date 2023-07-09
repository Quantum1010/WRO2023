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

#ここからプログラムを書き込む
ev3.speaker.beep()

#インスタンスの作成
touch = TouchSensor(Port.D)
color = ColorSensor(Port.A)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

#詳細
wheel_diameter = 56
axle_track = 123

#ここから動作
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

#drive_timeの後の括弧はスピード(mm/s),ハンドルの角度？(deg/s),速度(ミリ秒つまり秒数×1000)
#robot.drive_time(200, 0, 2000)#

#ライントレースのプログラム
while True:
    if color.reflected_light_intensity < 15:
        robot.drive_time(200, 0, 2000)
    else:robot.drive_time(0, 0, 0)