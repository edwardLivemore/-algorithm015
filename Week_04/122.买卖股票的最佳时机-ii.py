#
# @lc app=leetcode.cn id=122 lang=python
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        if prices:
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    result += prices[i] - prices[i - 1]
        return result
# @lc code=end

