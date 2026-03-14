#
# @lc app=leetcode.cn id=1411 lang=python3
#
# [1411] 给 N x 3 网格图涂色的方案数
#
# https://leetcode.cn/problems/number-of-ways-to-paint-n-3-grid/description/
#
# algorithms
# Hard (58.82%)
# Likes:    139
# Dislikes: 0
# Total Accepted:    14K
# Total Submissions: 22.2K
# Testcase Example:  '1'
#
# 你有一个 n x 3 的网格图 grid ，你需要用 红，黄，绿
# 三种颜色之一给每一个格子上色，且确保相邻格子颜色不同（也就是有相同水平边或者垂直边的格子颜色不同）。
# 
# 给你网格图的行数 n 。
# 
# 请你返回给 grid 涂色的方案数。由于答案可能会非常大，请你返回答案对 10^9 + 7 取余的结果。
# 
# 
# 示例 1：
# 输入：n = 1
# 输出：12
# 解释：总共有 12 种可行的方法：
# 
# 示例 2：
# 输入：n = 2
# 输出：54
# 
# 示例 3：
# 输入：n = 3
# 输出：246
# 
# 示例 4：
# 输入：n = 7
# 输出：106494
# 
# 示例 5：
# 输入：n = 5000
# 输出：30228214
# 
# 
# 提示：
# n == grid.length
# grid[i].length == 3
# 1 <= n <= 5000
# 
# 
#

# @lc code=start
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        # 动规结合状态表可解
        # 如果将 n = 1 时的12种状态分成两种类型，两种颜色为A、三种颜色为B
        # 则 A、B各占一半
        # 当如果前一行为A，后一行允许的状态为 3A2B；如果前一行为B，后一行允许的状态为 2A2B

        dpA = dpB = 6 # 代表所有可能的方案中最后一行为A的方案数和为B的方案数
        while n > 1:
            dpA, dpB = (3 * dpA + (dpB << 1)) % MOD, ((dpA + dpB) << 1) % MOD
            n -= 1
        return (dpA + dpB) % MOD
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.numOfWays(1)) # 12
    print(solution.numOfWays(2)) # 54
    print(solution.numOfWays(3)) # 246
    print(solution.numOfWays(7)) # 106494
    print(solution.numOfWays(5000)) # 30228214
