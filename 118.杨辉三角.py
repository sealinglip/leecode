#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

# 在杨辉三角中，每个数是它左上方和右上方的数的和。

# 示例:
# 输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

from typing import List
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []

        res = [[1]]
        for i in range(numRows - 1):
            res.append([1] + [res[-1][i] + res[-1][i+1] for i in range(len(res[-1]) - 1)] + [1])
        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.generate(5))