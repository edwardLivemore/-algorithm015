#
# @lc app=leetcode.cn id=242 lang=python
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        
        map = [0] * 26 
        for i in range(len_s):
            map[ord(s[i]) - ord('a')] += 1
            map[ord(t[i]) - ord('a')] -= 1

        for i in range(len(map)):
            if map[i] != 0:
                return False

        return True
# @lc code=end

