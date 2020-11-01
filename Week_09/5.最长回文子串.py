#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lens = len(s)
        result = ''
        dp = [[False for _ in range(lens)] for _ in range(lens)]
        for i in range(lens - 1, -1, -1):
            for j in range(i, lens):
                dp[i][j] = s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1])
                if dp[i][j] and (j - i + 1) > len(result):
                    result = s[i : j + 1]
        return result
# @lc code=end
