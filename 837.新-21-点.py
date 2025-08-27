#
# @lc app=leetcode.cn id=837 lang=python3
#
# [837] 新 21 点
#
# https://leetcode.cn/problems/new-21-game/description/
#
# algorithms
# Medium (39.76%)
# Likes:    431
# Dislikes: 0
# Total Accepted:    31.6K
# Total Submissions: 75.5K
# Testcase Example:  '10\n1\n10'
#
# 爱丽丝参与一个大致基于纸牌游戏 “21点” 规则的游戏，描述如下：
# 
# 爱丽丝以 0 分开始，并在她的得分少于 k 分时抽取数字。 抽取时，她从 [1, maxPts] 的范围中随机获得一个整数作为分数进行累计，其中
# maxPts 是一个整数。 每次抽取都是独立的，其结果具有相同的概率。
# 
# 当爱丽丝获得 k 分 或更多分 时，她就停止抽取数字。
# 爱丽丝的分数不超过 n 的概率是多少？
# 与实际答案误差不超过 10^-5 的答案将被视为正确答案。
# 
# 
# 示例 1：
# 输入：n = 10, k = 1, maxPts = 10
# 输出：1.00000
# 解释：爱丽丝得到一张牌，然后停止。
# 
# 示例 2：
# 输入：n = 6, k = 1, maxPts = 10
# 输出：0.60000
# 解释：爱丽丝得到一张牌，然后停止。 在 10 种可能性中的 6 种情况下，她的得分不超过 6 分。
# 
# 示例 3：
# 输入：n = 21, k = 17, maxPts = 10
# 输出：0.73278
# 
# 
# 提示：
# 0 <= k <= n <= 10^4
# 1 <= maxPts <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k + maxPts - 1 < n:
            return 1
        
        dp = [0.0] * (k + maxPts)
        for i in range(k, n + 1):
            dp[i] = 1.0

        s = n - k + 1
        for i in range(k-1, -1, -1):
            dp[i] = s / float(maxPts)
            s += dp[i] - dp[i + maxPts]

        return dp[0]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.new21Game(10, 1, 10)) # 1
    print(solution.new21Game(6, 1, 10)) # 0.6
    print(solution.new21Game(21, 17, 10)) # 0.73278
    print(solution.new21Game(28, 17, 10)) # q

