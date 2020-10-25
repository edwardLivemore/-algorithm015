import heapq
from heapq import heapify, heappop, heappush
class Solution(object):
    def heapSort(self, nums):
        if nums:
            heap = []
            heapify(heap)
            for i in nums:
                heappush(heap, i)
            for i in range(len(nums)):
                nums[i] = heappop(heap)
        return nums

# print(Solution().heapSort([4,3,5,2,1]))