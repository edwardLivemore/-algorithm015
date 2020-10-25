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
        if not s and not t:
            return True

        len_s, len_t = len(s), len(t)
        if len_s != len_t:
            return False
        
        nums = [0 for _ in range(26)]
        for i in range(len_s):
            nums[ord(s[i]) - ord('a')] += 1
            nums[ord(t[i]) - ord('a')] -= 1

        for i in nums:
            if i:
                return False
        
        return True

# @lc code=end

