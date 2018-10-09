#import numpy as np
#https://glebgrenkin.blogspot.com/2014/03/blog-post.html
#ускорение свободного падения
g=9.8
#масса снаряда
m=9.6
#начальная скорость
v=800

x=int(input (" Угол стрельбы 5-85:"))
if x<5 or x>85:
    print(" Угол стрельбы должен быть 5-85")
else:
    print(" Boom!!")
