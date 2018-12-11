S=input()
S1=S[:S.find('.')].upper()
L={}
#print(S1)
for i in S1:
    if i!=' ':
        if i in L:
            L[i]+=1
        else:
            L[i]=1
m=0
for i in L:
    if L[i]>m:
        m=L[i]
N={}
for i in L:
    if L[i]==m:
        N[i]=L[i]
 
P = N.keys() # получаем ключи
P = list(P) # превращаем его в обычный список
P.sort() # сортируем список
print(P[0],N[P[0]])
