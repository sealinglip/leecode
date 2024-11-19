# 给你一个 m x n 的二进制矩阵 grid 。
# 如果矩阵中一行或者一列从前往后与从后往前读是一样的，那么我们称这一行或者这一列是 回文 的。
# 你可以将 grid 中任意格子的值 翻转 ，也就是将格子里的值从 0 变成 1 ，或者从 1 变成 0 。
# 请你返回 最少 翻转次数，使得矩阵中 所有 行和列都是 回文的 ，且矩阵中 1 的数目可以被 4 整除 。


# 示例 1：
# 输入：grid = [[1,0,0],[0,1,0],[0,0,1]]
# 输出：3
# 解释：

# 示例 2：
# 输入：grid = [[0,1],[0,1],[0,0]]
# 输出：2
# 解释：

# 示例 3：
# 输入：grid = [[1],[1]]
# 输出：2
# 解释：

# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m * n <= 2 * 10^5
# 0 <= grid[i][j] <= 1

from typing import List

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        for i in range(m >> 1):
            for j in range(n >> 1):
                cnt = grid[i][j] + grid[i][n-j-1] + grid[m-i-1][j] + grid[m-i-1][n-j-1]
                res += min(cnt, 4 - cnt)

        diff = 0 # 统计奇数列和奇数行有几处不对称
        ones = 0 # 统计奇数列和奇数行对称且为1的个数
        # 如果m为奇数
        if m & 1:
            mid = m >> 1
            for j in range(n >> 1):
                if grid[mid][j] == grid[mid][n-j-1]:
                    ones += grid[mid][j]
                else:
                    diff += 1
        # 如果n为奇数
        if n & 1:
            mid = n >> 1
            for i in range(m >> 1):
                if grid[i][mid] == grid[m-i-1][mid]:
                    ones += grid[i][mid]
                else:
                    diff += 1

            if m & 1:
                res += grid[m >> 1][mid]
        
        # diff 一定是要改的，改成0还是改成1就要ones的情况
        res += diff
        # 假如diff为0，而ones为奇数，那么需要把两个1改成0
        if ones & 1 and diff == 0:
            res += 2
        return res

        
if __name__ == "__main__":
    solution = Solution()
    print(solution.minFlips([[0],[1],[1],[1],[1]])) # 2
    print(solution.minFlips([[1],[1],[1]])) # 3
    print(solution.minFlips([[1],[1],[1],[0]])) # 1
    print(solution.minFlips([[1,0,0],[0,1,0],[0,0,1]])) # 3
    print(solution.minFlips([[0,1],[0,1],[0,0]])) # 2
    print(solution.minFlips([[1],[1]])) # 2
