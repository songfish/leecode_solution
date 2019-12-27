#coding:utf-8
# method 1
# class Solution:
#     def plusOne(self, digits):
#         s = 0
#         length = len(digits)
#         for i in range(length):
#             s += pow(10, i) * digits[length-1-i]
#         result = s + 1
#         final_result = []
#         for j in range(length-1, -1, -1):
#             final_result.append(result % 10)
#             result = result // 10
#         if set(final_result) == {0}:
#             final_result.append(1)
#         return final_result[::-1]


# method 2
class Solution:
    def plusOne(self, digits):
        l = len(digits)
        for i in range(l-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
        if set(digits) == {0}:
            digits.insert(0, 1)
        return digits


S = Solution()
print(S.plusOne(digits=[1,2,3]))

'''
2019.12.27反思：
    1、method 1 一开始没有考虑[9],[9,9],[9,9,9]这种情况。最后加上了 if set(final_result) == {0}来判断是否需要进位。
    2、method 2 参考了别人的代码，break这个操作很厉害，一开始没有加，[1,2,3]输出了[2,3,4]。
'''