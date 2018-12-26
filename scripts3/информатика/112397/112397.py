from math import *
fin=open('input.txt','r')
fid=open('output.txt','w')
a=list (map(int,fin.read().split()))
n=[]
g={}
u=0
for i in range (len(a)):
    b=a[i]
    while b>10:
        u+=b%10
        b=floor(b/10)
    u+=b
    #print(u)
    
    g[a[i]]=u
    u=0

P = g.values()
P = list(P)
P.sort(reverse=True)
for i in range(len(P)):
    for j in g.keys():
        if g[j]==P[i]:
            print (j, file=fid)
            break
    g.pop(j)    
#print (P)
#print (g)
fin.close()
fid.close()
