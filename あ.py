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
a = 0
b = 12

robot.drive_time(200,0,500)
robot.drive_time(0,180,500)

while a < 2:
    if color.reflection() < b:
        a = a + 1
    print(color.reflection())
    robot.drive(200,0)
    if a : 2
    break

arm.run(-100)
wait(2000)

robot.drive_time(0,-180,500)
robot.drive_time(200,0,5000)

arm.run(100)
wait(2000)
arm.stop()

robot.drive_time(0,360,500)
robot.drive_time(200,0,5000)
robot.drive_time(0,180,500)
robot.drive_time(200,0,5000)

arm.run(-100)
arm.stop()
