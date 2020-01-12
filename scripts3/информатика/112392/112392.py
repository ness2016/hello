from math import*
sun=open('input.txt','r')
moon=open('output.txt','w')
a=list(map(int,sun.read().split()))
n=[]

for i in a:
    if (i>0) and (i%2==0):
        n.append(i)
print(n)        
if len(n)>0:
    c=str(min(n)) + " " + str(max(n))
    moon.write(c)
else:
    moon.write(str(0))
sun.close()
moon.close()
