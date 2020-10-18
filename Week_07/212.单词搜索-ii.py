#
# @lc app=leetcode.cn id=212 lang=python
#
# [212] 单词搜索 II
#

# @lc code=start
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # 构造字典树
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = True

        def dfs(i, j, node, pre, visited):
            if '#' in node:
                result.add(pre)

            # 上右下左
            for (di, dj) in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                new_i, new_j = i + di, j + dj
                if 0 <= new_i < m and 0 <= new_j < n and board[new_i][new_j] in node and (new_i, new_j) not in visited:
                    dfs(new_i, new_j, node[board[new_i][new_j]], 
                        pre + board[new_i][new_j], visited | {(new_i, new_j)})

        result, m, n = set(), len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie[board[i][j]], board[i][j], {(i, j)})
        return list(result)

# print(Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
# @lc code=end
