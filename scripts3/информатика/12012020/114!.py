n = int(input())
a = []
c = 12001
b = 12001
for i in range (n):
    a.append(int(input()))
for i in range (n):
    for j in range (i,n):
        if (a[i]+a[j])%144==0 and a[i]<a[j]:
            if c+b>=a[i]+a[j]:
                c = a[i]
                b = a[j]
if c == 12001:
    print(0)
else:
    print(c, b)
