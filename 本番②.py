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
rdeg = 97
ldeg = -92

robot.drive_time(200,0,1000)
robot.drive_time(0, rdeg, 1000)

robot.drive(200,0)
while not color.color() == Color.BLACK:
    pass
ev3.speaker.beep()
while color.color() == Color.BLACK:
    pass
ev3.speaker.beep()
wait(500)

while not color.color() == Color.BLACK:
    pass
ev3.speaker.beep()
while color.color() == Color.BLACK:
    pass
ev3.speaker.beep()
wait(500)
while not color.color() == Color.BLACK:
    pass
ev3.speaker.beep()

robot.stop()
arm.run(-100)
wait(800)

robot.drive_time(0,ldeg,1000)
robot.drive_time(200,0,2500)

arm.run(100)
wait(2000)
arm.stop()

robot.drive_time(0, 200, 1000)
robot.drive_time(200,0,1000)
robot.drive_time(0, rdeg, 1000)
robot.drive_time(200,0,4000)

arm.run(-100)
wait(2000)
arm.stop()

robot.drive_time(-200,0,1000)

#ここから先は本番無理そうだったら消す
robot.drive_time(0,ldeg,1000)
robot.drive_time(200,0,1000)
robot.drive_time(0,ldeg,1000)

robot.drive(200,0)
while not color.color() == Color.BLACK:
    pass
ev3.speaker.beep()
while color.color() == Color.BLACK:
    pass
ev3.speaker.beep()
wait(500)

while not color.color() == Color.BLACK:
    pass
ev3.speaker.beep()
while color.color() == Color.BLACK:
    pass
ev3.speaker.beep()
wait(500)

while not color.color() == Color.BLACK:
    pass
ev3.speaker.beep()
while color.color() == Color.BLACK:
    pass
ev3.speaker.beep()
wait(500)
while not color.color() == Color.BLACK:
    pass
ev3.speaker.beep()

robot.drive_time(0,-75,1000)
robot.drive_time(200,0,2500)

robot.stop()