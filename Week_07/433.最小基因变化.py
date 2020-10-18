#
# @lc app=leetcode.cn id=433 lang=python
#
# [433] 最小基因变化
#

# @lc code=start
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        # 单向BFS
        # if not start or not end or not bank or end not in bank:
        #     return -1

        # queue = [(start, 0)]
        # bank = set(bank)

        # while queue:
        #     word, step = queue.pop(0)
        #     if word == end:
        #         return step
        #     for i in range(len(word)):
        #         for w in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        #             new_word = word[:i] + w + word[i + 1:]
        #             if new_word in bank:
        #                 queue.append((new_word, step + 1))
        #                 bank.remove(new_word)
        # return -1

        # 双向BFS
        # Solution 1
        if not start or not end or not bank or end not in bank:
            return -1

        front, back = {start}, {end}
        bank = set(bank)
        step = 0

        while front:
            step += 1
            next_front = set()
            for word in front:
                for i in range(len(word)):
                    for w in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        new_word = word[:i] + w + word[i + 1:]
                        if new_word in back:
                            return step
                        if new_word in bank:
                            next_front.add(new_word)
                            bank.remove(new_word)
            front = next_front
            if len(front) > len(back):
                front, back = back, front
        return -1

        # Solution 2
        # if not start or not end or not bank or end not in bank:
        #     return -1

        # front, back = [(start, 1)], [(end, 0)]
        # bank = set(bank)

        # while front:
        #     next_front = []
        #     for word, step_f in front:
        #         for i in range(len(word)):
        #             for w in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        #                 new_word = word[:i] + w + word[i + 1:]
        #                 if new_word in back[0]:
        #                     word_b, step_b = back.pop(0)
        #                     return step_f + step_b
        #                 if new_word in bank:
        #                     next_front.append((new_word, step_f + 1))
        #                     bank.remove(new_word)
        #     front = next_front
        #     if len(front) > len(back):
        #         front, back = back, front
        # return -1

# print(Solution().minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))
# @lc code=end

