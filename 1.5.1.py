nums = [1, 5, 2, 7, 1, 9, 3, 8, 5, 9]
a=0
i = 0
while i < len(nums):
    a=a+nums[i]
    i = i + 1
b=a/len(nums)
#print(b)
c = 0
i = 0
while i < len(nums):
    c=c+(nums[i]-b)**2
    i = i + 1
b=c/len(nums)-1
d=b**(1/2)
print ("d=" + d)
