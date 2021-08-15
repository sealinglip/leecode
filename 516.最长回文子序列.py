#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#
# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

# 子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。


# 示例 1：
# 输入：s = "bbbab"
# 输出：4
# 解释：一个可能的最长回文子序列为 "bbbb" 。

# 示例 2：
# 输入：s = "cbbd"
# 输出：2
# 解释：一个可能的最长回文子序列为 "bb" 。


# 提示：
# 1 <= s.length <= 1000
# s 仅由小写英文字母组成

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 记dp(i,j) 为 s[i:i+j)里最长回文子序列长度，0 <= j <= len(s), 0 <= i <= len(s) - j
        # dp(i, j) = max(dp(i+1, j-1), dp(i, j-1), dp(i+1, j-2) + (2 if s[i] == s[i+j-1] else 0))
        # dp(i, 0) = 0
        # dp(i, 1) = 1
        N = len(s)
        dp = [[0] * N for _ in range(N + 1)]
        for i in range(N):
            dp[1][i] = 1

        for j in range(2, N + 1):
            for i in range(N - j + 1):
                dp[j][i] = max(dp[j-1][i+1], dp[j-1][i], dp[j-2][i+1]
                               + (2 if s[i] == s[i+j-1] else 0))

        return dp[N][0]
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindromeSubseq("bbbab"))
    print(solution.longestPalindromeSubseq("cbbd"))
