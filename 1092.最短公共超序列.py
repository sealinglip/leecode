#
# @lc app=leetcode.cn id=1092 lang=python3
#
# [1092] 最短公共超序列
#
# 给出两个字符串 str1 和 str2，返回同时以 str1 和 str2 作为子序列的最短字符串。如果答案不止一个，则可以返回满足条件的任意一个答案。

# （如果从字符串 T 中删除一些字符（也可能不删除，并且选出的这些字符可以位于 T 中的 任意位置），可以得到字符串 S，那么 S 就是 T 的子序列）


# 示例：
# 输入：str1 = "abac", str2 = "cab"
# 输出："cabac"
# 解释：
# str1 = "abac" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 的第一个 "c"得到 "abac"。
# str2 = "cab" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 末尾的 "ac" 得到 "cab"。
# 最终我们给出的答案是满足上述属性的最短字符串。

# 提示：
# 1 <= str1.length, str2.length <= 1000
# str1 和 str2 都由小写英文字母组成。

# Hard

# @lc code=start
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # 求 str1和str2的最长公共子序列，在此基础上把各自删掉的字符加回即可
        # 记dp(i, j)为str1[:i]和str2[:j]的最长公共子序列的长度
        m, n = len(str1), len(str2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        # 此时dp[m][n]为str1、str2最长公共子序列，回溯dp，将字符输出到缓冲区，结束后翻转拼接字符串即为结果
        i, j = m, n
        buf = []
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                buf.append(str1[i-1])
                i -= 1
                j -= 1
            else:
                if dp[i][j] == dp[i][j-1]:
                    buf.append(str2[j-1])
                    j -= 1
                else:
                    buf.append(str1[i-1])
                    i -= 1
        prefix = str1[:i] if i > 0 else (str2[:j] if j > 0 else '')
        buf.reverse()
        return prefix + ''.join(buf)

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.shortestCommonSupersequence("abac", "cab"))  # "cabac"
