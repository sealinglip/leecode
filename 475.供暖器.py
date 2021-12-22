#
# @lc app=leetcode.cn id=475 lang=python3
#
# [475] 供暖器
#
# 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
# 在加热器的加热半径范围内的每个房屋都可以获得供暖。
# 现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。
# 说明：所有供暖器都遵循你的半径标准，加热的半径也一样。


# 示例 1:
# 输入: houses = [1, 2, 3], heaters = [2]
# 输出: 1
# 解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。

# 示例 2:
# 输入: houses = [1, 2, 3, 4], heaters = [1, 4]
# 输出: 1
# 解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。

# 示例 3：
# 输入：houses = [1, 5], heaters = [2]
# 输出：3


# 提示：
# 1 <= houses.length, heaters.length <= 3 * 10^4
# 1 <= houses[i], heaters[i] <= 10^9


from typing import List
# @lc code=start


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        radius = 0

        M = len(heaters)
        cur = 0
        for h in houses:
            while h > heaters[cur] and cur < M - 1:
                cur += 1
            if cur > 0 and h < heaters[cur]:
                radius = max(min(abs(h - heaters[cur]),
                                 abs(h - heaters[cur-1])), radius)
            else:
                radius = max(abs(h - heaters[cur]), radius)

        return radius

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findRadius([1, 2, 3],  [2]))  # 1
    print(solution.findRadius([1, 2, 3, 4], [1, 4]))  # 1
    print(solution.findRadius([1, 5], [2]))  # 3
