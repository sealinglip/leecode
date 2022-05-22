#
# @lc app=leetcode.cn id=812 lang=python3
#
# [812] 最大三角形面积
#
# 给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。

# 示例:
# 输入: points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
# 输出: 2
# 解释:
# 这五个点如下图所示。组成的橙色三角形是最大的，面积为2。


# 注意:
# 3 <= points.length <= 50.
# 不存在重复的点。
# -50 <= points[i][j] <= 50.
# 结果误差值在 10 ^ -6 以内都认为是正确答案。

# 复习
from itertools import combinations
from typing import List
# @lc code=start


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # 求叉积的最大值
        def cross(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> float:
            a1, b1 = x2 - x1, y2 - y1
            a2, b2 = x3 - x1, y3 - y1
            return abs(a1 * b2 - a2 * b1) / 2  # 叉积除2得到三角形面积

        return max(cross(x1, y1, x2, y2, x3, y3) for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3))


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.largestTriangleArea(
        [[1, 0], [0, 0], [0, 1]]))  # 0.5
    print(solution.largestTriangleArea(
        [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]))  # 2
