m=int(input())
n=input()
a=n.split()
o=[]
if (m<=1000) and (int(max(a))<=1000) and (int(min(a))>=-1000):
    for i in range (0,m):
        o.append(min(a))
        a.pop(a.index(min(a)))
    print(' '.join(o))
else:
    print ()
