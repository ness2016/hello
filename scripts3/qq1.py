a=input()
#print (len(a))
#N=str.find
#n=(a.find('N'))
#m=(a.find('S'))
#print(n)
#print(m)
#c=a[n-1:n]
x=0
y=0
q=0
for i in a:
    #print(i)
    if i == 'S':
        #print(i)
        #print(q)
        #print(a[q:a.find()])
        print(a.find(i,q))
        #print(q)
        q=q+a.find(i)
    #elif i=='N':
    #elif i=='E':
    #elif i=='W':    
