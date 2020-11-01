#
# @lc app=leetcode.cn id=680 lang=python
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def checkPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return checkPalindrome(left + 1, right) or checkPalindrome(left, right - 1)
        return True
                
# @lc code=end

