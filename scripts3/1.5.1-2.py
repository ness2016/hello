nums = [1, 5, 2, 7, 1, 9, 3, 8, 5, 9]
m=sum(nums)/len(nums)
var_res = sum([(xi-m)**2 for xi in nums])/len(nums)