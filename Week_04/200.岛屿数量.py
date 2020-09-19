#
# @lc app=leetcode.cn id=200 lang=python
#
# [200] 岛屿数量
#

# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        result = 0
        def helper(i, j):
            if i < 0 or i >= row  or j < 0 or j >= col or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                helper(x, y)

        if grid:
            row = len(grid)
            col = len(grid[0])
            
            for i in range(row):
                for j in range(col):
                    if grid[i][j] == '1':
                        result += 1
                        helper(i, j)
        return result
# @lc code=end

