#
# @lc app=leetcode.cn id=712 lang=python3
#
# [712] 两个字符串的最小ASCII删除和
#
# https://leetcode.cn/problems/minimum-ascii-delete-sum-for-two-strings/description/
#
# algorithms
# Medium (72.21%)
# Likes:    454
# Dislikes: 0
# Total Accepted:    72.6K
# Total Submissions: 98.2K
# Testcase Example:  '"sea"\n"eat"'
#
# 给定两个字符串s1 和 s2，返回 使两个字符串相等所需删除字符的 ASCII 值的最小和 。
# 
# 
# 示例 1:
# 输入: s1 = "sea", s2 = "eat"
# 输出: 231
# 解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
# 在 "eat" 中删除 "t" 并将 116 加入总和。
# 结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
# 
# 示例 2:
# 输入: s1 = "delete", s2 = "leet"
# 输出: 403
# 解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
# 将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
# 结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
# 如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。
# 
# 
# 提示:
# 0 <= s1.length, s2.length <= 1000
# s1 和 s2 由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # 动规
        # 记dp(i,j) = minimumDeleteSum(s1[:i], s2[:j])
        # dp(i,j) = min(dp(i-1,j)+ord(s1[i-1]), dp(i,j-1)+ord(s2[j-1]), dp(i-1,j-1)+(0 if s1[i-1]==s2[j-1] else ord(s1[i-1]) + ord(s2[j-1])))
        m, n = len(s1), len(s2)
        # dp(i,*)只依赖dp(i-1,*)，所以状态矩阵可以压缩成两个轮换的一维dp数组
        dp = [0] * (n+1)
        for j in range(n):
            dp[j+1] = dp[j] + ord(s2[j])
        newDp = [0] * (n+1)

        for i in range(m):
            newDp[0] = dp[0] + ord(s1[i])
            for j in range(n):
                if s1[i] == s2[j]:
                    newDp[j+1] = dp[j]
                else:
                    newDp[j+1] = min(dp[j+1]+ord(s1[i]), newDp[j]+ord(s2[j]))
            dp, newDp = newDp, dp

        return dp[-1]
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumDeleteSum("sea", "eat")) # 231
    print(solution.minimumDeleteSum("delete", "leet")) # 403

