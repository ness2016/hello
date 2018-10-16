# -*- coding: Windows-1251 -*-
import math
# теория https://glebgrenkin.blogspot.com/2014/03/blog-post.html
#ускорение свободного падения
g=9.8
#масса снаряда
m=9.6
#начальная скорость
v=800
#коэффициент сопротивления
k=0.0008137
# Шаг вычисления
dt=0.00025
#переменные
x=0 #x
y=0 #y

a=float(input ())

vx=v*math.cos(math.radians( a )) #горизонтальная скорость
vy=v*math.sin(math.radians( a )) #вертикальная скорость

if a<5:
    a=5
elif a>85:
    a=85
  
while 1==1:
    vxx=vx
    vyy=vy
    vx = vx-k*vx*math.sqrt(vx*vx+vy*vy)*dt/m
    vy = vy-(g+k*vy*math.sqrt(vx*vx+vy*vy)/m)*dt
    x  = x+(vx+vxx)*dt/2
    y  = y+(vy+vyy)*dt/2
    if y<=0:
        print(int(round(x)))
        break
            
