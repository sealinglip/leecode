#
# @lc app=leetcode.cn id=587 lang=python3
#
# [587] 安装栅栏
#
# 在一个二维的花园中，有一些用(x, y) 坐标表示的树。由于安装费用十分昂贵，你的任务是先用最短的绳子围起所有的树。只有当所有的树都被绳子包围时，花园才能围好栅栏。你需要找到正好位于栅栏边界上的树的坐标。


# 示例 1:
# 输入: [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
# 输出: [[1, 1], [2, 0], [4, 2], [3, 3], [2, 4]]
# 解释:

# 示例 2:
# 输入: [[1, 2], [2, 2], [4, 2]]
# 输出: [[1, 2], [2, 2], [4, 2]]
# 解释:

# 即使树都在一条直线上，你也需要先用绳子包围它们。


# 注意:
# 所有的树应当被围在一起。你不能剪断绳子来包围树或者把树分成一组以上。
# 输入的整数在 0 到 100 之间。
# 花园至少有一棵树。
# 所有树的坐标都是不同的。
# 输入的点没有顺序。输出顺序也没有要求。

# Hard
# 复习
from typing import List
# @lc code=start


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # 二维凸包问题
        def cross(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        n = len(trees)
        if n < 4:
            return trees

        # 按照 x 从小到大排序，如果 x 相同，则按照 y 从小到大排序
        trees.sort()

        hull = [0]  # hull[0] 需要入栈两次，不标记
        used = [False] * n
        # 求凸包的下半部分
        for i in range(1, n):
            while len(hull) > 1 and cross(trees[hull[-2]], trees[hull[-1]], trees[i]) < 0:
                used[hull.pop()] = False
            used[i] = True
            hull.append(i)
        # 求凸包的上半部分
        m = len(hull)
        for i in range(n - 2, -1, -1):
            if not used[i]:
                while len(hull) > m and cross(trees[hull[-2]], trees[hull[-1]], trees[i]) < 0:
                    used[hull.pop()] = False
                used[i] = True
                hull.append(i)
        # hull[0] 同时参与凸包的上半部分检测，因此需去掉重复的 hull[0]
        hull.pop()

        return [trees[i] for i in hull]

        # @lc code=end
