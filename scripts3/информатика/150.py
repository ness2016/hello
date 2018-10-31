n=int(input ('введите число '))
m=0
f=0
i=x**3
if n<=1028:
    for x in range (0,10):
        m=(n-i)**(1/3)
        f=round(m)
        if m=f:
            print (m,i)
        else:
            print ('inpossible')
else:
    print ('введите правильные числа')
    
