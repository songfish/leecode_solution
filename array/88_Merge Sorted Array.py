#coding:utf-8
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        point1 = 0
        point2 = 0
        point = 0
        while point1 < m and point2 < n:
            # print('1:{},2:{}'.format(point1,point2))
            if nums1_copy[point1] < nums2[point2]:
                nums1[point] = nums1_copy[point1]
                point1 += 1
                point += 1
            else:
                nums1[point] = nums2[point2]
                point2 += 1
                point += 1
        if point1 < m:
            nums1[point:] = nums1_copy[point1:]
            point += 1
        if point2 < n:
            nums1[point:] = nums2[point2:]
        return nums1

S = Solution()
print(S.merge([4,0,0,0,0,0],1,[1,2,3,5,6],5))


'''
2020.1.3反思：
1、一开始while循环里面都写的是if，结果对于[1,0],1,[2],1 AC不了，因为两个if都要执行，就超出list的范围。
2、修改了if之后对于用例[4,0,0,0,0,0],1,[1,2,3,5,6],5 AC不了。原因是while的条件写成了point1 < m and point2 < n and point < m。去掉point < m的条件终于AC。

'''