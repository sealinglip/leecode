#
# @lc app=leetcode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
#
# 给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

# 示例：
# 输入: "sea", "eat"
# 输出: 2
# 解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"

# 提示：
# 给定单词的长度不超过500。
# 给定单词中的字符只含有小写字母。

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 可转换为只有一个单词运行增删，另一个单词不变，求最短距离
        # 定义dp(a, b)为word1前a个字符和word2前b个字符的两个子字符串的最短编辑距离
        # dp(a, b) = a + b if a == 0 or b == 0
        #          = min(dp(a-1, b) + 1, dp(a, b-1) + 1, dp(a-1, b-1) + (2 if word1[a-1] != word2[b-1] else 0))
        N, M = len(word1), len(word2)

        dp = [[0] * (M + 1) for _ in range(N + 1)]
        # 初始化边界
        for j in range(M + 1):
            dp[0][j] = j
        for i in range(N + 1):
            dp[i][0] = i

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1]
                               [j-1] + (2 if word1[i-1] != word2[j-1] else 0))

        return dp[N][M]

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.minDistance("leetcode", "etco"))  # 4
    print(solution.minDistance("sea", "eat"))  # 2
