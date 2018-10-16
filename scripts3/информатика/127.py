A,i = raw_input().split()
A=int(A)
i=int(i)
z=(A>>i)<<i
print(A-z)
