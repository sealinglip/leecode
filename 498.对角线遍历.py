#
# @lc app=leetcode.cn id=498 lang=python3
#
# [498] 对角线遍历
#
# 给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。


# 示例 1：
# 输入：mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 输出：[1, 2, 4, 7, 5, 3, 6, 8, 9]

# 示例 2：
# 输入：mat = [[1, 2], [3, 4]]
# 输出：[1, 2, 3, 4]


# 提示：
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# -10^5 <= mat[i][j] <= 10^5

from typing import List
# @lc code=start


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # 先得到矩阵维度大小
        m, n = len(mat), len(mat[0])
        # 起点
        pt = (0, 0)
        # 方向，True代表向右上，False代表向左下
        dir = True
        res = []
        while pt != (m-1, n-1):
            res.append(mat[pt[0]][pt[1]])
            if dir:
                r, c = pt[0]-1, pt[1]+1
                if r < 0:
                    r, c = (0, c) if c < n else (1, c-1)
                    dir = False
                elif c >= n:
                    r, c = r + 2, n-1
                    dir = False
            else:
                r, c = pt[0]+1, pt[1]-1
                if c < 0:
                    r, c = (r, 0) if r < m else (r-1, 1)
                    dir = True
                elif r >= m:
                    r, c = m-1, c + 2
                    dir = True
            pt = (r, c)

        res.append(mat[m-1][n-1])
        return res
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    # [1, 2, 4, 7, 5, 3, 6, 8, 9]
    print(solution.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(solution.findDiagonalOrder([[1, 2], [3, 4]]))  # [1, 2, 3, 4]
