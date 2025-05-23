#
# @lc app=leetcode.cn id=1931 lang=python3
#
# [1931] 用三种不同颜色为网格涂色
#
# https://leetcode.cn/problems/painting-a-grid-with-three-different-colors/description/
#
# algorithms
# Hard (61.47%)
# Likes:    58
# Dislikes: 0
# Total Accepted:    5.5K
# Total Submissions: 8.3K
# Testcase Example:  '1\n1'
#
# 给你两个整数 m 和 n 。构造一个 m x n 的网格，其中每个单元格最开始是白色。请你用 红、绿、蓝
# 三种颜色为每个单元格涂色。所有单元格都需要被涂色。
# 
# 涂色方案需要满足：不存在相邻两个单元格颜色相同的情况 。返回网格涂色的方法数。因为答案可能非常大， 返回 对 10^9 + 7 取余 的结果。
# 
# 
# 示例 1：
# 输入：m = 1, n = 1
# 输出：3
# 解释：如上图所示，存在三种可能的涂色方案。
# 
# 示例 2：
# 输入：m = 1, n = 2
# 输出：6
# 解释：如上图所示，存在六种可能的涂色方案。
# 
# 示例 3：
# 输入：m = 5, n = 5
# 输出：580986
# 
# 
# 提示：
# 1 <= m <= 5
# 1 <= n <= 1000
#

# @lc code=start
from collections import defaultdict


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10 ** 9 + 7
        
        valid = {}
        for mask in range(3**m): # 枚举一行所有满足要求的涂色方案
            clr = []
            mm = mask
            for i in range(m):
                clr.append(mm % 3)
                mm //= 3
            if any(clr[i] == clr[i-1] for i in range(1, m)):
                # 有同色，不满足要求
                continue
            valid[mask] = clr

        # 预处理，找出行与行能相邻的关系
        adjacent = defaultdict(list)
        for m1, c1 in valid.items():
            for m2, c2 in valid.items():
                if any(x==y for x, y in zip(c1, c2)):
                    continue
                adjacent[m1].append(m2)
        
        dp = {k: 1 for k in valid.keys()} # dp[i]记录当前行i涂色方案为i时的方案数，第一行的所有满足要求的涂色方案为1
        for i in range(1, n):
            newDp = {k: 0 for k in valid.keys()}
            for m1 in dp.keys():
                for m2 in adjacent[m1]:
                    newDp[m2] += dp[m1]
            for m in newDp.keys():
                if newDp[m] >= MOD:
                    newDp[m] %= MOD
            dp = newDp

        return sum(dp.values()) % MOD
            
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.colorTheGrid(1, 1)) # 3
    print(solution.colorTheGrid(1, 2)) # 6
    print(solution.colorTheGrid(5, 5)) # 580986
