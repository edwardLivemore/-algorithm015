#
# @lc app=leetcode.cn id=127 lang=python
#
# [127] 单词接龙
#

# @lc code=start
from collections import defaultdict


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # 单向BFS
        # 判断endword是否在wordlist中以及其他边界检查
        if not wordList or not beginWord or not endWord or endWord not in wordList:
            return 0

        dic = defaultdict(list)

        # 预处理wordlist
        for word in wordList:
            for i in range(len(word)):
                dic[word[:i] + '*' + word[i + 1:]].append(word)

        queue = [(beginWord, 1)]
        visited = {beginWord}

        while queue:
            current_word, level = queue.pop(0)
            for i in range(len(current_word)):
                pair_word = current_word[:i] + '*' + current_word[i + 1:]
                for word in dic[pair_word]:
                    if word == endWord:
                        return level + 1

                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
                dic[pair_word] = []
        return 0
        
# print(Solution().ladderLength('hit', 'cog', ['hot','dot','dog','lot','log','cog']))
# @lc code=end
