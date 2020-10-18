#
# @lc app=leetcode.cn id=37 lang=python
#
# [37] 解数独
#

# @lc code=start
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = [set(range(1, 10)) for _ in range(9)] # 行剩余可用数字
        col = [set(range(1, 10)) for _ in range(9)] # 列剩余可用数字
        block = [set(range(1, 10)) for _ in range(9)] # 块剩余可用数字

        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i // 3) * 3 + j // 3].remove(val)
                else:
                    empty.append((i, j))

        def backtrack(level):
            if level == len(empty):
                return True
            i, j = empty[level]
            b = (i // 3) * 3 + j // 3
            for val in row[i] & col[j] & block[b]:
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if backtrack(level + 1):
                    return True
                row[i].add(val)
                col[j].add(val)
                block[b].add(val)
            return False

        backtrack(0)
# @lc code=end

