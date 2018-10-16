nums = [1, 5, 2, 7, 1, 9, 3, 8, 5, 9]
c = 0
i = 0
while i < len(nums):
    c=c+(nums[i]-b)**2
    i = i + 1
b=c/(len(nums)-1)
print(b)
d=b**(0.5)
print ("d=" + str(d))
