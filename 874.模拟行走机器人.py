#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#
# 机器人在一个无限大小的 XY 网格平面上行走，从点(0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令 commands ：

# -2 ：向左转 90 度
# -1 ：向右转 90 度
# 1 <= x <= 9 ：向前移动 x 个单位长度
# 在网格上有一些格子被视为障碍物 obstacles 。第 i 个障碍物位于网格点  obstacles[i] = (xi, yi) 。

# 机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续尝试进行该路线的其余部分。

# 返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。（即，如果距离为 5 ，则返回 25 ）


# 注意：

# 北表示 + Y 方向。
# 东表示 + X 方向。
# 南表示 - Y 方向。
# 西表示 - X 方向。


# 示例 1：
# 输入：commands = [4, -1, 3], obstacles = []
# 输出：25
# 解释：
# 机器人开始位于(0, 0)：
# 1. 向北移动 4 个单位，到达(0, 4)
# 2. 右转
# 3. 向东移动 3 个单位，到达(3, 4)
# 距离原点最远的是(3, 4) ，距离为 32 + 42 = 25

# 示例 2：
# 输入：commands = [4, -1, 4, -2, 4], obstacles = [[2, 4]]
# 输出：65
# 解释：机器人开始位于(0, 0)：
# 1. 向北移动 4 个单位，到达(0, 4)
# 2. 右转
# 3. 向东移动 1 个单位，然后被位于(2, 4) 的障碍物阻挡，机器人停在(1, 4)
# 4. 左转
# 5. 向北走 4 个单位，到达(1, 8)
# 距离原点最远的是(1, 8) ，距离为 12 + 82 = 65


# 提示：
# 1 <= commands.length <= 10^4
# commands[i] is one of the values in the list[-2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9].
# 0 <= obstacles.length <= 10^4
# -3 * 10^4 <= xi, yi <= 3 * 10^4
# 答案保证小于 2^31

from typing import List

# @lc code=start
from sortedcontainers import SortedList


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 预处理障碍物
        obstacles.sort()
        x_map = {}
        y_map = {}
        for ox, oy in obstacles:
            if ox not in x_map:
                x_map[ox] = SortedList()
            x_map[ox].add(oy)
            if oy not in y_map:
                y_map[oy] = SortedList()
            y_map[oy].add(ox)

        def move(x: int, y: int, dir: int, step: int) -> int:
            """
            返回在某方向能移动几步
            """
            ob_map = x_map.get(x, None) if (
                dir & 1 == 0) else y_map.get(y, None)
            cur = y if (dir & 1 == 0) else x
            if ob_map is None:  # 没有障碍
                return step if dir < 2 else -step
            else:
                ptr = ob_map.bisect_left(cur)
                # 就站在障碍物上——只有初始才可能
                if ptr < len(ob_map) and ob_map[ptr] == cur and dir < 2:
                    ptr += 1
                # cur 一定为与 ptr - 1 和 ptr之间
                if dir < 2:
                    if ptr == len(ob_map) or ob_map[ptr] - cur > step:
                        return step
                    else:
                        return ob_map[ptr] - cur - 1
                else:
                    if ptr == 0 or cur - ob_map[ptr - 1] > step:
                        return -step
                    else:
                        return -(cur - ob_map[ptr - 1] - 1)

        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = 0
        dir = 0  # 初始在原点，向北

        res = 0
        # 模拟求解
        for c in commands:
            if c == -1:
                dir = (dir + 1) % 4
            elif c == -2:
                dir = (dir + 3) % 4
            else:
                # 向前走
                if dir & 1:
                    x += move(x, y, dir, c)
                else:
                    y += move(x, y, dir, c)
                res = max(res, (x ** 2) + (y ** 2))

        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    # 竟然会有人一开始就在障碍物上待着的情况
    print(solution.robotSim([2, 2, 5, -1, -1], [[-3, 5], [-2, 5], [3, 2],
          [5, 0], [-2, 0], [-1, 5], [5, -3], [0, 0], [-4, 4], [-3, 4]]))  # 81
    print(solution.robotSim([7, -2, -2, 7, 5], [[-3, 2], [-2, 1], [0, 1],
          [-2, 4], [-1, 0], [-2, -3], [0, -3], [4, 4], [-3, 3], [2, 2]]))  # 4
    print(solution.robotSim([6, -1, -1, 6], []))  # 36
    print(solution.robotSim([4, -1, 3], []))  # 25
    print(solution.robotSim([4, -1, 4, -2, 4], [[2, 4]]))  # 65
