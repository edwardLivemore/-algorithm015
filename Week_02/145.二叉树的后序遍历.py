#
# @lc app=leetcode.cn id=145 lang=python
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归法
        # result = []
        # def helper(root):
        #     if root:
        #         helper(root.left)
        #         helper(root.right)
        #         result.append(root.val)
        # helper(root)
        # return result

        # 迭代法, 栈遍历
        result, stack = [], []

        if root:
            stack.append(root)
        
        while stack:
            current = stack.pop()
            if current:
                stack.append(current.val)
                stack.append(None)
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)
            else:
                result.append(stack.pop())
                 
        return result
# @lc code=end

