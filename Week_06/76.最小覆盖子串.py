#
# @lc app=leetcode.cn id=76 lang=python
#
# [76] 最小覆盖子串
#

# @lc code=start
from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def check():
            for i in map_ori.keys():
                if map_cnt[i] < map_ori[i]:
                    return False
            return True

        map_ori = defaultdict(int)
        map_cnt = defaultdict(int)

        len_max = float('inf')
        len_s = len(s)
        len_t = len(t)
        ansLeft, ansRight = -1, -1

        for c in t:
            map_ori[c] += 1

        left, right = 0, -1

        while right < len_s:
            right += 1

            if right < len_s and s[right] in map_ori:
                map_cnt[s[right]] += 1

            while check() and left <= right:
                if right - left + 1 < len_max:
                    len_max = right - left + 1
                    ansLeft = left
                    ansRight = left + len_max

                if s[left] in map_ori:
                    map_cnt[s[left]] -= 1
                
                left += 1
        
        return '' if ansLeft == -1 else s[ansLeft:ansRight]
# @lc code=end

