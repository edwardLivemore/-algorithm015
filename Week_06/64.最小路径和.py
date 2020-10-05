#
# @lc app=leetcode.cn id=64 lang=python
#
# [64] 最小路径和
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        if grid and grid[0]:
            m, n = len(grid), len(grid[0])
            dp = [[0] * n for _ in range(m)]

            # 从起点到终点
            m, n = len(grid), len(grid[0])
            dp = [[0] * n for _ in range(m)]
            dp[0][0] = grid[0][0]
            for i in range(1, m):
                dp[i][0] = dp[i - 1][0] + grid[i][0]
            for j in range(1, n):
                dp[0][j] = dp[0][j - 1] + grid[0][j]
            for i in range(1, m):
                for j in range(1, n):
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
            result = dp[m - 1][n - 1]

            # 从终点到起点
            # dp[m - 1][n - 1] = grid[m - 1][n - 1]
            # for i in range(m - 2, -1, -1):
            #     dp[i][n - 1] = dp[i + 1][n - 1] + grid[i][n - 1]
            # for j in range(n - 2, -1, -1):
            #     dp[m - 1][j] = dp[m - 1][j + 1] + grid[m - 1][j]
            # for i in range(m - 2, -1, -1):
            #     for j in range(n - 2, -1, -1):
            #         dp[i][j] = min(dp[i][j + 1], dp[i + 1][j]) + grid[i][j]
            # result = dp[0][0]

        return result

# print(Solution().minPathSum([[1,3,1], [1,5,1], [4,2,1]]))
# @lc code=end

