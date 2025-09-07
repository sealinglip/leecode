#
# @lc app=leetcode.cn id=3446 lang=python3
#
# [3446] 按对角线进行矩阵排序
#
# https://leetcode.cn/problems/sort-matrix-by-diagonals/description/
#
# algorithms
# Medium (79.38%)
# Likes:    16
# Dislikes: 0
# Total Accepted:    8K
# Total Submissions: 9.4K
# Testcase Example:  '[[1,7,3],[9,8,2],[4,5,6]]'
#
# 给你一个大小为 n x n 的整数方阵 grid。返回一个经过如下调整的矩阵：
# 
# 左下角三角形（包括中间对角线）的对角线按 非递增顺序 排序。
# 右上角三角形 的对角线按 非递减顺序 排序。
# 
# 
# 示例 1：
# 输入： grid = [[1,7,3],[9,8,2],[4,5,6]]
# 输出： [[8,2,3],[9,6,7],[4,5,1]]
# 解释：
# 标有黑色箭头的对角线（左下角三角形）应按非递增顺序排序：
# [1, 8, 6] 变为 [8, 6, 1]。
# [9, 5] 和 [4] 保持不变。
# 标有蓝色箭头的对角线（右上角三角形）应按非递减顺序排序：
# [7, 2] 变为 [2, 7]。
# [3] 保持不变。
# 
# 示例 2：
# 输入： grid = [[0,1],[1,2]]
# 输出： [[2,1],[1,0]]
# 解释：
# 标有黑色箭头的对角线必须按非递增顺序排序，因此 [0, 2] 变为 [2, 0]。其他对角线已经符合要求。
# 
# 示例 3：
# 输入： grid = [[1]]
# 输出： [[1]]
# 解释：
# 只有一个元素的对角线已经符合要求，因此无需修改。
# 
# 
# 提示：
# grid.length == grid[i].length == n
# 1 <= n <= 10
# -10^5 <= grid[i][j] <= 10^5
# 
# 
#

from typing import List
# @lc code=start
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        for i in range(n):
            diag = [grid[i+j][j] for j in range(n-i)]
            diag.sort(reverse=True)
            for j in range(n-i):
                grid[i+j][j] = diag[j]
        
        for i in range(1, n):
            diag = [grid[j][i+j] for j in range(n-i)]
            diag.sort()
            for j in range(n-i):
                grid[j][i+j] = diag[j]

        return grid
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.sortMatrix([[1,7,3],[9,8,2],[4,5,6]])) # [[8,2,3],[9,6,7],[4,5,1]]
    print(solution.sortMatrix([[0,1],[1,2]])) # [[2,1],[1,0]]
    print(solution.sortMatrix([[1]])) # [[1]]
