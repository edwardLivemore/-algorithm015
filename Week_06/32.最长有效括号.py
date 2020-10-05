#
# @lc app=leetcode.cn id=32 lang=python
#
# [32] 最长有效括号
#

# @lc code=start
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        if s:
            n = len(s)
            dp = [0] * n
            for i in range(n):
                # i-dp[i-1]-1是与当前)对称的位置
                if s[i] == ')' and i - dp[i - 1] - 1 >= 0 and s[i -dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
            result = max(dp)
        return result

# @lc code=end
