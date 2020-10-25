#
# @lc app=leetcode.cn id=52 lang=python
#
# [52] N皇后 II
#

# @lc code=start
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0

        self.result = 0

        def dfs(row, cols, pie, na):
            if row >= n:
                self.result += 1
                return
            # 获取当前所有的空位
            bits = (~(cols | pie | na)) & (( 1 << n) - 1)

            while bits:
                # 取得最低位的1
                p = bits & -bits
                dfs(row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)
                # 去掉最后最低位的1，即取出下个位置的皇后
                bits = bits & (bits - 1)

        dfs(0, 0, 0, 0)
        return self.result

# @lc code=end

