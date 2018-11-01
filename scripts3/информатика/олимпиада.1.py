A=int(input ('введите номер первого дома '))
B=int(input ('введите номер второго дома '))
import math
x=A-B
if x>=0:
    s1=x//2
    print (s1)
else:
    s2=math.fabs(x)//2
    print (round(s2))
