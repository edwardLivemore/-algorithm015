#
# @lc app=leetcode.cn id=144 lang=python
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归法
        # result = []
        # def helper(root):
        #     if root:
        #         result.append(root.val)
        #         helper(root.left)
        #         helper(root.right)
        # helper(root)
        # return result

        # 迭代法一, 栈遍历
        # stack, result = [root, ], []
        
        # while stack:
        #     root = stack.pop()
        #     if root:
        #         result.append(root.val)
        #         if root.right:
        #             stack.append(root.right)
        #         if root.left:
        #             stack.append(root.left)
        
        # return result

        # 迭代法二, 模拟递归
        result, stack = [], []
        if root:
            stack.append(root)
        
        while stack:
            current = stack.pop()
            if current:
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)
                stack.append(current.val)
                stack.append(None)
            else:
                result.append(stack.pop())
        
        return result

# @lc code=end

