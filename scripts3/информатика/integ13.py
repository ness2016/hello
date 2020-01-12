from math import*
      
n = 99999
      
def f(k):
    return 2*cos(k/2)
def F(k):
    return k**2
x = -99
y1 = f(x)
y2 = F(x)
while y1 < y2:
    x+= 0.0001
    y1 = f(x)
    y2 = F(x)
      
a = x
      
while y2 < y1:
    x+= 0.0001
    y1 = f(x)
    y2 = F(x)
      
b = x
dx = (b - a) / n
S1=0
x = a
for i in range(1,n-1):
    S1 += dx*(f(x)+f(x+dx))/2
    x+=dx
print(S1)
S2=0
x = a
for i in range(2,n-1):
    S2 += dx*(F(x)+F(x))/2
    x+=dx
print(S2)
print(S1-S2)