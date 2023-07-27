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

robot.drive_time(200,0,1000)
robot.drive_time(0,97,1000)

while a < 2:
    print(a)
    robot.drive(200,0)
    if color.color() == Color.BLACK:
        ev3.speaker.beep()
        a = a + 1
        while not color.color() == Color.BLACK:
            pass
    if a == 2:
        break
robot.stop()
arm.run(-100)
wait(2000)

robot.drive_time(0,-90,1000)
robot.drive_time(200,0,3000)

arm.run(100)
wait(2000)
arm.stop()

robot.drive_time(0,183,1000)
robot.drive_time(200,0,1000)
robot.drive_time(0,90,1000)
robot.drive_time(200,0,5000)

arm.run(-100)
wait(2000)

robot.drive_time(-200,0,1000)
