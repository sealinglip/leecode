#
# @lc app=leetcode.cn id=940 lang=python3
#
# [940] 不同的子序列 II
#

# 给定一个字符串 s，计算 s 的 不同非空子序列 的个数。因为结果可能很大，所以返回答案需要对 10 ^ 9 + 7 取余 。

# 字符串的 子序列 是经由原字符串删除一些（也可能不删除）字符但不改变剩余字符相对位置的一个新字符串。

# 例如，"ace" 是 "abcde" 的一个子序列，但 "aec" 不是。


# 示例 1：
# 输入：s = "abc"
# 输出：7
# 解释：7 个不同的子序列分别是 "a", "b", "c", "ab", "ac", "bc", 以及 "abc"。

# 示例 2：
# 输入：s = "aba"
# 输出：6
# 解释：6 个不同的子序列分别是 "a", "b", "ab", "ba", "aa" 以及 "aba"。

# 示例 3：
# 输入：s = "aaa"
# 输出：3
# 解释：3 个不同的子序列分别是 "a", "aa" 以及 "aaa"。


# 提示：
# 1 <= s.length <= 2000
# s 仅由小写英文字母组成

# Hard
# 复习

# @lc code=start
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10 ** 9 + 7

        g = [0] * 26
        total = 0
        for c in s:
            oi = ord(c) - ord('a')
            g[oi], total = (total + 1) % MOD, (total * 2 + 1 - g[oi]) % MOD

        return total


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.distinctSubseqII("abc"))  # 7
    print(solution.distinctSubseqII("aba"))  # 6
    print(solution.distinctSubseqII("aaa"))  # 3
