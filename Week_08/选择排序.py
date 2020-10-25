class Solution(object):
    def selectionSort(self, nums):
        m = len(nums)
        for i in range(m):
            min_index = i
            for j in range(i + 1, m):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums

# print(Solution().selectionSort([4,3,5,2,1])) 