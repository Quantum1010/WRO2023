#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import uselect

# Create your objects here.
ev3 = EV3Brick()

# ここからプログラムを書き込む
ev3.speaker.beep()

color_sensor = ColorSensor(Port.S4)

# RGB値を取得して変換
rgb_val = color_sensor.rgb()
red, green, blue = rgb_val[0], rgb_val[1], rgb_val[2]

# 色を判定
if 200<= red and 140>= green and 100>= blue
    return "赤"
elif 55>=red and 55>=green and 55>=blue
    return "黒"
elif 
    return "青"
elif 
    return "緑"
elif 
    return "白"
else:
    return "その他の色"


lab_values = rgb_to_lab(red, green, blue)
color_name = detect_color_name(lab_values)

print("RGB values:", red, green, blue)
print("Lab values:", lab_values)
print("Detected color:", color_name)
