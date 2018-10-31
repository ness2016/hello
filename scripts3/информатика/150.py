n=int(input ('введите число '))
find=False
if n<=1028:
    for x in range (0,11):
        i=x**3
        m=(n-i)**(1/3)
        if m.is_integer():
            print (int(m),x)
            find=True
            break
    if not find :    
        print ('impossible')
else:
    print ('введите правильные числа')
