#
# @lc app=leetcode.cn id=223 lang=python3
#
# [223] 矩形面积
#
# 给你 二维 平面上两个 由直线构成的 矩形，请你计算并返回两个矩形覆盖的总面积。
# 每个矩形由其 左下 顶点和 右上 顶点坐标表示：
# 第一个矩形由其左下顶点(ax1, ay1) 和右上顶点(ax2, ay2) 定义。
# 第二个矩形由其左下顶点(bx1, by1) 和右上顶点(bx2, by2) 定义。


# 示例 1：
# Rectangle Area
# 输入：ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
# 输出：45

# 示例 2：
# 输入：ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
# 输出：16


# 提示：
# -10^4 <= ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 <= 10^4


# @lc code=start
from typing import List


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def area(ax1: int, ay1: int, ax2: int, ay2: int) -> int:
            return (ax2 - ax1) * (ay2 - ay1)

        def overlap(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> List[int]:
            if ((bx1 <= ax1 < bx2) or (bx1 < ax2 <= bx2) or (ax1 <= bx1 < ax2) or (ax1 < bx2 <= ax2)) and \
                    ((by1 <= ay1 < by2) or (by1 < ay2 <= by2) or (ay1 <= by1 < ay2) or (ay1 < by2 <= ay2)):
                return [max(ax1, bx1), max(ay1, by1), min(ax2, bx2), min(ay2, by2)]
            else:
                return None

        # 先分别求两矩形面积
        s = area(ax1, ay1, ax2, ay2) + area(bx1, by1, bx2, by2)
        # 再减掉overlap矩形的面积
        overlapRect = overlap(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
        if (overlapRect):
            s -= area(*overlapRect)

        return s
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.computeArea(-2, -2, 2, 2, -1, -1, 1, 1))  # 16
    print(solution.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))  # 45
    print(solution.computeArea(-2, -2, 2, 2, -2, -2, 2, 2))  # 16
