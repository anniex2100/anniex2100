## 5번

ss = 'Python'

for i in range(0,len(ss)):
    print(ss[i] + '$',end = '')
print('\n')


## 11번

a = input("문자열:")

for i in range(0,len(a)):
    if a[i].isalpha() == True:
        print(a[i], end = '')
print('\n')


## 9번

inStr, outStr = "Python", ""
strLen = len(inStr)

for i in range(0, strLen):
    outStr += inStr[-i-1]

print("내용을 거꾸로 출력 --> %s" %outStr)


## 13번

import turtle
import random
from tkinter.simpledialog import *
import math

## 전역 변수 선언 부분 ##

inStr = ''
swidth, sheight = 500, 500
tX, tY, txtSize = 0, 0, 20

angle, radian = 0, 0
spiral_factor = 7
radius_decrement = 5

## 메인 코드 부분 ##

turtle.title('거북이 글자쓰기')
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()

inStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')

total_chars = len(inStr)
angle_increment = 720 / (total_chars * 1.5)

radius = total_chars * spiral_factor

for ch in inStr :

    radian = math.radians(angle)
    tX = radius * math.cos(radian)
    tY = radius * math.sin(radian)
    r = random.random(); g = random.random(); b = random.random()

    turtle.goto(tX, tY)
    turtle.pencolor((r, g, b))
    turtle.write(ch, font=('맑은 고딕', txtSize, 'bold'))

    angle += angle_increment
    radius -= radius_decrement

turtle.done()



## 3번

def plus(v1,v2,v3):
    result = 0
    result = v1 + v2 + v3
    return result

hap = plus(100,200,300)
print(hap)


## 4번

def f1():
    print(var)

def f2():
    var = 10
    print(var)

var = 100
f1()
f2()


## 11번

def addNumber(num):
    if num <= 1:
        return num
    else:
        return num + addNumber(num-1)

print(addNumber(100))


## 8번

def myFunc(p1 = 1, p2 = 2, p3 = 3):
    ret = p1 + p2 + p3
    return ret

print("매개변수 없이 호출 ==>" , myFunc())
print("매개변수가 1개로 호출 ==>" , myFunc(1))
print("매개변수가 2개로 호출 ==>" , myFunc(1,2))
print("매개변수가 3개로 호출 ==>" , myFunc(1,2,3))



