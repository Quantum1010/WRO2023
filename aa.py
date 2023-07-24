#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Color

# Create your objects here.
ev3 = EV3Brick()

# ここからプログラムを書き込む
ev3.speaker.beep()

color_sensor = ColorSensor(Port.S4)

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