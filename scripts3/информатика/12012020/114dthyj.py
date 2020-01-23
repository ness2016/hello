n = int(input())
a = [0]*144
b = 0
vu = 0
c = 0
for i in range(n):
    t = int(input())
    a[t%144] = t
    vu = a[144-t%144]
    if vu != 0 and vu < t:
        if b == 0 or vu + t <= b + c:
            b = vu
            c = t
if b == 0:
    print(0)
else:
    print(b, c)
