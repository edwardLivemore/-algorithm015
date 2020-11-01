#
# @lc app=leetcode.cn id=8 lang=python
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        max_int =  2 ** 31 - 1
        min_val = -2 ** 31

        index, sign, result = 0, 1, 0
        lens = len(s)
        while index < lens and s[index] == ' ' :
            index += 1
        
        if index < lens and (s[index] == '+' or s[index] == '-'):
            sign = 1 if s[index] == '+' else -1
            index += 1
        
        while index < lens:
            digit = ord(s[index]) - ord('0')
            if digit < 0 or digit > 9:
                break

            if max_int // 10 < result or (max_int // 10 == result and max_int % 10 < digit):
                return max_int if sign == 1 else min_val

            result = result * 10 + digit
            index += 1

        return sign * result
# @lc code=end

