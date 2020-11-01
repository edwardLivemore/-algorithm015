#
# @lc app=leetcode.cn id=387 lang=python
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start

import collections

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        map = collections.Counter(s)
        for idx, ch in enumerate(s):
            if map[ch] == 1:
                return idx
        return - 1

# print(Solution().firstUniqChar('loveleetcode'))
# print(Solution().firstUniqChar('leetcode'))
# @lc code=end

