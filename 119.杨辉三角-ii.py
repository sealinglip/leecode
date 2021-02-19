#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
# 在杨辉三角中，每个数是它左上方和右上方的数的和。

# 示例:
# 输入: 3
# 输出: [1, 3, 3, 1]
# 进阶：

# 你可以优化你的算法到 O(k) 空间复杂度吗？

from typing import List
# @lc code=start


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex + 1):
            tmp = 1
            for j in range(1, i):
                newVal = row[j] + tmp
                tmp = row[j]
                row[j] = newVal
            row.append(1)

        return row
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.getRow(3))
