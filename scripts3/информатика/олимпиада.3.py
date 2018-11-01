m=int(input('введите количество участников '))
i=0
j=0
h=0
r=0
d=0
e=0
if m<=2*1000000000:
    while m%2==0:
        m=m/2
        i=i+1
    print (i)
    while m%3==0:
        m=m/3
        j=j+1
    print (j)
    while m%5==0:
        m=m/5
        h=h+1
    print (h)
    while m%7==0:
        m=m/7
        r=r+1
    print (r)
    if i%2==0:
        d=i*i
    else:
        e=e+i*i
    print (e)
    print (d)
    if j%2==0:
        d=d+j*j*j
    else:
        e=e+j*j*j
    print (e)
    print (d)
    if h%2==0:
        d=d+h*h*h*h*h
    else:
        e=e+h*h*h*h*h
    print (e)
    print (d)
    if r%2==0:
        d=d+r*r*r*r*r*r*r*r
    else:
        e=e+r*r*r*r*r*r*r*r
    print (e)
    print (d)
    s=m/e
    print (s)
else:
    print ('введите правильные числа')

