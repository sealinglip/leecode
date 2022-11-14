#
# @lc app=leetcode.cn id=805 lang=python3
#
# [805] 数组的均值分割
#
# 给定你一个整数数组 nums
# 我们要将 nums 数组中的每个元素移动到 A 数组 或者 B 数组中，使得 A 数组和 B 数组不为空，并且 average(A) == average(B) 。
# 如果可以完成则返回true ， 否则返回 false  。
# 注意：对于数组 arr,  average(arr) 是 arr 的所有元素除以 arr 长度的和。


# 示例 1:
# 输入: nums = [1, 2, 3, 4, 5, 6, 7, 8]
# 输出: true
# 解释: 我们可以将数组分割为[1, 4, 5, 8] 和[2, 3, 6, 7], 他们的平均值都是4.5。

# 示例 2:
# 输入: nums = [3, 1]
# 输出: false


# 提示:
# 1 <= nums.length <= 30
# 0 <= nums[i] <= 10^4

# Hard
# 复习

from typing import List
# @lc code=start


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False
        if n == 2:
            return nums[0] == nums[1]

        s = sum(nums)
        # 要切分成两个平均值相等的子数组，那么子数组的平均值和整个数组平均值是相同的。
        # 问题就转化为是否能找到k个数，使其和为 s * k / n，0 < k < n，实际上因为对称，所以如果存在k，那么一定有 k <= n / 2

        m = n >> 1
        # 首先判断是否存在k，使得 s * k % n == 0
        if all(s * i % n for i in range(1, m + 1)):
            return False

        # 计dp[i][x]表示是否可以从当前已经遍历过的元素中取出i个元素构成x
        # 如果当前遍历到位置j，前j个元素有 dp[i][x] == true，则有 dp[i+1][x+nums[j]] = dp[i][x]
        dp = [set() for _ in range(m + 1)]
        dp[0].add(0)  # 初始边界
        for j, num in enumerate(nums):
            for i in range(min(j+1, m), 0, -1):  # 得倒着来，因为dp[i]依赖dp[i-1]
                for x in dp[i-1]:
                    cur = x + num
                    if cur * n == s * i:
                        return True
                    dp[i].add(cur)

        return False

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.splitArraySameAverage([5, 3, 11, 19, 2]))  # True
    print(solution.splitArraySameAverage([1, 2, 3, 4, 5, 6, 7, 8]))  # True
    print(solution.splitArraySameAverage([3, 1]))  # False
