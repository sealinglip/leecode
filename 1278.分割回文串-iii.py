#
# @lc app=leetcode.cn id=1278 lang=python3
#
# [1278] 分割回文串 III
#
# 给你一个由小写字母组成的字符串 s，和一个整数 k。

# 请你按下面的要求分割字符串：

# 首先，你可以将 s 中的部分字符修改为其他的小写英文字母。
# 接着，你需要把 s 分割成 k 个非空且不相交的子串，并且每个子串都是回文串。
# 请返回以这种方式分割字符串所需修改的最少字符数。


# 示例 1：
# 输入：s = "abc", k = 2
# 输出：1
# 解释：你可以把字符串分割成 "ab" 和 "c"，并修改 "ab" 中的 1 个字符，将它变成回文串。

# 示例 2：
# 输入：s = "aabbc", k = 3
# 输出：0
# 解释：你可以把字符串分割成 "aa"、"bb" 和 "c"，它们都是回文串。

# 示例 3：
# 输入：s = "leetcode", k = 8
# 输出：0

# 提示：
# 1 <= k <= s.length <= 100
# s 中只含有小写英文字母。

# Hard
# @lc code=start
from math import inf


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        # 动态规划
        # 记dp(i,j)为将s[:i]分隔为j个非空且不相交的回文子串最少需要修改的字符数
        # dp(i, i) = 0

        cost = [[0] * n for _ in range(n)] # cost[i][j] 记录s[i:j+1]要变成回文串最少需要修改的字符数
        for span in range(2, n+1):
            for i in range(n-span+1):
                j = i + span - 1
                cost[i][j] = cost[i+1][j-1] + int(s[i] != s[j])
        
        dp = [[inf] * (k+1) for _ in range(n+1)]
        dp[0][0] = 0
        for i in range(1, n+1):
            for j in range(1, min(k, i) + 1):
                if j == 1:
                    dp[i][j] = cost[0][i-1]
                else:
                    for l in range(j-1, i):
                        dp[i][j] = min(dp[i][j], dp[l][j-1] + cost[l][i-1])

        return dp[n][k]
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.palindromePartition("abc", 2)) # 1
    print(solution.palindromePartition("aabbc", 3)) # 0
    print(solution.palindromePartition("leetcode", 8)) # 0
