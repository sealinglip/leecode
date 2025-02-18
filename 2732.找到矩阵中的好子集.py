#
# @lc app=leetcode.cn id=2732 lang=python3
#
# [2732] 找到矩阵中的好子集
#
# 给你一个下标从 0 开始大小为 m x n 的二进制矩阵 grid 。

# 从原矩阵中选出若干行构成一个行的 非空 子集，如果子集中任何一列的和至多为子集大小的一半，那么我们称这个子集是 好子集。

# 更正式的，如果选出来的行子集大小（即行的数量）为 k，那么每一列的和至多为 floor(k / 2) 。

# 请你返回一个整数数组，它包含好子集的行下标，请你将其 升序 返回。

# 如果有多个好子集，你可以返回任意一个。如果没有好子集，请你返回一个空数组。

# 一个矩阵 grid 的行 子集 ，是删除 grid 中某些（也可能不删除）行后，剩余行构成的元素集合。

 
# 示例 1：
# 输入：grid = [[0,1,1,0],[0,0,0,1],[1,1,1,1]]
# 输出：[0,1]
# 解释：我们可以选择第 0 和第 1 行构成一个好子集。
# 选出来的子集大小为 2 。
# - 第 0 列的和为 0 + 0 = 0 ，小于等于子集大小的一半。
# - 第 1 列的和为 1 + 0 = 1 ，小于等于子集大小的一半。
# - 第 2 列的和为 1 + 0 = 1 ，小于等于子集大小的一半。
# - 第 3 列的和为 0 + 1 = 1 ，小于等于子集大小的一半。

# 示例 2：
# 输入：grid = [[0]]
# 输出：[0]
# 解释：我们可以选择第 0 行构成一个好子集。
# 选出来的子集大小为 1 。
# - 第 0 列的和为 0 ，小于等于子集大小的一半。

# 示例 3：
# 输入：grid = [[1,1,1],[1,1,1]]
# 输出：[]
# 解释：没有办法得到一个好子集。
 

# 提示：
# m == grid.length
# n == grid[i].length
# 1 <= m <= 10^4
# 1 <= n <= 5
# grid[i][j] 要么是 0 ，要么是 1 。

# Hard

from typing import List
# @lc code=start
from functools import reduce
class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        # n <= 5 是个关键条件，说明：
        # 如果有好子集，那么一定存在一行或两行组成的好子集
        # 将行传成掩码
        row = [reduce(lambda x, y: (x << 1 | y), r) for r in grid]
        m = len(row)
        for i in range(m):
            if row[i] == 0:
                return [i]
        
        for i in range(m):
            for j in range(i+1, m):
                if row[i] & row[j] == 0:
                    return [i, j]
        
        return []
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.goodSubsetofBinaryMatrix([[0,0,1,0],[1,1,1,1],[0,0,1,0]])) # []
    print(solution.goodSubsetofBinaryMatrix([[0,1,1,0],[1,1,0,1],[0,0,1,0]])) # [1,2]
    print(solution.goodSubsetofBinaryMatrix([[0,1,1,0],[0,0,0,1],[1,1,1,1]])) # [0,1]
    print(solution.goodSubsetofBinaryMatrix([[0]])) # [0]
    print(solution.goodSubsetofBinaryMatrix([[1,1,1],[1,1,1]])) # []