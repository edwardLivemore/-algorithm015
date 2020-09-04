#
# @lc app=leetcode.cn id=264 lang=python
#
# [264] 丑数 II
#

# @lc code=start
# 堆
from heapq import *
class Ugly:
    def __init__(self):
        map = {1,}
        self.nums = []
        basic = [2,3,5]
        heap = []
        heappush(heap, 1)

        for _ in range(1690):
            min_element = heappop(heap)
            self.nums.append(min_element)
            for _basic in basic:
                current = min_element * _basic
                if current not in map:
                    map.add(current)
                    heappush(heap, current)

class Solution(object):
    ugly = Ugly()
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.ugly.nums[n - 1]
        
# 动态规划
# class Ugly:
#     def __init__(self):
#         self.nums = [1]
#         i2 = i3 = i5 = 0

#         for i in range(1, 1690):
#             min_value = min(self.nums[i2] * 2,
#                             self.nums[i3] * 3, self.nums[i5] * 5)

#             self.nums.append(min_value)

#             if self.nums[i2] * 2 == min_value:
#                 i2 += 1
#             if self.nums[i3] * 3 == min_value:
#                 i3 += 1
#             if self.nums[i5] * 5 == min_value:
#                 i5 += 1

# class Solution(object):
#     ugly = Ugly()
#     def nthUglyNumber(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         return self.ugly.nums[n - 1]
# @lc code=end