#
# @lc app=leetcode.cn id=347 lang=python
#
# [347] 前 K 个高频元素
#

# @lc code=start
from heapq import *
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 堆
        heap = []
        map = {}
        result = []

        for i in nums:
            if i not in map:
                map[i] = 0
            else:
                map[i] -= 1

        for key in map.keys():
                heappush(heap, (map.get(key), key))

        for _ in range(k):
            result.append(heappop(heap)[1])

        return result

        # 桶排序
        # if not nums or len(nums) <= 1:
        #     return nums
        # lens = len(nums)
        # result = []
        # barket = [[] for _ in range(lens + 1) ]
        # dic = Counter(nums)

        # for key, count in dic.items():
        #     barket[count].append(key)
        
        # for j in range(lens, -1, -1):
        #     result.extend(barket[j])
        #     if len(result) >= k:
        #         return result
# @lc code=end
