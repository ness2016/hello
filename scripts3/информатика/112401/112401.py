fin=open('input.txt','r')
fid=open('output.txt','w')

l = [line.strip() for line in fin]

a=int(l.pop(0))
c=0
e=[]
for i in l:
        b=list(i.split())
        d=int(b.pop(2))
        if d>a:
                c+=1
                b[1]=b[1][0]+'.'
                e.append(b)
#print(c, file=fid)
e.sort( key = (lambda input_str:input_str[0] ) )
                
print(c, file=fid)
for i in range(len(e)):
        print(str(i+1)+') '+e[i][1]+' '+e[i][0], file=fid)

fin.close()
fid.close()
