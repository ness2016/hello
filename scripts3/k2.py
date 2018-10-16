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
k=0.3251
# Шаг вычисления
dt=0.001
#переменные
x=0 #x
y=0 #y

a=float(input (" Угол стрельбы 5-85:"))

vx=v*math.cos(math.radians( a )) #горизонтальная скорость
vy=v*math.sin(math.radians( a )) #вертикальная скорость

if a<5 or a>85:
    print(" Угол стрельбы должен быть 5-85")
else:
    
    while 1==1:
        vx = vx-k/m*vx*dt
        vy = vy-(g+k/m*vy)*dt
        x  = x+vx*dt
        y  = y+vy*dt
        if y<=0:
            print(int(round(x)))
            break
            
