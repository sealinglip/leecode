#
# @lc app=leetcode.cn id=767 lang=python3
#
# [767] 重构字符串
#
# 给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。

# 若可行，输出任意可行的结果。若不可行，返回空字符串。

# 示例 1:
# 输入: S = "aab"
# 输出: "aba"

# 示例 2:
# 输入: S = "aaab"
# 输出: ""

# 注意:
# S 只包含小写字母并且长度在[1, 500]区间内。
from collections import Counter
# @lc code=start
class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S:
            return ""

        # 判断是否有解
        cnt = Counter(S)
        chars = cnt.most_common() # 从多到少排列的字符
        most = chars[0][1]

        L = len(S)
        limit = ((L >> 1) + 1) if (L & 1) else (L >> 1)
        if most > limit:
            return ""

        res = [None] * L
        pos = 0
        for c, cCnt in chars:
            for i in range(cCnt):
                res[pos] = c
                pos += 2
                if pos >= L:
                    pos = 1

        return "".join(res)
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.reorganizeString("aab"))
    print(solution.reorganizeString("aaab"))