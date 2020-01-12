#from math import *
fin=open('input.txt','r')
fid=open('output.txt','w')
a=list (map(int,fin.read().split()))

def sort_by_sum(inputStr):
        return sum(map(int, list(str( inputStr )))) 

a.sort(key= sort_by_sum,reverse=True )

#a.sort( key = (lambda inputStr: sum(map(int, list(str( inputStr ))))),reverse=True )

for i in range (len(a)):
    print (a[i], file=fid)    

fin.close()
fid.close()
