#
# @lc app=leetcode.cn id=647 lang=python
#
# [647] 回文子串
#

# @lc code=start
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 动态规划
        result = 0
        if s:
            lens = len(s)
            dp = [[False] * lens for _ in range(lens)]

            for j in range(lens):
                for i in range(j + 1):
                    # 1.当只有一个字符时，比如 a 自然是一个回文串。
                    # 2.当有两个字符时，如果是相等的，比如 aa，也是一个回文串。
                    # 3.当有三个及以上字符时，比如 ababa 这个字符记作串 1，把两边的 a 去掉，也就是 bab 记作串 2，
                    #   可以看出只要串2是一个回文串，那么左右各多了一个 a 的串 1 必定也是回文串。所以当 s[i]==s[j] 时，
                    #   自然要看 dp[i+1][j-1] 是不是一个回文串。
                    if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                        dp[i][j] = True
                        result += 1
        return result

# print(Solution().countSubstrings('ababa'))
# @lc code=end

