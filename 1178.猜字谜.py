#
# @lc app=leetcode.cn id=1178 lang=python3
#
# [1178] 猜字谜
#
# 外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。
# 字谜的迷面 puzzle 按字符串形式给出，如果一个单词 word 符合下面两个条件，那么它就可以算作谜底：
# 单词 word 中包含谜面 puzzle 的第一个字母。
# 单词 word 中的每一个字母都可以在谜面 puzzle 中找到。
# 例如，如果字谜的谜面是 "abcdefg"，那么可以作为谜底的单词有 "faced", "cabbage", 和 "baggage"；而 "beefed"（不含字母 "a"）以及 "based"（其中的 "s" 没有出现在谜面中）则不满足条件。
# 返回一个答案数组 answer，数组中的每个元素 answer[i] 是在给出的单词列表 words 中可以作为字谜迷面 puzzles[i] 所对应的谜底的单词数目。

# 示例：
# 输入：
# words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"],
# puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
# 输出：[1, 1, 3, 2, 4, 0]
# 解释：
# 1 个单词可以作为 "aboveyz" 的谜底: "aaaa"
# 1 个单词可以作为 "abrodyz" 的谜底: "aaaa"
# 3 个单词可以作为 "abslute" 的谜底: "aaaa", "asas", "able"
# 2 个单词可以作为 "absoryz" 的谜底: "aaaa", "asas"
# 4 个单词可以作为 "actresz" 的谜底: "aaaa", "asas", "actt", "access"
# 没有单词可以作为 "gaswxyz" 的谜底，因为列表中的单词都不含字母 'g'。

# 提示：
# 1 <= words.length <= 10 ^ 5
# 4 <= words[i].length <= 50
# 1 <= puzzles.length <= 10 ^ 4
# puzzles[i].length == 7
# words[i][j], puzzles[i][j] 都是小写英文字母。
# 每个 puzzles[i] 所包含的字符都不重复。

from typing import List
from collections import Counter
# @lc code=start


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # 这个解法会超时
        # wordSet = [set(w) for w in words]  # 转换成字符集合
        # answers = []
        # for p in puzzles:
        #     pSet = set(p)
        #     cnt = 0
        #     for ws in wordSet:
        #         if p[0] in ws and ws.issubset(pSet):
        #             cnt += 1
        #     answers.append(cnt)

        # 优化是对wordSet做进一步压缩，去掉重复，对puzzle也做去重 ——还是超时
        # wordSet = [frozenset(w) for w in words]  # 转换成字符集合
        # wordCnt = Counter(filter(lambda ws: len(ws) <= 7, wordSet))
        # answers = []
        # cache = {}
        # for p in puzzles:
        #     pSet = frozenset(p)
        #     key = (p[0], pSet)
        #     if key not in cache:
        #         cnt = 0
        #         for ws in wordCnt:
        #             if p[0] in ws and ws.issubset(pSet):
        #                 cnt += wordCnt.get(ws)
        #         cache[key] = cnt
        #     else:
        #         cnt = cache[key]
        #     answers.append(cnt)
        # return answers

        # 继续优化
        # 因为puzzle[i]长度<=7，所以words里>7的可以不要
        wordCnt = Counter(
            filter(lambda ws: len(ws) <= 7, map(frozenset, words)))

        def match(puzzle) -> int:
            cbt = [puzzle[0]]
            for c in puzzle[1:]:
                cbt += [s + c for s in cbt]
            # cbt为puzzle的所有可能子集（一定包含首字母）
            return sum(wordCnt[s] for s in map(frozenset, cbt) if s in wordCnt)
        return [*map(match, puzzles)]

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    # expected answer: [0,1,3,2,0]
    print(solution.findNumOfValidWords(
        ["apple", "pleas", "please"], ["aelwxyz", "aelpxyz", "aelpsxy", "saelpxy", "xaelpsy"]))

    print(solution.findNumOfValidWords(
        ["aaaa", "asas", "able", "ability", "actt", "actor", "access"], ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]))
