#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

# 示例 1：
# 输入：text1 = "abcde", text2 = "ace"
# 输出：3
# 解释：最长公共子序列是 "ace" ，它的长度为 3 。

# 示例 2：
# 输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc" ，它的长度为 3 。

# 示例 3：
# 输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0 。

# 提示：
# 1 <= text1.length, text2.length <= 1000
# text1 和 text2 仅由小写英文字符组成。

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        # 动态规划
        # 定义dp[m][n] 为 text1[:m]和text2[:n]的最长公共子序列长度
        # 则有dp[m][n] = 0 if m == 0 or n == 0
        #             = dp[m-1][n-1] + 1 if text1[m-1] == text2[n-1]
        #             = max(dp[m][n-1], dp[m-1][n]) if text1[m-1] != text2[n-1]
        dp = [[0] * (N + 1) for _ in range(M + 1)]  # 初始都为0
        for m in range(M):
            for n in range(N):
                if text1[m] == text2[n]:
                    dp[m+1][n+1] = dp[m][n] + 1
                else:
                    dp[m+1][n+1] = max(dp[m+1][n], dp[m][n+1])

        return dp[M][N]
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonSubsequence("abcba", "abcbcba"))
    print(solution.longestCommonSubsequence("abcde", "ace"))
    print(solution.longestCommonSubsequence("abc", "abc"))
    print(solution.longestCommonSubsequence("abc", "def"))
