a=input()
q=0
q1=0
x=0
y=0
for i in a:
    if i=='S':
        y=y+int(a[q1:a.find(i,q)])
        q1=a.find(i,q)+1
    elif i=='N':
        y=y-int(a[q1:a.find(i,q)])
        q1=a.find(i,q)+1        
    elif i=='E':
        x=x+int(a[q1:a.find(i,q)])
        q1=a.find(i,q)+1
    elif i=='W':
        x=x-int(a[q1:a.find(i,q)])
        q1=a.find(i,q)+1           
    q=q+1
print('x:'+str(x)+' y:'+str(y))
