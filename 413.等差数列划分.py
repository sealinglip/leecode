#
# @lc app=leetcode.cn id=413 lang=python3
#
# [413] 等差数列划分
#
# 如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。
# 例如，[1, 3, 5, 7, 9]、[7, 7, 7, 7] 和[3, -1, -5, -9] 都是等差数列。
# 给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。
# 子数组 是数组中的一个连续序列。

# 示例 1：
# 输入：nums = [1, 2, 3, 4]
# 输出：3
# 解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和[1, 2, 3, 4] 自身。

# 示例 2：
# 输入：nums = [1]
# 输出：0

# 提示：
# 1 <= nums.length <= 5000
# -1000 <= nums[i] <= 1000

from typing import List
# @lc code=start


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 3:
            return 0

        delta, cnt = nums[1] - nums[0], 2

        total = 0
        for i in range(2, N):
            if nums[i] - nums[i - 1] == delta:
                cnt += 1
            else:
                # 如果共有cnt个数组成等差数据（cnt >= 3)
                # 则可以组成(cnt - 1)(cnt - 2) / 2 个等差数列
                if cnt >= 3:
                    total += ((cnt - 1)*(cnt - 2)) >> 1
                delta, cnt = nums[i] - nums[i - 1], 2
        if cnt >= 3:
            total += ((cnt - 1)*(cnt - 2)) >> 1
        return total


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfArithmeticSlices([1, 2, 3, 4]))
    print(solution.numberOfArithmeticSlices([1]))
    print(solution.numberOfArithmeticSlices(
        [1, 2, 3, 4, 5, 7, 9, 11, 15, 19, 23]))
