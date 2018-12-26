fin=open('input.txt','r')
fid=open('output.txt','w')

l = [line.strip() for line in fin]

a=int(l.pop(0))
c=0

for i in l:
        b=list(i.split())
        if int(b[1])<a:
                c+=1
                print(i, file=fid)
print(c, file=fid)                
 

fin.close()
fid.close()
