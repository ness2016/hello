a=int(input())
b=int(input())
c=int(input())
if (c<a<b) or (b<a<c):
    print (a)
elif (a<c<b) or (b<c<a):
    print (c)
else:
    print (b)
