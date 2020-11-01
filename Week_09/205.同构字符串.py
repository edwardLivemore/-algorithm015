#
# @lc app=leetcode.cn id=205 lang=python
#
# [205] 同构字符串
#

# @lc code=start
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map = {}
        lens = len(s)
        for i in range(lens):
            if s[i] not in map:
                if t[i] in map.values():
                    return False
                map[s[i]] = t[i]
            else:
                if map[s[i]] != t[i]:
                    return False
        return True
# @lc code=end

