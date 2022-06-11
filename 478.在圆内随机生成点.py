#
# @lc app=leetcode.cn id=478 lang=python3
#
# [478] 在圆内随机生成点
#
# 给定圆的半径和圆心的位置，实现函数 randPoint ，在圆中产生均匀随机点。

# 实现 Solution 类:

# Solution(double radius, double x_center, double y_center) 用圆的半径 radius 和圆心的位置(x_center, y_center) 初始化对象
# randPoint() 返回圆内的一个随机点。圆周上的一点被认为在圆内。答案作为数组返回[x, y] 。


# 示例 1：
# 输入:
# ["Solution", "randPoint", "randPoint", "randPoint"]
# [[1.0, 0.0, 0.0], [], [], []]
# 输出: [null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]
# 解释:
# Solution solution = new Solution(1.0, 0.0, 0.0)
# solution.randPoint()
# //返回[-0.02493，- 0.38077]
# solution.randPoint()
# //返回[0.82314, 0.38945]
# solution.randPoint()
# //返回[0.36572, 0.17248]


# 提示：
# 0 < radius <= 10^8
# -10^7 <= x_center, y_center <= 10^7
# randPoint 最多被调用 3 * 10^4 次

from typing import List
# @lc code=start
import random
from math import sqrt, sin, cos, pi


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        r = sqrt(random.random()) * self.radius
        angle = random.random() * pi * 2
        return [self.x_center + r * cos(angle), self.y_center + r * sin(angle)]


        # Your Solution object will be instantiated and called as such:
        # obj = Solution(radius, x_center, y_center)
        # param_1 = obj.randPoint()
        # @lc code=end
if __name__ == "__main__":
    solution = Solution(1.0, 0.0, 0.0)
    print(solution.randPoint())
    print(solution.randPoint())
    print(solution.randPoint())
