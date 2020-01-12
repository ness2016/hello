#from math import*
fin=open('input.txt','r')
fid=open('output.txt','w')
a=list (map(int,fin.read().split()))
k={}
t=0


for i in range (len(a)):
    print(a[i])
    if a[i]==a[i-1]:
        t+=1
        if t>k.get(a[i],0):
            k[a[i]]=t
    else:
        t=0
    
    print('---')
print(a)
print(k)

r=str(min(k))+" "+str(max(k))
print ((max(k)), file=fid)
fin.close()
fid.close()
