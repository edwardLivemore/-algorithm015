#
# @lc app=leetcode.cn id=105 lang=python
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 递归
        map_inorder = {}

        # build inorder index map
        for i in range(len(inorder)):
            map_inorder[inorder[i]] = i

        def helper(index, left_bound, right_bound):
            if left_bound > right_bound:
                return None

            # 1.get and build root from preorder
            node = TreeNode(preorder[index])
            
            # 2. get node index from inorder
            node_index = map_inorder.get(preorder[index])

            # 3.update left child
            node.left = helper(index + 1, left_bound, node_index - 1)

            # 4.update right child
            node.right = helper(index + node_index - left_bound + 1,  node_index + 1, right_bound)

            return node

        root = helper(0, 0, len(inorder) - 1)
        return root


# preorder = [3,9,8,20,15,7]
# inorder = [8,9,3,15,20,7]
# print(Solution().buildTree(preorder, inorder))
# @lc code=end

