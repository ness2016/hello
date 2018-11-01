a=int(input())
b=int(input())
c=int(input())
if a+b+c<=30000:
    if (c<a<b) or (b<a<c):
        print (a)
    elif (a<c<b) or (b<c<a):
        print (c)
    else:
        print (b)
else:
    print ('введите правильные числа')
