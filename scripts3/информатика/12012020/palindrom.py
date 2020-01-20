n = int(input())
t = 0
k = 0
c=[]
d=[]
for i in range (n):
    c.append(int(input()))
    
for i in c:
    d.append(hex(i).lstrip('0x'))

for i in d:
    t = len(i)
    for j in range (t//2):
        if i[j]!=i[-1-j]:
            k += 1
            break
l=len(d) # исходное количество строк
m=l-k    # из них палиндромы	
print(f'{m} чисел из {l} являются палиндромами')


