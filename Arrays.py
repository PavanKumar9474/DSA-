# Plusone
def plusOne(digits):
    for i in range(len(digits)-1,-1,-1):
        if digits[i]<9:
            digits[i]+=1
            return digits
        digits[i]=0
    return [1]+digits
print(plusOne([1,2,3]))

#Find the Index of the First Occurrence in a String
haystack="sadbutsad"
needle="sad"
ans=-1
for i in range(len(haystack)-len(needle)+1):
    if haystack[i:i+len(needle)]==needle:
        ans=i
        break
print(ans)

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

# Remove Element
nums=[3,2,2,3]
val=3
new=[]
for i in nums:
    if i!=val:
        new.append(i)
print(len(new))
print(new)

# Search insert Position
nums=[1,3,5,6]
target=5
for i in range(len(nums)):
    if nums[i]>=target:
        print(i)
        break
else:
    print(len(nums))

# Count Number of pairs of "()"
s=input()
stack=[-1]
ans=0
for i,ch in enumerate(s):
    if ch=='(':
        stack.append(i)
    else:
        stack.pop()
        if not stack:
            stack.append(i)
        else:
            ans=max(ans,i-stack[-1])
print(ans)

# For every open "({[" There is an close ")}]"
def isValid(self, s):
    d={")":"(","}":"{","]":"["}
    st=[]
    for i in s:
        if i in "({[":
            st.append(i)
        else:
            if not st or st.pop()!=d[i]:
                return False
                break
    return len(st)==0

# Missing Number
def missingNumber(nums):
    for i in range(len(nums)):
        if i not in nums:
            return i
    else:
        return len(nums)
