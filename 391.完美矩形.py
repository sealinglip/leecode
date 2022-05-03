#
# @lc app=leetcode.cn id=391 lang=python3
#
# [391] 完美矩形
#
# 给你一个数组 rectangles ，其中 rectangles[i] = [xi, yi, ai, bi] 表示一个坐标轴平行的矩形。这个矩形的左下顶点是(xi, yi) ，右上顶点是(ai, bi) 。

# 如果所有矩形一起精确覆盖了某个矩形区域，则返回 true ；否则，返回 false 。


# 示例 1：
# 输入：rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
# 输出：true
# 解释：5 个矩形一起可以精确地覆盖一个矩形区域。

# 示例 2：
# 输入：rectangles = [[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]]
# 输出：false
# 解释：两个矩形之间有间隔，无法覆盖成一个矩形。

# 示例 3：
# 输入：rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [3, 2, 4, 4]]
# 输出：false
# 解释：图形顶端留有空缺，无法覆盖成一个矩形。

# 示例 4：
# 输入：rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [2, 2, 4, 4]]
# 输出：false
# 解释：因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。


# 提示：
# 1 <= rectangles.length <= 2 * 10^4
# rectangles[i].length == 4
# -10^5 <= xi, yi, ai, bi <= 10^5

# Hard

from typing import List
# @lc code=start
from collections import defaultdict


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # 条件1：所有矩形组成的区域，最左小角和最右上角组成的矩形面积应该等于所有矩形的面积和，不满足的肯定不满足完美矩形的条件
        # 条件2：满足条件1的，未必是完美矩形，满足条件1且矩形列表两两不相交的，才满足。要满足条件2，则所有顶点，除最外侧的点，只能出现一次，其他点，必须出现2次或4次
        # 否则就是有重叠
        LIMIT = 10 ** 5
        left, bottom, top, right = LIMIT, LIMIT, -LIMIT, -LIMIT  # 记录边界
        areaSum = 0
        cnt = defaultdict(int)
        for x, y, a, b in rectangles:
            areaSum += (a - x) * (b - y)
            if x < left:
                left = x
            if y < bottom:
                bottom = y
            if a > right:
                right = a
            if b > top:
                top = b
            cnt[(x, y)] += 1
            cnt[(a, b)] += 1
            cnt[(x, b)] += 1
            cnt[(a, y)] += 1

        if areaSum != (top - bottom) * (right - left) or cnt[(left, bottom)] != 1 or cnt[(left, top)] != 1 or cnt[(right, top)] != 1 or cnt[(right, bottom)] != 1:
            return False

        del cnt[(left, bottom)], cnt[(left, top)], cnt[(
            right, top)], cnt[(right, bottom)]

        return all(c == 2 or c == 4 for c in cnt.values())

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.isRectangleCover(
        [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]))  # True
    print(solution.isRectangleCover(
        [[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]]))  # False
    print(solution.isRectangleCover(
        [[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [3, 2, 4, 4]]))  # False
    print(solution.isRectangleCover(
        [[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [2, 2, 4, 4]]))  # False
