#
# @lc app=leetcode.cn id=51 lang=python
#
# [51] N 皇后
#

# @lc code=start
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        def helper(queenlist, pie, na):
            row = len(queenlist)
            if row == n:
                result.append(queenlist)
                return
            for col in range(n):
                if col not in queenlist and row + col not in pie and row - col not in na:
                    helper(queenlist + [col], pie + [row + col], na + [row - col])
        helper([], [], [])
        return [['.' * queen + 'Q' + '.' * (n - queen - 1)  for queen in sol] for sol in result]
# @lc code=end
