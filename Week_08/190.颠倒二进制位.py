#
# @lc app=leetcode.cn id=190 lang=python
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result, power = 0, 31
        while n:
            result += (n & 1) << power
            n = n >> 1
            power -= 1
        return result
        
# @lc code=end

