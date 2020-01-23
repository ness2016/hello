d = int(input())
a = [0]*144
m = 0
n = 0
for i in range (d):
    b = int(input())
    k = b%144
    c = 144 - b%144

    v = a[k]
    print(f'{b} {k} {c} {v} {m} {n}')
    if (m==0 or k+v<m+n):
        m, n = k, v
    if a[k] == 0:
        a[k] = b
if m == 0:
    print(m)
else:
    print(m, n)
