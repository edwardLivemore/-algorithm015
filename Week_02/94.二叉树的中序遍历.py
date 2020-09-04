#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归法
        # result = []
        # def helper(root):
        #     if root:
        #         helper(root.left)
        #         result.append(root.val)
        #         helper(root.right)
        # helper(root)    
        # return result

        # 迭代法一, 栈遍历
        # result, stack, cur = [], [], root
        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     result.append(cur.val)
        #     cur = cur.right
        # return result

        # 迭代法二, 栈模拟
        result, stack = [], []

        if root:
            stack.append(root)

        while stack:
            current = stack.pop()
            if current:
                if current.right:
                    stack.append(current.right)
                stack.append(current.val)
                stack.append(None)
                if current.left:
                    stack.append(current.left)
            else:
                result.append(stack.pop())

        return result
# @lc code=end

