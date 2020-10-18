#
# @lc app=leetcode.cn id=127 lang=python
#
# [127] 单词接龙
#

# @lc code=start
from collections import defaultdict

import string
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # 单向BFS
        # if not beginWord or not endWord or not wordList or endWord not in wordList:
        #     return 0

        # dic = defaultdict(list)

        # # 预处理wordlist
        # for word in wordList:
        #     for i in range(len(word)):
        #         dic[word[:i] + '*' + word[i + 1:]].append(word)

        # queue = [(beginWord, 1)]
        # visited = {beginWord}

        # while queue:
        #     current_word, level = queue.pop(0)
        #     if current_word == endWord:
        #         return level

        #     for i in range(len(current_word)):
        #         pair_word = current_word[:i] + '*' + current_word[i + 1:]
        #         for word in dic[pair_word]:
        #             if word not in visited:
        #                 queue.append((word, level + 1))
        #                 visited.add(word)
        #         dic[pair_word] = []
        # return 0

        # 双向BFS
        if endWord not in wordList:
            return 0
        front = {beginWord}
        back = {endWord}
        distance = 1
        wordList = set(wordList)
        while front:
            distance += 1
            next_front = set()
            for word in front:
                for i in range(len(word)):
                    # 'abcdefg....xyz'
                    for c in string.lowercase:
                        if c != word[i]:
                            new_word = word[:i] + c + word[i + 1:]
                            if new_word in back:
                                return distance
                            if new_word in wordList:
                                next_front.add(new_word)
                                wordList.remove(new_word)
            front = next_front
            if len(back) < len(front):
                front, back = back, front
        return 0 


# print(Solution().ladderLength('hit', 'cog', ['hot','dot','dog','lot','log','cog']))
# @lc code=end
