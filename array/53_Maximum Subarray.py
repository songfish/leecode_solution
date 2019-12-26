class Solution:
    def maxSubArray(self, nums):
        ans = nums[0]
        sum = 0
        for num in nums:
            if sum < 0:
                sum = num
            else:
                sum += num
            ans = max(sum, ans)
        return ans


S = Solution()
print(S.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

'''
2019.12.26反思：
    是很巧妙的结题思路了，正向增益。
'''
