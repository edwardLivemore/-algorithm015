#
# @lc app=leetcode.cn id=589 lang=python
#
# [589] N叉树的前序遍历
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
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack, result = [root, ], []            
        while stack:
            root = stack.pop()
            result.append(root.val)
            stack.extend(root.children[::-1])
                
        return result
# @lc code=end
