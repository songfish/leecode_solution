#coding:utf-8
class Solution:
    def plusOne(self, digits):
        s = 0
        length = len(digits)
        for i in range(length):
            s += pow(10, i) * digits[length-1-i]
        result = s + 1
        final_result = []
        for j in range(length-1, -1, -1):
            final_result.append(result % 10)
            result = result // 10
        if set(final_result) == {0}:
            final_result.append(1)
        return final_result[::-1]


S = Solution()
print(S.plusOne(digits=[9,9,9]))

'''
2019.12.27反思：
    一开始没有考虑[9],[9,9],[9,9,9]这种情况。最后加上了 if set(final_result) == {0}来判断是否需要进位。
'''