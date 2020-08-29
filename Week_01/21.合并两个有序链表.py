#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 递归法
        # if not l1:
        #     return l2
        # if not l2:
        #     return l1
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         l1.next = self.mergeTwoLists(l1.next, l2)
        #         return l1
        #     else:
        #         l2.next = self.mergeTwoLists(l1, l2.next)
        #         return l2

        # 迭代法
        dummy = ListNode(-1)
        prev = dummy

        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 else l2

        return dummy.next
# @lc code=end

