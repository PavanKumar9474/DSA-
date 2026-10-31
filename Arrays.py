# 1. Plus One - LeetCode 66
def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits
print("1. Plus One:", plusOne([1, 2, 3]))
# Output: [1, 2, 4]


# 2. Find the Index of the First Occurrence in a String - LeetCode 28
def strStr(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1
print("2. First Occurrence:", strStr("sadbutsad", "sad"))
# Output: 0


# 3. Single Number - LeetCode 136
def singleNumber(nums):
    for i in nums:
        if nums.count(i) == 1:
            return i
print("3. Single Number:", singleNumber([2, 2, 1]))
# Output: 1


# 4. Concatenation of Array - LeetCode 1929
def getConcatenation(nums):
    new = []
    for i in nums:
        new.append(i)
    for i in nums:
        new.append(i)
    return new
print("4. Concatenation:", getConcatenation([1, 2, 1]))
# Output: [1, 2, 1, 1, 2, 1]


# 5. Merge Sorted Array - LeetCode 88
def merge(nums1, m, nums2, n):
    nums1[:] = nums1[:m] + nums2[:n]
    nums1.sort()
    return nums1
print("5. Merge Sorted Array:",
      merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
# Output: [1, 2, 2, 3, 5, 6]


# 6. Remove Element - LeetCode 27
def removeElement(nums, val):
    k = 0
    for i in nums:
        if i != val:
            nums[k] = i
            k += 1
    return k
nums = [3, 2, 2, 3]
k = removeElement(nums, 3)
print("6. Remove Element:", nums[:k])
# Output: [2, 2]


# 7. Search Insert Position - LeetCode 35
def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)

print("7. Search Insert Position:", searchInsert([1, 3, 5, 6], 5))
# Output: 2


# 8. Longest Valid Parentheses - LeetCode 32
def longestValidParentheses(s):
    stack = [-1]
    ans = 0
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                ans = max(ans, i - stack[-1])
    return ans
print("8. Longest Valid Parentheses:",
      longestValidParentheses(")()())"))
# Output: 4


# 9. Valid Parentheses - LeetCode 20
def isValid(s):
    d = {")": "(", "}": "{", "]": "["}
    stack = []
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if ch not in d or not stack or stack.pop() != d[ch]:
                return False
    return len(stack) == 0
print("9. Valid Parentheses:", isValid("()[]{}"))
# Output: True


# 10. Missing Number - LeetCode 268
def missingNumber(nums):
    for i in range(len(nums)):
        if i not in nums:
            return i
    return len(nums)
print("10. Missing Number:", missingNumber([3, 0, 1]))
# Output: 2


# 11. Majority Element - LeetCode 169
def majorityElement(nums):
    d = {}
    n = len(nums) // 2
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for i in d:
        if d[i] > n:
            return i
print("11. Majority Element:", majorityElement([3, 2, 3]))
# Output: 3


# 12. Check if All Characters Have Equal Number of Occurrences - LeetCode 1941
def areOccurrencesEqual(s):
    d = {}
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    return len(set(d.values())) == 1
print("12. Equal Occurrences:", areOccurrencesEqual("abacbc"))
# Output: True


# 13. Minimum Positive Sum Subarray - LeetCode 3364
def minimumSumSubarray(nums, l, r):
    ans = []
    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total += nums[j]
            length = j - i + 1
            if l <= length <= r and total > 0:
                ans.append(total)
    if ans:
        return min(ans)
    return -1
print("13. Minimum Positive Sum Subarray:",
      minimumSumSubarray([3, -2, 1, 4], 2, 3))
# Output:1


# FizzBuzz
n = int(input("Enter n: "))
l = []
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        l.append("FizzBuzz")
    elif i % 3 == 0:
        l.append("Fizz")
    elif i % 5 == 0:
        l.append("Buzz")
    else:
        l.append(str(i))
print(l)

#CheckAlmostEquivalent
def checkAlmostEquivalent(self,word1,word2):
    for i in "abcdefghijklmnopqrstuvwxyz":
        if abs(word1.count(i)-word2.count(i))>3:
            return False
    return True

#ReverseString
def reverseString(s):
    l = 0
    r = len(s) - 1
    while l < r:
        le = s[l]
        re = s[r]
        s[l] = re
        s[r] = le
        l += 1
        r -= 1
print(s)

# Check perfectNumber
num=28
s=1
if num<=1:
    print(False)
else:
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            s+=i
            s+=num//i
            if i==num//i:
                s-=i
    print(s==num)
