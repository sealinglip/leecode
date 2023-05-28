#
# @lc app=leetcode.cn id=1330 lang=python3
#
# [1330] 翻转子数组得到最大的数组值
#
# 给你一个整数数组 nums 。「数组值」定义为所有满足 0 <= i < nums.length-1 的 | nums[i]-nums[i+1] | 的和。

# 你可以选择给定数组的任意子数组，并将该子数组翻转。但你只能执行这个操作 一次 。

# 请你找到可行的最大 数组值 。


# 示例 1：
# 输入：nums = [2, 3, 1, 5, 4]
# 输出：10
# 解释：通过翻转子数组[3, 1, 5] ，数组变成[2, 5, 1, 3, 4] ，数组值为 10 。

# 示例 2：
# 输入：nums = [2, 4, 9, 24, 2, 1, 10]
# 输出：68


# 提示：
# 1 <= nums.length <= 3*10 ^ 4
# -10 ^ 5 <= nums[i] <= 10 ^ 5

# 困难

from math import inf
from typing import List
# @lc code=start


class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n - 1):
            res += abs(nums[i+1] - nums[i])

        mx1 = 0
        for i in range(1, n - 1):
            mx1 = max(mx1, abs(nums[0] - nums[i + 1]) -
                      abs(nums[i] - nums[i + 1]))
            mx1 = max(mx1, abs(nums[-1] - nums[i - 1]
                               ) - abs(nums[i] - nums[i - 1]))
        mx2, mn2 = -inf, inf
        for i in range(n - 1):
            x, y = nums[i], nums[i + 1]
            mx2 = max(mx2, min(x, y))
            mn2 = min(mn2, max(x, y))
        return res + max(mx1, 2 * (mx2 - mn2))


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxValueAfterReverse([2, 3, 1, 5, 4]))  # 10
    print(solution.maxValueAfterReverse([2, 4, 9, 24, 2, 1, 10]))  # 68
