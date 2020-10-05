#
# @lc app=leetcode.cn id=221 lang=python
#
# [221] 最大正方形
#

# @lc code=start
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        result = 0
        if matrix and matrix[0]:
            m = len(matrix)
            n = len(matrix[0])
            max_side = 0
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(0, m):
                for j in range(0, n):
                    if matrix[i][j] == '1':
                        dp_i, dp_j = i + 1, j + 1
                        dp[dp_i][dp_j] = min(dp[dp_i - 1][dp_j], dp[dp_i][dp_j - 1], dp[dp_i - 1][dp_j - 1]) + 1
                        max_side = max(max_side, dp[dp_i][dp_j])
            result = max_side * max_side
        return result

        # result = 0
        # if not matrix or not matrix[0]:
        #     return result

        # max_side, rows, colums = 0, len(matrix), len(matrix[0])
        # dp = [[0] * colums for _ in range(rows)]

        # for i in range(rows):
        #     for j in range(colums):
        #         if matrix[i][j] == '1':
        #             if i == 0 or j == 0:
        #                 dp[i][j] = 1
        #             else:
        #                 dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        #             max_side = max(max_side, dp[i][j])

        # result = max_side * max_side
        # return result
# @lc code=end

