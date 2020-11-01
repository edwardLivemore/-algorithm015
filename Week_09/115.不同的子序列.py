#
# @lc app=leetcode.cn id=115 lang=python
#
# [115] 不同的子序列
#

# @lc code=start

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(m + 1):
            dp[0][i] = 1

        for i in range(1, n + 1):
            for j in range(i, m + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[n][m]

# print(Solution().numDistinct('rabbbit', 'rabbit'))
# @lc code=end

