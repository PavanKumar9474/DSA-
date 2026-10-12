# Plusone
def plusOne(digits):
    for i in range(len(digits)-1,-1,-1):
        if digits[i]<9:
            digits[i]+=1
            return digits
        digits[i]=0
    return [1]+digits
print(plusOne([1,2,3]))

# SingleNumber
def singleNumber(nums):
    for i in nums:
        if nums.count(i)==1:
            return i
nums=[2,2,1]
print(singleNumber(nums))

# getConcatenation
nums=[1,2,1]
new=[]
for i in nums:
    new.append(i)
for i in nums:
    new.append(i)
print(new)


# Merge sorted Array
nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3
nums1=nums1[:m]+nums2
nums1.sort()
print(nums1)
