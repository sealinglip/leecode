#
# @lc app=leetcode.cn id=1536 lang=python3
#
# [1536] 排布二进制网格的最少交换次数
#
# https://leetcode.cn/problems/minimum-swaps-to-arrange-a-binary-grid/description/
#
# algorithms
# Medium (48.39%)
# Likes:    67
# Dislikes: 0
# Total Accepted:    8K
# Total Submissions: 15.5K
# Testcase Example:  '[[0,0,1],[1,1,0],[1,0,0]]'
#
# 给你一个 n x n 的二进制网格 grid，每一次操作中，你可以选择网格的 相邻两行 进行交换。
# 一个符合要求的网格需要满足主对角线以上的格子全部都是 0 。
# 请你返回使网格满足要求的最少操作次数，如果无法使网格符合要求，请你返回 -1 。
# 主对角线指的是从 (1, 1) 到 (n, n) 的这些格子。
# 
# 
# 示例 1：
# 输入：grid = [[0,0,1],[1,1,0],[1,0,0]]
# 输出：3
# 
# 示例 2：
# 输入：grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# 输出：-1
# 解释：所有行都是一样的，交换相邻行无法使网格符合要求。
# 
# 示例 3：
# 输入：grid = [[1,0,0],[1,1,0],[1,1,1]]
# 输出：0
# 
# 
# 提示：
# n == grid.length
# n == grid[i].length
# 1 <= n <= 200
# grid[i][j] 要么是 0 要么是 1 。
# 
# 
#

from typing import List
# @lc code=start
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # 查找每行最右侧 1 的位置
        maxRight = [-1] * n
        for i in range(n):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 1:
                    maxRight[i] = j
                    break

        res = 0
        # 模拟交换
        for i in range(n):
            k = -1
            for j in range(i, n):
                if maxRight[j] <= i:
                    # 第j行满足i行对右侧 0 的个数要求，它需要 j-i 步交换到i行
                    res += j - i
                    k = j
                    break
            
            if k != -1:
                # 更新[i+1, j+1]区间
                for j in range(k, i, -1):
                    maxRight[j], maxRight[j - 1] = maxRight[j - 1], maxRight[j]
            else:
                # 没找到满足条件的行，无解
                return -1
        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minSwaps([[0,0,1],[1,1,0],[1,0,0]])) # 3
    print(solution.minSwaps([[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]])) # -1
    print(solution.minSwaps([[1,0,0],[1,1,0],[1,1,1]])) # 0
