# 给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。


# 上面是由数组[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。 感谢 Marcos 贡献此图。

# 示例:

# 输入: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# 输出: 6


# 来源：力扣（LeetCode）
# 链接：https: // leetcode-cn.com/problems/volume-of-histogram-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        # 遍历，总是保存到当前位置的前最高点和位置，以及累计的装水
        # 由两侧往中间走，直到相遇，相遇之后，取边界较低的一侧，前行至较高的一侧
        leftHighest, leftPos, rightHighest, rightPos, totalAccum, currLeftAccum, currRightAccum = \
            height[0], 0, height[-1], len(height) - 1, 0, 0, 0
        l, r = leftPos + 1, rightPos - 1
        while l < r:
            if height[l] >= leftHighest:
                leftHighest = height[l]
                leftPos = l
                totalAccum += currLeftAccum
                currLeftAccum = 0
            else:
                currLeftAccum += leftHighest - height[l]
            l += 1
            if height[r] >= rightHighest:
                rightHighest = height[r]
                rightPos = r
                totalAccum += currRightAccum
                currRightAccum = 0
            else:
                currRightAccum += rightHighest - height[r]
            r -= 1

        if l == r and height[l] >= leftHighest and height[l] >= rightHighest:  # 相遇到一个更高点（比两侧都高）
            totalAccum += currLeftAccum + currRightAccum
        elif leftHighest > rightHighest:  # 右边继续往左边推
            while r > leftPos:
                if height[r] >= rightHighest:
                    rightHighest = height[r]
                    rightPos = r
                    totalAccum += currRightAccum
                    currRightAccum = 0
                else:
                    currRightAccum += rightHighest - height[r]
                r -= 1
            totalAccum += currRightAccum
        else:  # 左边往右边推
            while l < rightPos:
                if height[l] >= leftHighest:
                    leftHighest = height[l]
                    leftPos = l
                    totalAccum += currLeftAccum
                    currLeftAccum = 0
                else:
                    currLeftAccum += leftHighest - height[l]
                l += 1
            totalAccum += currLeftAccum

        return totalAccum
