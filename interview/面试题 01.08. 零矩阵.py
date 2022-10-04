# 编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。

# 示例 1：
# 输入：
# [
#     [1, 1, 1],
#     [1, 0, 1],
#     [1, 1, 1]
# ]
# 输出：
# [
#     [1, 0, 1],
#     [0, 0, 0],
#     [1, 0, 1]
# ]

# 示例 2：
# 输入：
# [
#     [0, 1, 2, 0],
#     [3, 4, 5, 2],
#     [1, 3, 1, 5]
# ]
# 输出：
# [
#     [0, 0, 0, 0],
#     [0, 4, 5, 0],
#     [0, 3, 1, 0]
# ]

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M, N = len(matrix), len(matrix[0])

        flagC0 = False  # 记录第1列是否包含0
        for i in range(M):
            if matrix[i][0] == 0:
                flagC0 = True
            for j in range(1, N):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(M - 1, -1, -1):
            for j in range(1, N):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if flagC0:
                matrix[i][0] = 0
