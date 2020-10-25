class Solution(object):
    def quickSort(self, nums):
        def myQuickSort(nums, begin, end):
            if begin >= end:
                return
            pivot = partition(nums, begin, end)
            myQuickSort(nums, begin, pivot - 1)
            myQuickSort(nums, pivot + 1, end)

        def partition(nums, begin, end):
            pivot = end
            counter = begin
            for i in range(begin, end):
                if nums[i] < nums[pivot]:
                    nums[i], nums[counter] = nums[counter], nums[i]
                    counter += 1
            nums[counter], nums[pivot] = nums[pivot], nums[counter]
            return counter

        if nums:
            myQuickSort(nums, 0, len(nums) - 1)
        return nums

print(Solution().quickSort([4,3,5,2,1]))