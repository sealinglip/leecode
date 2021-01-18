#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#
# 在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。
# 请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。

# 示例 1：
# 输入：coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
# 输出：true

# 示例 2：
# 输入：coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
# 输出：false

# 提示：
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10 ^ 4 <= coordinates[i][0], coordinates[i][1] <= 10 ^ 4
# coordinates 中不含重复的点

from typing import List
# @lc code=start
from fractions import Fraction


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        N = len(coordinates)
        if N <= 2:
            return True

        f = None if coordinates[1][0] == coordinates[0][0] else Fraction(coordinates[1][1] - coordinates[0][1],
                                                                         coordinates[1][0] - coordinates[0][0])

        for i in range(2, N):
            f2 = None if coordinates[i][0] == coordinates[0][0] else Fraction(coordinates[i][1] - coordinates[0][1],
                                                                              coordinates[i][0] - coordinates[0][0])
            if f != f2:
                return False

        return True


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.checkStraightLine([[0, 0], [0, 1], [0, -1]]
                                     ))
    print(solution.checkStraightLine([[0, 0], [0, 1], [1, -1]]
                                     ))
    print(solution.checkStraightLine(
        [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
    print(solution.checkStraightLine(
        [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
