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
color_sensor = ColorSensor(Port.S2)
ultra = UltrasonicSensor(Port.S1)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
arm = Motor(Port.A)

#詳細
wheel_diameter = 56
axle_track = 120
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

#箱の色確認
arm.on_for_degrees(50,90)
if color_sensor.color == 3:
    iro = 3
else:
    iro = 2

#超音波センサーを使ったやつ
while ultra.distance_centimeters < 100:
    if color_sensor.reflected_light_intensity <= 50:
        robot.drive(50,30)
    else:robot.drive(50,-30)

#ライントレースのプログラム
while True:
    if color_sensor.reflected_light_intensity <= 4:
        robot.drive(50,30)
    else:robot.drive(50,-30)

#RGB変換
# RGB値を取得して変換
rgb_val = color_sensor.rgb()
red, green, blue = rgb_val[0], rgb_val[1], rgb_val[2]
# 判別条件を設定する
BLACK_THRESHOLD = 15
BLUE_THRESHOLD = 30
GREEN_THRESHOLD = 30
WHITE_THRESHOLD = 30

# RGB値を使って色を判別する関数
def detect_color(red, green, blue):
    if red < BLACK_THRESHOLD and green < BLACK_THRESHOLD and blue < BLACK_THRESHOLD:
        return "黒"
    elif blue > BLUE_THRESHOLD and green < GREEN_THRESHOLD and red < GREEN_THRESHOLD:
        return "青"
    elif green > GREEN_THRESHOLD and red < BLUE_THRESHOLD and blue < BLUE_THRESHOLD:
        return "緑"
    elif red > WHITE_THRESHOLD and green > WHITE_THRESHOLD and blue > WHITE_THRESHOLD:
        return "白"
    else:
        return "不明"

# 色を判別して表示
color = detect_color(red, green, blue)
print(rgb_val[0], rgb_val[1], rgb_val[2])
print("検出色",color)