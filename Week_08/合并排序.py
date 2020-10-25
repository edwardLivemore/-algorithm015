class Solution(object):
    def mergeSort(self, nums):
        def myMergeSort(nums, low, high):
            if low >= high:
                return
            mid = low + ((high - low ) >> 1)
            myMergeSort(nums, low, mid)
            myMergeSort(nums, mid + 1, high)
            merge(nums, low, mid, high)
        
        def merge(nums, low, mid, high):
            temp = []
            i, j = low, mid + 1
            while i <= mid and j <= high:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= high:
                temp.append(nums[j])
                j += 1
            nums[low:high + 1] = temp

        if nums:
            myMergeSort(nums, 0, len(nums) - 1)
        return nums

# print(Solution().mergeSort([4,3,5,2,1]))