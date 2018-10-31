n=int(input ())
find=False
if n<=1028:
    for x in range (0,12):
        i=x**3
        if n-i < 0:
            break
        m=(n-i)**(1/3)
        print(i,m,x)
        #if not isinstance(m, complex):
        if m.is_integer():
            if int(m)**3 + x**3 == n :
                print (int(m),x)
                find=True
                break
    if not find :    
        print ('impossible')
