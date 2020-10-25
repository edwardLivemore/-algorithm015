学习笔记
这周主要学习了位运算、布隆过滤器、LRU缓存和排序算法。
位运算:
    常见的位运算操作有:
    <<: 左移(相当于乘法)
    >>: 右移(相当于除法)
    | : 或运算(有1则1)
    & : 与运算(有0则0)
    ~ : 取反运算(0转1, 1转0)
    ^ : 异或运算(不同为1, 相同为0)
    x & (~0 << n) : 将x最右边的n位清零
    (x >> n) & 1 : 获取x的第n位值
    x & ( 1 << n) : 获取x的第n位幂值
    x | (1 << n) : 仅将x的第n位置为1
    x & (~ (1 << n)) : 仅将x的第n位置为0
    x & ((1 << n) - 1) : 将x的最高位至n位清零
    x & (x - 1) : 清零最低位的1
    x & -x : 得到最低位的1

布隆过滤器:
    通过将输入的参数转化为0和1组成的bit，并判断该bit是否存在于缓存数组中，来判断
    这个参数是否存在。由于是位运算，所以查询效率远超一般的搜算算法。但布隆过滤器也有
    缺点，就是会发生误判，通过布隆过滤器得到的结果，如果为False则表示该参数肯定不存在，
    但若结果为True，则该参数有可能存在，所以布隆过滤器一般用于最外层的筛选过滤。

LRU缓存:
    通过哈希表和双向链表组成的结构，存储最近使用过的元素，当存储的元素个数达到阈值且有
    新元素加入时，则淘汰链表中队尾的元素(即最久未被访问的元素),同时，每次有新元素加入或
    被访问时，都将该元素移动到队首。

排序算法:
    比较类排序: 
        交换排序(冒泡排序、快速排序)
        插入排序(简单插入排序、希尔排序)
        选择排序(简单选择排序、堆排序)
        归并排序(二路归并排序、多路归并排序)
    非比较排序:
        计数排序、桶排序、基数排序
    冒泡排序(时间复杂度O(n * n), 稳定):
    ```
    class Solution(object):
    def bubleSort(self, nums):
        m = len(nums)
        for i in range(m - 1):
            for j in range(m - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
    ```
    快速排序(时间复杂度O(n * logn), 不稳定):
    ```
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

    ```
    插入排序(时间复杂度O(n * n), 稳定):
    ```
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
    ```
    选择排序(时间复杂度O(n * n), 稳定):
    ```
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
    ```
    堆排序(时间复杂度O(n * logn), 不稳定):
    ```
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
    ```
    归并排序(时间复杂度O(n * logn), 稳定):
    ```
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

    ```
