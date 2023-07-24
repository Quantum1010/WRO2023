#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Color
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.tools import wait
import uselect

# Create your objects here.
ev3 = EV3Brick()

# ここからプログラムを書き込む
ev3.speaker.beep()

# RGB値を取得する関数
def rgb_to_lab(r, g, b):
    # RGB値を範囲0-1に変換
    r /= 255.0
    g /= 255.0
    b /= 255.0

    # sRGBからLinear RGBへの変換
    def srgb_to_linear(color):
        if color <= 0.04045:
            return color / 12.92
        return ((color + 0.055) / 1.055) ** 2.4

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
            return t ** (1.0 / 3.0)
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
    # ... (以前に定義したdetect_color_name関数をここに記述)

# RGB値を取得して変換
rgb_val = ev3.color_sensor.get_rgb()
red, green, blue = rgb_val[0], rgb_val[1], rgb_val[2]
lab_values = rgb_to_lab(red, green, blue)

# Lab値を利用して色を判定
color_name = detect_color_name(lab_values)
print("RGB values:", red, green, blue)
print("Lab values:", lab_values)
print("Detected color:", color_name)
