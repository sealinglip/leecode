#
# @lc app=leetcode.cn id=1499 lang=python3
#
# [1499] 满足不等式的最大值
#
# 给你一个数组 points 和一个整数 k 。数组中每个元素都表示二维平面上的点的坐标，并按照横坐标 x 的值从小到大排序。也就是说 points[i] = [xi, yi] ，并且在 1 <= i < j <= points.length 的前提下， xi < xj 总成立。

# 请你找出 yi + yj + |xi - xj | 的 最大值，其中 | xi - xj | <= k 且 1 <= i < j <= points.length。

# 题目测试数据保证至少存在一对能够满足 | xi - xj | <= k 的点。


# 示例 1：
# 输入：points = [[1, 3], [2, 0], [5, 10], [6, -10]], k = 1
# 输出：4
# 解释：前两个点满足 | xi - xj | <= 1 ，代入方程计算，则得到值 3 + 0 + |1 - 2 | = 4 。第三个和第四个点也满足条件，得到值 10 + -10 + |5 - 6 | = 1 。
# 没有其他满足条件的点，所以返回 4 和 1 中最大的那个。

# 示例 2：
# 输入：points = [[0, 0], [3, 0], [9, 2]], k = 3
# 输出：3
# 解释：只有前两个点满足 | xi - xj | <= 3 ，代入方程后得到值 0 + 0 + |0 - 3 | = 3 。


# 提示：
# 2 <= points.length <= 10 ^ 5
# points[i].length == 2
# -10 ^ 8 <= points[i][0], points[i][1] <= 10 ^ 8
# 0 <= k <= 2 * 10 ^ 8
# 对于所有的1 <= i < j <= points.length ，points[i][0] < points[j][0] 都成立。也就是说，xi 是严格递增的。

# Hard
# 复习

from collections import deque
from math import inf
from typing import List
# @lc code=start


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        res = -inf

        # 要求 yi + yj + |xi - xj|，因为对称性，不妨设 j > i
        # max(yi + yj + |xi - xj|) = max(xj - xi + yi + yj) = max(xj + yj) - min(xi - yi)
        # 单调栈：（xi - yi）越小排得越靠前
        queue = deque([(points[0][0], points[0][0] - points[0][1])])
        for i in range(1, len(points)):
            # 超出k范围的点去掉
            while queue and points[i][0] - queue[0][0] > k:
                queue.popleft()

            # 如果queue空了，说明当前点找不到xj - xi <= k 的 i 点
            if queue:
                res = max(res, points[i][0] + points[i][1] - queue[0][1])

            # 入栈
            d = points[i][0] - points[i][1]
            while queue and queue[-1][1] > d:
                queue.pop()
            queue.append((points[i][0], d))

        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxValueOfEquation(
        [[-19, 9], [-15, -19], [-5, -8]], 10))  # -6
    print(solution.findMaxValueOfEquation(
        [[1, 3], [2, 0], [5, 10], [6, -10]], 1))  # 4
    print(solution.findMaxValueOfEquation([[0, 0], [3, 0], [9, 2]], 3))  # 3
