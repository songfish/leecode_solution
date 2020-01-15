# class Solution:
#     def removeElement(self, nums, val):
#         length = len(nums)
#         for i in range(length-1, -1, -1):
#             if nums[i] == val:
#                 nums.pop(i)
#         print(nums)
#         return len(nums)

class Solution:
    def removeElement(self, nums, val):
        # length = len(nums)
        # for i in range(length-1, -1, -1):
        #     if nums[i] == val:
        #         nums.pop(i)
        # return len(nums)
        left_pointer = 0
        right_pointer = 0
        while right_pointer < len(nums):
            if nums[right_pointer] == val:
                right_pointer += 1
            else:
                nums[left_pointer] = nums[right_pointer]
                left_pointer += 1
                right_pointer += 1
        return left_pointer

S = Solution()
print(S.removeElement(nums=[3,2,2,3],val=3))

'''
2019.12.24反思:
    第一种方法 沿用26题的思路，倒序比较[自己写出来的]
    第二种方法 参考别人的code，双指针
'''
