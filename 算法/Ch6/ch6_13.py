import random
nums = random.sample(range(1,100),10)
nums2 = nums[:]#copy

print(nums)
nsum = 0

for i in range(3):
    maxNum = 0
    for j in range(len(nums)):
        if nums[j] > maxNum:
            maxNum = nums[j]
    print(maxNum)        
    nsum +=  maxNum
    nums.remove(maxNum)
print("MaxSum:",nsum)    
    
newList = sorted(nums2)
print(newList)
testSum =newList[-1] + newList[-2]+ newList[-3]
print("MaxSum2:",testSum)    
