#
# @lc app=leetcode.cn id=455 lang=python
#
# [455] 分发饼干
#

# @lc code=start
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        i, j = 0, 0
        if g and s:
            len_g = len(g)
            len_s = len(s)
            g.sort()
            s.sort()
            while i < len_g and j < len_s:
                if g[i] <= s[j]:
                    i += 1
                j += 1
        return i
# @lc code=end

