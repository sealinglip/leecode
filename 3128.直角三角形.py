#
# @lc app=leetcode.cn id=3128 lang=python3
#
# [3128] 直角三角形
#
# 给你一个二维 boolean 矩阵 grid 。
# 请你返回使用 grid 中的 3 个元素可以构建的 直角三角形 数目，且满足 3 个元素值 都 为 1 。
# 注意：
# 如果 grid 中 3 个元素满足：一个元素与另一个元素在 同一行，同时与第三个元素在 同一列 ，那么这 3 个元素称为一个 直角三角形 。这 3 个元素互相之间不需要相邻。
 
# 示例 1：
# 0	1	0
# 0	1	1
# 0	1	0
# 输入：grid = [[0,1,0],[0,1,1],[0,1,0]]
# 输出：2
# 解释：
# 有 2 个直角三角形。

# 示例 2：
# 1	0	0	0
# 0	1	0	1
# 1	0	0	0
# 输入：grid = [[1,0,0,0],[0,1,0,1],[1,0,0,0]]
# 输出：0
# 解释：
# 没有直角三角形。

# 示例 3：
# 1	0	1
# 1	0	0
# 1	0	0
# 输入：grid = [[1,0,1],[1,0,0],[1,0,0]]
# 输出：2
# 解释：
# 有两个直角三角形。

# 提示：
# 1 <= grid.length <= 1000
# 1 <= grid[i].length <= 1000
# 0 <= grid[i][j] <= 1

from typing import List
# @lc code=start
class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        # 先统计每行、每列 1 的个数
        m, n = len(grid), len(grid[0])
        rows = [0] * m
        cols = [0] * n
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 1:
                    rows[i] += 1
                    cols[j] += 1

        res = 0
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 1:
                    res += (rows[i] - 1) * (cols[j] - 1)
        return res


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfRightTriangles([[0,1,0],[0,1,1],[0,1,0]])) # 2
    print(solution.numberOfRightTriangles([[1,0,0,0],[0,1,0,1],[1,0,0,0]])) # 0
    print(solution.numberOfRightTriangles([[1,0,1],[1,0,0],[1,0,0]])) # 2
