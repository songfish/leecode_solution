class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # left_pointer = 0
        # right_pointer = left_pointer + 1
        length = len(nums)
        for i in range(length-1,0,-1):
            if nums[i] == nums[i-1]:
                nums.pop(i)
        return len(nums)


'''
    2019.12.23反思：
    1.想到了用双指针但不会实现。 
    2.参考了别人的code。
    3.coding的过程中出现了两个问题，第一，for循环的条件一开始写成了(length, -1, -1)，最后一个参数才是步长。
    第二，这句写成了nums.pop(nums[i]),里面的参数是索引才对。
'''
