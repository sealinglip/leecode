#
# @lc app=leetcode.cn id=497 lang=python3
#
# [497] 非重叠矩形中的随机点
#
# 给定一个由非重叠的轴对齐矩形的数组 rects ，其中 rects[i] = [ai, bi, xi, yi] 表示(ai, bi) 是第 i 个矩形的左下角点，(xi, yi) 是第 i 个矩形的右上角点。设计一个算法来随机挑选一个被某一矩形覆盖的整数点。矩形周长上的点也算做是被矩形覆盖。所有满足要求的点必须等概率被返回。

# 在给定的矩形覆盖的空间内的任何整数点都有可能被返回。

# 请注意 ，整数点是具有整数坐标的点。

# 实现 Solution 类:

# Solution(int[][] rects) 用给定的矩形数组 rects 初始化对象。
# int[] pick() 返回一个随机的整数点[u, v] 在给定的矩形所覆盖的空间内。


# 示例 1：
# 输入:
# ["Solution", "pick", "pick", "pick", "pick", "pick"]
# [[[[-2, -2, 1, 1], [2, 2, 4, 6]]], [], [], [], [], []]
# 输出:
# [null, [1, -2], [1, -1], [-1, -2], [-2, -2], [0, 0]]
# 解释：
# Solution solution = new Solution([[-2, -2, 1, 1], [2, 2, 4, 6]])
# solution.pick()
# // 返回[1, -2]
# solution.pick()
# // 返回[1, -1]
# solution.pick()
# // 返回[-1, -2]
# solution.pick()
# // 返回[-2, -2]
# solution.pick()
# // 返回[0, 0]


# 提示：
# 1 <= rects.length <= 100
# rects[i].length == 4
# -10^9 <= ai < xi <= 10^9
# -10^9 <= bi < yi <= 10^9
# xi - ai <= 2000
# yi - bi <= 2000
# 所有的矩形不重叠。
# pick 最多被调用 10^4 次。

from tkinter import W
from typing import List
# @lc code=start
from random import randint
from bisect import bisect_left


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.arr = [0]  # 前缀和
        for x1, y1, x2, y2 in rects:
            self.arr.append(self.arr[-1] + (x2 - x1 + 1) * (y2 - y1 + 1))

    def pick(self) -> List[int]:
        w = randint(1, self.arr[-1])
        idx = bisect_left(self.arr, w) - 1
        x1, y1, x2, y2 = self.rects[idx]
        return [x1 + randint(0, x2 - x1), y1 + randint(0, y2 - y1)]

        # Your Solution object will be instantiated and called as such:
        # obj = Solution(rects)
        # param_1 = obj.pick()
        # @lc code=end
