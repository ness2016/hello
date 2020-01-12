n = int(input())
a = []
v=0
d=0
for i in range (n):
    a.append(list(map(int, input().split())))
m = list(map(int, input().split()))
c=len(m)
for t in range (c-1):
    if a[m[t]-1][m[t+1]-1]!=0:
        v=v+a[m[t]-1][m[t+1]-1]
    else:
        d=d+1
if d>0:
    print(0)
else:
    print(v)
