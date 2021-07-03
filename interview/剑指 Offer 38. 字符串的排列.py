# 输入一个字符串，打印出该字符串中字符的所有排列。
# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

# 示例:
# 输入：s = "abc"
# 输出：["abc", "acb", "bac", "bca", "cab", "cba"]
#  
# 限制：
# 1 <= s 的长度 <= 8

from typing import List
from collections import Counter


class Solution:
    def permutation(self, s: str) -> List[str]:
        stat = Counter(s)
        chars = list(stat.keys())
        chars.sort()
        L, N = len(s), len(chars)
        cnt = [stat[c] for c in chars]
        res = []

        def backtrack(stack: List[str]):
            if len(stack) == L:
                res.append("".join(stack))
            else:
                for i in range(N):
                    if cnt[i] > 0:
                        cnt[i] -= 1
                        stack.append(chars[i])
                        backtrack(stack)
                        stack.pop()
                        cnt[i] += 1
        backtrack([])
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.permutation("aba"))
    print(solution.permutation("abca"))
    print(solution.permutation("abc"))
