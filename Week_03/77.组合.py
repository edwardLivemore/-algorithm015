#
# @lc app=leetcode.cn id=77 lang=python
#
# [77] 组合
#

# @lc code=start
from copy import copy
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # result = []

        # def helper(sublist, nlist):
        #     if len(sublist) == k:
        #         result.append(sublist)
        #         return
            
        #     for i in range(len(nlist)):
        #         helper(sublist + [nlist[i]], nlist[i + 1:])

        # helper([], list(range(1, n + 1)))
        # return result

        result = []

        def helper(sublist, nlist, index):
            if len(sublist) == k:
                result.append(sublist)
                return
            
            for i in range(index, len(nlist)):
                index += 1
                helper(sublist + [nlist[i]], nlist, index)

        helper([], list(range(1, n + 1)), 0)
        return result
# @lc code=end