#
# @lc app=leetcode.cn id=2594 lang=python3
#
# [2594] 修车的最少时间
#
# 给你一个整数数组 ranks ，表示一些机械工的 能力值 。ranksi 是第 i 位机械工的能力值。能力值为 r 的机械工可以在 r * n2 分钟内修好 n 辆车。

# 同时给你一个整数 cars ，表示总共需要修理的汽车数目。

# 请你返回修理所有汽车 最少 需要多少时间。

# 注意：所有机械工可以同时修理汽车。


# 示例 1：
# 输入：ranks = [4, 2, 3, 1], cars = 10
# 输出：16
# 解释：
# - 第一位机械工修 2 辆车，需要 4 * 2 * 2 = 16 分钟。
# - 第二位机械工修 2 辆车，需要 2 * 2 * 2 = 8 分钟。
# - 第三位机械工修 2 辆车，需要 3 * 2 * 2 = 12 分钟。
# - 第四位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。
# 16 分钟是修理完所有车需要的最少时间。

# 示例 2：
# 输入：ranks = [5, 1, 8], cars = 6
# 输出：16
# 解释：
# - 第一位机械工修 1 辆车，需要 5 * 1 * 1 = 5 分钟。
# - 第二位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。
# - 第三位机械工修 1 辆车，需要 8 * 1 * 1 = 8 分钟。
# 16 分钟时修理完所有车需要的最少时间。

# 提示：
# 1 <= ranks.length <= 10^5
# 1 <= ranks[i] <= 100
# 1 <= cars <= 10^6

# 复习

from math import sqrt
from typing import List
# @lc code=start


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks.sort()  # 排序

        def canFinish(t: int) -> bool:
            """
            判断在时间t之内能否修完
            """
            total = 0
            for r in ranks:
                # 时间t 足够 r 修
                total += int(sqrt(t / r))
                if total >= cars:
                    return True
            return False

        # 在可能的时间区间内二分查找，[0, ranks[-1] * cars * cars]
        l, r = 0, ranks[-1] * cars * cars
        while l < r:
            m = (l + r) >> 1
            if canFinish(m):
                r = m
            else:
                l = m + 1
        return l
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.repairCars([4, 2, 3, 1], 10))  # 16
    print(solution.repairCars([5, 1, 8], 6))  # 16
