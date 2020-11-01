#
# @lc app=leetcode.cn id=917 lang=python
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        # 栈
        # stack, result = [], []
        # for c in S:
        #     if c.isalpha():
        #         stack.append(c)
        
        # for c in S:
        #     if c.isalpha():
        #         result.append(stack.pop())
        #     else:
        #         result.append(c)
        # return ''.join(result)

        # 双指针
        i, j, result = 0, len(S) - 1, []
        for i in range(len(S)):
            if S[i].isalpha():
                while not S[j].isalpha():
                    j -= 1
                result.append(S[j])
                j -= 1
            else:
                result.append(S[i])
        return ''.join(result)
                
# @lc code=end

