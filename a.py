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
colorsensor = ColorSensor(Port.S4)
color = colorsensor.color

#Lab値にするよー！
def rgb_to_lab(r, g, b):
    # RGB値を範囲0-1に変換
    r /= 255.0
    g /= 255.0
    b /= 255.0

    # sRGBからLinear RGBへの変換
    def srgb_to_linear(color):
        if color <= 0.04045:
            return color / 12.92
        return ((color + 0.055) / 1.055) ;2.4

    r_linear = srgb_to_linear(r)
    g_linear = srgb_to_linear(g)
    b_linear = srgb_to_linear(b)

    # XYZ色空間への変換
    x = r_linear * 0.4124564 + g_linear * 0.3575761 + b_linear * 0.1804375
    y = r_linear * 0.2126729 + g_linear * 0.7151522 + b_linear * 0.0721750
    z = r_linear * 0.0193339 + g_linear * 0.1191920 + b_linear * 0.9503041

    # XYZをLabに変換
    x /= 0.950456
    y /= 1.000000
    z /= 1.088754

    def xyz_to_lab(t):
        if t > 0.008856:
            return t * (1.0 / 3.0)
        else:
            return (903.3 * t + 16.0) / 116.0

    fx = xyz_to_lab(x)
    fy = xyz_to_lab(y)
    fz = xyz_to_lab(z)

    l = max(0, 116.0 * fy - 16.0)
    a = 500.0 * (fx - fy)
    b = 200.0 * (fy - fz)

    return l, a, b

# 色名を返す関数
def detect_color_name(lab_values):
    l, a, b = lab_values

    # 赤色のLab値の範囲を定義
    red_min_l = 60
    red_max_l = 100
    red_min_a = 0
    red_max_a = 80
    red_min_b = -60
    red_max_b = 20

    # 黒色のLab値の範囲を定義
    black_max_l = 50
    black_max_a = 20
    black_max_b = 20

    # 青色のLab値の範囲を定義
    blue_min_l = 20
    blue_max_l = 80
    blue_max_a = 10
    blue_max_b = 10

    # 緑色のLab値の範囲を定義
    green_min_l = 40
    green_max_l = 90
    green_max_a = 30
    green_max_b = 30

    # 白色のLab値の範囲を定義
    white_min_l = 80
    white_max_a = 10
    white_max_b = 10

    # 色を判定
    if red_min_l <= l <= red_max_l and red_min_a <= a <= red_max_a and red_min_b <= b <= red_max_b:
        return "赤"
    elif l <= black_max_l and abs(a) <= black_max_a and abs(b) <= black_max_b:
        return "黒"
    elif blue_min_l <= l <= blue_max_l and a <= -blue_max_a and b >= blue_max_b:
        return "青"
    elif green_min_l <= l <= green_max_l and -green_max_a <= a <= green_max_a and -green_max_b <= b <= green_max_b:
        return "緑"
    elif l >= white_min_l and abs(a) <= white_max_a and abs(b) <= white_max_b:
        return "白"
    else:
        return "その他の色"

# RGB値を取得
red = 0
green = 255
blue = 0

# RGB値をLab値に変換
lab_values = rgb_to_lab(red, green, blue)

# 色を検出して表示
color_name = detect_color_name(lab_values)
print("検出された色:", color_name)