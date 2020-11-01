#
# @lc app=leetcode.cn id=91 lang=python
#
# [91] 解码方法
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0
        pre, cur = 1, 1
        for i in range(1, len(s)):
            temp = cur
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    cur = pre
                else:
                    return 0
            else:
                if s[i - 1] == '1' or (s[i - 1] == '2' and '1' <= s[i] <= '6'):
                    cur += pre
            pre = temp
        return cur
# print(Solution().numDecodings('12'))
# @lc code=end

