#
# @lc app=leetcode.cn id=541 lang=python
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # a = list(s)
        # for i in range(0, len(a), 2*k):
        #     a[i:i+k] = reversed(a[i:i+k])
        # return "".join(a)

        if not s or k == 0 or k == 1:
            return s
        
        i, temp = 0, list(s)
        lens = len(temp)

        def helper(left, right):
            while left < right:
                temp[left], temp[right] = temp[right], temp[left]
                left += 1
                right -= 1
        
        while True:
            helper(i, min(i + k - 1, lens - 1))
            if i + k > lens:
                break
            i += 2 * k
        return ''.join(temp)

# print(Solution().reverseStr('abcdefg', 2))
# @lc code=end

