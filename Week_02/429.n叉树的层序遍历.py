#
# @lc app=leetcode.cn id=429 lang=python
#
# [429] N叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        # 队列法
        # result, current_layer = [], []

        # if root:
        #     current_layer.append(root)
        
        # while current_layer:
        #     result.append([])
        #     next_layer = []
        #     for node in current_layer:
        #         if node:
        #             result[-1].append(node.val)
        #             next_layer.extend(node.children)
        #     current_layer = next_layer
            
        # return result

        # 递归法
        result = []

        def helper(node, level):
            if len(result) == level:
                result.append([])
            if node:
                result[level].append(node.val)
                for child in node.children:
                    helper(child, level + 1)
        
        if root:
            helper(root, 0)
        
        return result
# @lc code=end
