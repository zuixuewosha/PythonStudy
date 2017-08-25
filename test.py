#!/bin/usr/
#-*-coding : UTF-8-*-
def pay(x,n)
    s=1
    while x < 1:
        n = n -1
        s = s * x
    return s

zui=pay(5,2)
print(zui)