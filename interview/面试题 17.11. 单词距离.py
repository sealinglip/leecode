# 有个内含单词的超大文本文件，给定任意两个不同的单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，你能对此优化吗?

# 示例：
# 输入：words = ["I", "am", "a", "student", "from", "a", "university", "in", "a", "city"], word1 = "a", word2 = "student"
# 输出：1

# 提示：
# words.length <= 100000
from typing import List


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        res = len(words)
        idx1 = idx2 = -1
        for i, w in enumerate(words):
            if w == word1:
                idx1 = i
                if idx2 != -1:
                    res = min(res, idx1 - idx2)
            elif w == word2:
                idx2 = i
                if idx1 != -1:
                    res = min(res, idx2 - idx1)
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.findClosest(
        ["I", "am", "a", "student", "from", "a", "university", "in", "a", "city"], "a", "student"))  # 1
