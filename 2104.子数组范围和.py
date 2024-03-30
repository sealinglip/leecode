#
# @lc app=leetcode.cn id=2104 lang=python3
#
# [2104] 子数组范围和
#
# 给你一个整数数组 nums 。nums 中，子数组的 范围 是子数组中最大元素和最小元素的差值。

# 返回 nums 中 所有 子数组范围的 和 。

# 子数组是数组中一个连续 非空 的元素序列。


# 示例 1：
# 输入：nums = [1, 2, 3]
# 输出：4
# 解释：nums 的 6 个子数组如下所示：
# [1]，范围 = 最大 - 最小 = 1 - 1 = 0
# [2]，范围 = 2 - 2 = 0
# [3]，范围 = 3 - 3 = 0
# [1, 2]，范围 = 2 - 1 = 1
# [2, 3]，范围 = 3 - 2 = 1
# [1, 2, 3]，范围 = 3 - 1 = 2
# 所有范围的和是 0 + 0 + 0 + 1 + 1 + 2 = 4

# 示例 2：
# 输入：nums = [1, 3, 3]
# 输出：4
# 解释：nums 的 6 个子数组如下所示：
# [1]，范围 = 最大 - 最小 = 1 - 1 = 0
# [3]，范围 = 3 - 3 = 0
# [3]，范围 = 3 - 3 = 0
# [1, 3]，范围 = 3 - 1 = 2
# [3, 3]，范围 = 3 - 3 = 0
# [1, 3, 3]，范围 = 3 - 1 = 2
# 所有范围的和是 0 + 0 + 0 + 2 + 0 + 2 = 4

# 示例 3：
# 输入：nums = [4, -2, -3, 4, 1]
# 输出：59
# 解释：nums 中所有子数组范围的和是 59


# 提示：
# 1 <= nums.length <= 1000
# -10^9 <= nums[i] <= 10^9


# 进阶：你可以设计一种时间复杂度为 O(n) 的解决方案吗？

import enum
from typing import List
# @lc code=start


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # 单调栈找出每个元素能成为最小值的范围，设nums[i]在nums[j,k]范围内最小，j<=i<=k，则有(i-j+1)*(k-i+1)种子数组范围，其最小值为nums[i]
        # 累计求出所有最小值的和，同理可求出最大值之和，答案为两者之差
        n = len(nums)
        minLeft = [0] * n
        maxLeft = [0] * n
        minStack = []
        maxStack = []
        for i, num in enumerate(nums):
            while minStack and nums[minStack[-1]] > num:
                minStack.pop()
            minLeft[i] = minStack[-1] if minStack else -1
            minStack.append(i)

            while maxStack and nums[maxStack[-1]] <= num:
                maxStack.pop()
            maxLeft[i] = maxStack[-1] if maxStack else -1
            maxStack.append(i)

        minRight = [0] * n
        maxRight = [0] * n
        minStack = []
        maxStack = []
        for i in range(n-1, -1, -1):
            num = nums[i]
            while minStack and nums[minStack[-1]] >= num:
                minStack.pop()
            minRight[i] = minStack[-1] if minStack else n
            minStack.append(i)

            while maxStack and nums[maxStack[-1]] < num:
                maxStack.pop()
            maxRight[i] = maxStack[-1] if maxStack else n
            maxStack.append(i)

        sum = 0
        for i, num in enumerate(nums):
            sum += ((maxRight[i] - i) * (i - maxLeft[i]) -
                    (minRight[i] - i) * (i - minLeft[i])) * num

        return sum

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.subArrayRanges([1, 2, 3]))  # 4
    print(solution.subArrayRanges([1, 3, 3]))  # 4
    print(solution.subArrayRanges([4, -2, -3, 4, 1]))  # 59
