def f(k):
    return k**2
x1=int(input ('введите x1 = '))
x2=int(input ('введите x2 = '))
i=x1-1
if (x1<x2) and (x2-x1<=10): 
    while i<x2:
        i=i+1
        print ('абсцисса = ' + str(i) + ' ордината = ' + str(f(i)))
else:
    print ('введите правильные числа')
   
