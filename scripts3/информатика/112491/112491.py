fin=open('input.txt','r')
error = False
a=list (map(str,fin.read().split()))
res=[]
for i in range (len(a)):
    sign = a[i][:1]
    val = a[i][1:]
    if sign == '+':
        if not val.isdigit():
            error=True
            break
        res.append(val)
    elif sign == '-':
        if len(res)>0:
            res.pop()
        #else:
            #error=True
            #break
    else:
        error=True
        break
    #print(sign)
    #print(val)
if not error:            
    if len(res)==0:
        print('EMPTY')
    else:
        print(' '.join(res))
else:
    print('ERROR')
fin.close()

