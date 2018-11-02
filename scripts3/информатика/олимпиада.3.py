m=int(input('введите количество участников '))
i=0
j=0
h=0
r=0
d=0
e=0
k=0
p=0
m1=m
if m<=2*1000000000:
    while m%2==0:
        m=m/2
        i=i+1
    while m%3==0:
        m=m/3
        j=j+1
    while m%5==0:
        m=m/5
        h=h+1
    while m%7==0:
        m=m/7
        r=r+1
    while m%11==0:
        m=m/11
        k=k+1
    while m%13==0:
        m=m/13
        p=p+1
    if i%2==0:
        d=d+2**i
    else:
        e=e+2
    if j%2==0:
        d=d+3**j
    else:
        e=e+3
    if h%2==0:
        d=d+5**h
    else:
        e=e+5
    if r%2==0:
        d=d+7**r
    else:
        e=e+7
    if k%2==0:
        d=d+11**k
    else:
        k=k+11
    if p%2==0:
        d=d+13**p
    else:
        e=e+13
    s=round(m1/int(e))
    print ('максимальное количество людей в полку = '+str(s))
else:
    print ('введите правильные числа')

