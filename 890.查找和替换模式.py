#
# @lc app=leetcode.cn id=890 lang=python3
#
# [890] 查找和替换模式
#
# 你有一个单词列表 words 和一个模式  pattern，你想知道 words 中的哪些单词与模式匹配。

# 如果存在字母的排列 p ，使得将模式中的每个字母 x 替换为 p(x) 之后，我们就得到了所需的单词，那么单词与模式是匹配的。

# （回想一下，字母的排列是从字母到字母的双射：每个字母映射到另一个字母，没有两个字母映射到同一个字母。）

# 返回 words 中与给定模式匹配的单词列表。

# 你可以按任何顺序返回答案。


# 示例：
# 输入：words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern = "abb"
# 输出：["mee", "aqq"]
# 解释：
# "mee" 与模式匹配，因为存在排列 {a -> m, b -> e, ...}。
# "ccc" 与模式不匹配，因为 {a -> c, b -> c, ...} 不是排列。
# 因为 a 和 b 映射到同一个字母。


# 提示：
# 1 <= words.length <= 50
# 1 <= pattern.length = words[i].length <= 20

from typing import List
# @lc code=start


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word: str, pattern: str) -> bool:
            # 题目已经确定长度一致，这里就不校验了
            map = [None] * 26  # 初始都没有映射
            mask = 0
            for s, d in zip(word, pattern):
                si = ord(s) - ord('a')
                di = ord(d) - ord('a')
                if (map[si] and d != map[si]) or (map[si] is None and (mask & (1 << di)) != 0):
                    return False
                else:
                    map[si] = d
                    mask |= (1 << di)
            return True

        res = []
        for w in words:
            if match(w, pattern):
                res.append(w)
        return res


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findAndReplacePattern(
        ["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))  # ["mee", "aqq"]
