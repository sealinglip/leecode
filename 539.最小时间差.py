#
# @lc app=leetcode.cn id=539 lang=python3
#
# [539] 最小时间差
#

# 给定一个 24 小时制（小时: 分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。


# 示例 1：
# 输入：timePoints = ["23:59", "00:00"]
# 输出：1

# 示例 2：
# 输入：timePoints = ["00:00", "23:59", "00:00"]
# 输出：0


# 提示：
# 2 <= timePoints <= 2 * 10^4
# timePoints[i] 格式为 "HH:MM"

from typing import List
# @lc code=start


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            return 0

        tp = [int(t[0:2]) * 60 + int(t[3:]) for t in timePoints]
        tp.sort()

        minDiff = 1440
        for i in range(1, len(tp)):
            if (diff := tp[i] - tp[i - 1]) < minDiff:
                minDiff = diff

        if (diff := tp[0] + 1440 - tp[-1]) < minDiff:
            minDiff = diff

        return minDiff

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findMinDifference(["23:59", "00:00"]))  # 1
    print(solution.findMinDifference(["00:00", "23:59", "00:00"]))  # 0
