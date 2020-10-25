class Solution(object):
    def bubleSort(self, nums):
        m = len(nums)
        for i in range(m - 1):
            for j in range(m - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

print(Solution().bubleSort([4,3,5,2,1]))