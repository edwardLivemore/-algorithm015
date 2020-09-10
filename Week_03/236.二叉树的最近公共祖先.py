#
# @lc app=leetcode.cn id=236 lang=python
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    result = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def helper(root, p, q):
            if not root:
                return False

            lson = helper(root.left, p, q)
            rson = helper(root.right, p, q)

            if (lson and rson) or ((root.val == p.val or root.val == q.val) and (lson or rson)):
                self.result = root

            return lson or rson or (root.val == p.val or root.val == q.val)
        
        helper(root, p, q)
        return self.result
# @lc code=end
