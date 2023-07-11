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
touch = TouchSensor(Port.D)
color = ColorSensor(Port.S2)
Ultra = UltrasonicSensor(Port.S1)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
arm = Motor(Port.A)

#詳細
wheel_diameter = 56
axle_track = 120

#ここから動作
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

#drive_timeの後の括弧はスピード(mm/s),ハンドルの角度？(deg/s),速度(ミリ秒つまり秒数×1000)
#robot.drive_time(200,0,2000)
#robot.drive_time(0,90,1000)

#ライントレースのプログラム
while Ultra.distance_centimeters < 20 :
    if color.reflected_light_intensity <= 50 :
        robot.drive(50,30)
    else:robot.drive(50,-30)

#左においてある箱の色を確認する
robot.drive_time(0,-90,1000)
robot.drive_time(100,0,1000)
arm.on_for_degrees(50,90)
if color.color == 3:
    iro = 3
else:
    iro = 2

#白ブロックに向かおう！
robot.drive_time(0,180,1000)
while
if color.reflected_light_intensity <= 50 :
    robot.drive(50,30)
else:robot.drive(50,-30)
wait(200000)

break