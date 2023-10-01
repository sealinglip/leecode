#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#
# 假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

# 给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n
# 朵花？能则返回True，不能则返回False。

# 示例 1:
# 输入: flowerbed = [1, 0, 0, 0, 1], n = 1
# 输出: True

# 示例 2:
# 输入: flowerbed = [1, 0, 0, 0, 1], n = 2
# 输出: False

# 提示：
# 1 <= flowerbed.length <= 2 * 10^4
# flowerbed[i] 为 0 或 1
# flowerbed 中不存在相邻的两朵花
# 0 <= n <= flowerbed.length


from typing import List
# @lc code=start


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not flowerbed:
            return n == 0

        N = len(flowerbed)
        zeros = 0
        res = 0
        for i, f in enumerate(flowerbed):
            if f:
                res += (zeros >> 1) if zeros == i else ((zeros-1) >> 1)
                zeros = 0
            else:
                zeros += 1

        if zeros == N:
            res += (zeros+1) >> 1
        elif zeros > 1:
            res += zeros >> 1

        return res >= n

        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.canPlaceFlowers([0], 1))  # True
    print(solution.canPlaceFlowers([0, 0, 0], 2))  # True
    print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 1))  # True
    print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 2))  # False
    print(solution.canPlaceFlowers([0, 0, 1, 0, 0], 2))  # True
    print(solution.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))  # False
    print(solution.canPlaceFlowers([1, 0, 0, 0, 0, 0, 1], 2))  # True
    print(solution.canPlaceFlowers([0, 0, 1, 0, 0, 0, 1], 2))  # True
