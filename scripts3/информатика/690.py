# -*- coding: Windows-1251 -*-
import math
# ������ https://glebgrenkin.blogspot.com/2014/03/blog-post.html
#��������� ���������� �������
g=9.8
#����� �������
m=9.6
#��������� ��������
v=800
#����������� �������������
k=0.0008137
# ��� ����������
dt=0.00025
#����������
x=0 #x
y=0 #y

a=float(input ())

vx=v*math.cos(math.radians( a )) #�������������� ��������
vy=v*math.sin(math.radians( a )) #������������ ��������

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
            
