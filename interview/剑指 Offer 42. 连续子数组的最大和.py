# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
# 要求时间复杂度为O(n)。

# 示例1:
# 输入: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# 输出: 6
# 解释: 连续子数组 [4, -1, 2, 1] 的和最大，为 6。
#  
# 提示：
# 1 <= arr.length <= 10 ^ 5
# -100 <= arr[i] <= 100
# 注意：本题与主站 53 题相同：https: // leetcode-cn.com/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        accum, minAccum, maxSubSum = 0, 0, float('-inf')

        for num in nums:
            accum += num
            if accum - minAccum > maxSubSum:
                maxSubSum = accum - minAccum
            if accum < minAccum:
                minAccum = accum

        return maxSubSum


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(solution.maxSubArray([-1]))
