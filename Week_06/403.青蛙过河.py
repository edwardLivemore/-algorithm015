#
# @lc app=leetcode.cn id=403 lang=python
#
# [403] 青蛙过河
#

# @lc code=start
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if stones:
            lens = len(stones)

            dp = [[False] * (lens + 1) for _ in range(lens)]
            dp[0][0] = True

            for i in range(1, lens):
                for j in range(i):
                    k = stones[i] - stones[j]
                    
                	# 为什么有这么个判断？
                	# 因为其他石头跳到第 i 个石头跳的步数 k 必定满足 k <= i
                	# 这又是为什么？
                	# 1、比如 nums = [0,1,3,5,6,8,12,17]
                	#    那么第 0 个石头跳到第 1 个石头，步数肯定为 1，然后由于后续最大的步数是 k + 1，
                    #    因此第 1 个石头最大只能跳 2 个单位
                 	#    因此如果逐个往上加，那么第 2 3 4 5 ... 个石头最多依次跳跃的步数是 3 4 5 6...
                	# 2、 第 i 个石头能跳的最大的步数是 i + 1，那么就意味着其他石头 j 跳到第 i 个石头的最大步数只能是 i 或者 j + 1
                	#    而 这个 k 是其他石头跳到 i 石头上来的，因此 k 必须 <= i （或者是 k <= j + 1）
                
                    if k <= i:
                        dp[i][k] = dp[j][k - 1] or dp[j][k] or dp[j][k + 1]
                        # 提前结束循环直接返回结果
                        if i == lens - 1 and dp[i][k]:
                            return True
        return False

# @lc code=end
