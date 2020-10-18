#
# @lc app=leetcode.cn id=547 lang=python
#
# [547] 朋友圈
#

# @lc code=start

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # 构造并查集
        if not M:
            return 0

        n = len(M)
        p = [i for i in range(n)]

        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    self.union(p, i, j)
        
        # wrong answer
        # return len(set([p[i] for i in range(n)]))

        # correct answer
        return len(set([self.findParent(p, i) for i in range(n)]))

    def union(self, p, i, j):
        p1 = self.findParent(p, i)
        p2 = self.findParent(p, j)
        p[p2] = p1

    def findParent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        # 路径压缩
        while p[i] != i:
            x = i
            i = p[i]
            p[x] = root
        return root
# @lc code=end

