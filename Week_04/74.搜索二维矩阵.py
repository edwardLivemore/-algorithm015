#
# @lc app=leetcode.cn id=74 lang=python
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        m = len(matrix)
        n = len(matrix[0])

        low, high = 0, m * n - 1

        while low <= high:
            mid = low + (high - low) // 2
            row_m = mid // n
            col_m = mid % n
            if matrix[row_m][col_m] == target:
                return True
            if target < matrix[row_m][col_m]:
                # 在左侧
                high = mid - 1
            else:
                # 在右侧
                low = mid + 1
        return False
# @lc code=end

