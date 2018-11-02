n=int(input('введите число '))
j=False
if n<=100000:
        if n==3:
                print ('--+')
                j=True
        if n%4==0:
                i=n/4
                print ('-++-'*int(i))
                j=True
        elif n%2==1:
                for m in range (1,100000):
                        if n==7+4*(m-1):
                                c=(n-7)/4
                                print ('++--++'+'--++'*int(c)+'+')
                                j=True
                                break
                        #else:
                        #        print ('impossible')
        if not j:
                print ('impossible')           
else:
    print ('введите правильные числа')
