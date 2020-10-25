class Solution(object):
    def insertionSort(self, nums):
        m = len(nums)
        for i in range(1, m):
            num = nums[i]
            # 二分查找, 找到插入下标
            index, low, high = 0, 0, i - 1
            while low <= high:
                mid = low + ((high - low) >> 1 )
                if num == nums[mid]:
                    index = mid
                    break
                if num < nums[mid]:
                    high = mid - 1
                    index = high if high >= 0 else 0
                else:
                    low = mid + 1
                    index = low
            while i > index:
                nums[i] = nums[i - 1]
                i -= 1
            nums[index] = num

        return nums

# print(Solution().insertionSort([4,3,5,2,1]))