def f(k):
    return k**2
x1=int(input ('введите x1 = '))
x2=int(input ('введите x2 = '))
i=x1
if x1<x2:
    while i<x2:
        i=i+1
        print (f(i))
else:
    print ('введите правильные числа')
