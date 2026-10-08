nums=[100,4,200,1,3,2]
nums.sort()
long=0
c=0
for i in range(len(nums)-1):
    if nums[i]+1==nums[i+1]:
        c+=1
        if c>long:
            long=c
    elif nums[i]==nums[i+1]:
        continue
    else:
        c=0
if nums:
    print(long+1)
else:
    print(0)


nums = [2,2,1]
for i in nums:
    if nums.count(i)==1:
        print(i)