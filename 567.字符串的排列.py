#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
# 换句话说，第一个字符串的排列之一是第二个字符串的子串。

# 示例1:
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一("ba").

# 示例2:
# 输入: s1 = "ab" s2 = "eidboaoo"
# 输出: False

# 注意：
# 输入的字符串只包含小写字母
# 两个字符串的长度都在[1, 10,000] 之间

# @lc code=start
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        N = len(s1)

        cur = Counter(s2[:N])
        if cur == target:
            return True
        for i in range(len(s2) - N):
            cur.update(s2[i + N])
            cur.subtract(s2[i])
            if cur[s2[i]] == 0:
                del cur[s2[i]]
            if cur == target:
                return True

        return False
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.checkInclusion("ab", "eidbaooo"))
    print(solution.checkInclusion("ab", "eidboaoo"))
