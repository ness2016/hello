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
k=0.3251
# ��� ����������
dt=0.001
#����������
x=0 #x
y=0 #y

a=float(input (" ���� �������� 5-85:"))

vx=v*math.cos(math.radians( a )) #�������������� ��������
vy=v*math.sin(math.radians( a )) #������������ ��������

if a<5 or a>85:
    print(" ���� �������� ������ ���� 5-85")
else:
    
    while 1==1:
        vx = vx-k/m*vx*dt
        vy = vy-(g+k/m*vy)*dt
        x  = x+vx*dt
        y  = y+vy*dt
        if y<=0:
            print("������� ���������: "+str(int(round(x)))+" ������")
            break
            
