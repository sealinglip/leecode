#
# @lc app=leetcode.cn id=1255 lang=python3
#
# [1255] 得分最高的单词集合
#
# '[1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]'
# 你将会得到一份单词表 words，一个字母表 letters （可能会有重复字母），以及每个字母对应的得分情况表 score。

# 请你帮忙计算玩家在单词拼写游戏中所能获得的「最高得分」：能够由 letters 里的字母拼写出的 任意 属于 words 单词子集中，分数最高的单词集合的得分。

# 单词拼写游戏的规则概述如下：

# 玩家需要用字母表 letters 里的字母来拼写单词表 words 中的单词。
# 可以只使用字母表 letters 中的部分字母，但是每个字母最多被使用一次。
# 单词表 words 中每个单词只能计分（使用）一次。
# 根据字母得分情况表score，字母 'a', 'b', 'c', ... , 'z' 对应的得分分别为 score[0], score[1], ..., score[25]。
# 本场游戏的「得分」是指：玩家所拼写出的单词集合里包含的所有字母的得分之和。


# 示例 1：
# 输入：words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
# 输出：23
# 解释：
# 字母得分为  a=1, c=9, d=5, g=3, o=2
# 使用给定的字母表 letters，我们可以拼写单词 "dad" (5+1+5)和 "good" (3+2+2+5)，得分为 23 。
# 而单词 "dad" 和 "dog" 只能得到 21 分。

# 示例 2：
# 输入：words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
# 输出：27
# 解释：
# 字母得分为  a=4, b=4, c=4, x=5, z=10
# 使用给定的字母表 letters，我们可以组成单词 "ax" (4+5)， "bx" (4+5) 和 "cx" (4+5) ，总得分为 27 。
# 单词 "xxxz" 的得分仅为 25 。

# 示例 3：
# 输入：words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
# 输出：0
# 解释：
# 字母 "e" 在字母表 letters 中只出现了一次，所以无法组成单词表 words 中的单词。


# 提示：
# 1 <= words.length <= 14
# 1 <= words[i].length <= 15
# 1 <= letters.length <= 100
# letters[i].length == 1
# score.length == 26
# 0 <= score[i] <= 10
# words[i] 和 letters[i] 只包含小写的英文字母。

# Hard
# 复习

from collections import Counter
from typing import List
# @lc code=start


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        values = [sum(score[ord(c) - ord('a')] for c in w)
                  for w in words]  # 计算出每个单词的得分
        consume = [Counter(w) for w in words]  # 每个单词的消耗
        left = Counter(letters)

        res = 0

        # 直接状态压缩再遍历的方式不利于剪枝
        # dfs+回溯法
        def dfs(idx: int, total: int) -> None:
            if idx < 0:
                nonlocal res
                res = max(res, total)
                return

            # 当前词不选
            dfs(idx - 1, total)

            # 选当前词
            if values[idx] == 0 or (not (left >= consume[idx])):  # 当前词没分 或者 剩余不够选当前词
                return  # 剪枝
            left.subtract(consume[idx])
            dfs(idx - 1, total + values[idx])

            # 恢复
            left.update(consume[idx])

        dfs(len(words)-1, 0)

        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxScoreWords(["dog", "cat", "dad", "good"], [
          "a", "a", "c", "d", "d", "d", "g", "o", "o"], [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))  # 23
    print(solution.maxScoreWords(["xxxz", "ax", "bx", "cx"], [
          "z", "a", "b", "c", "x", "x", "x"], [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]))  # 27
    print(solution.maxScoreWords(["leetcode"],
          ["l", "e", "t", "c", "o", "d"], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]))
