#
# @lc app=leetcode.cn id=1072 lang=python3
#
# [1072] 按列翻转得到最大值等行数
#
# 给定 m x n 矩阵 matrix 。

# 你可以从中选出任意数量的列并翻转其上的 每个 单元格。（即翻转后，单元格的值从 0 变成 1，或者从 1 变为 0 。）

# 返回 经过一些翻转后，行内所有值都相等的最大行数 。
# （Return the maximum number of rows that have all values equal after some number of flips.）


# 示例 1：
# 输入：matrix = [[0, 1], [1, 1]]
# 输出：1
# 解释：不进行翻转，有 1 行所有值都相等。

# 示例 2：
# 输入：matrix = [[0, 1], [1, 0]]
# 输出：2
# 解释：翻转第一列的值之后，这两行都由相等的值组成。

# 示例 3：
# 输入：matrix = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]
# 输出：2
# 解释：翻转前两列的值之后，后两行由相等的值组成。

# 提示：
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] == 0 或 1

from typing import List
# @lc code=start


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        def encodeRow(row: List[int]) -> int:
            '''
            按位编码
            '''
            res = 0
            for c in row:
                res <<= 1
                res |= c
            return res

        def flipEncode(enc: int) -> int:
            n = len(matrix[0])
            res = ~enc
            # 只保留最低的n位
            flag = (1 << n) - 1
            res &= flag
            return res

        count = {}
        for row in matrix:
            enc = encodeRow(row)
            count[enc] = count.get(enc, 0) + 1

        res = 0
        for k, v in count.items():
            res = max(res, v + count.get(flipEncode(k), 0))
        return res


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxEqualRowsAfterFlips([[0, 1], [1, 1]]))  # 1
    print(solution.maxEqualRowsAfterFlips([[0, 1], [1, 0]]))  # 2
    print(solution.maxEqualRowsAfterFlips(
        [[0, 0, 0], [0, 0, 1], [1, 1, 0]]))  # 2
