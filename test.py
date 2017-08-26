#!/bin/usr/
#-*-coding : UTF-8-*-
# 计算乘方
def pay(x,n):
    s=1
    while n > 0:
        n = n -1
        s = s * x
    return s

zui=pay(5,2)
print zui

# 计算面积函数
def area(width, height):
    return width * height
 
def print_welcome(name):
    print("Welcome", name)

print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))