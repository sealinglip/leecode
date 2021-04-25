#
# @lc app=leetcode.cn id=368 lang=python3
#
# [368] 最大整除子集
#
# 给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer，
# 子集中每一元素对(answer[i], answer[j]) 都应当满足：
# answer[i] % answer[j] == 0 ，或
# answer[j] % answer[i] == 0
# 如果存在多个有效解子集，返回其中任何一个均可。

# 示例 1：
# 输入：nums = [1, 2, 3]
# 输出：[1, 2]
# 解释：[1, 3] 也会被视为正确答案。

# 示例 2：
# 输入：nums = [1, 2, 4, 8]
# 输出：[1, 2, 4, 8]

# 提示：
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2 * 10^9
# nums 中的所有整数 互不相同

from typing import List
# @lc code=start


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums

        L = len(nums)
        # 先对数组进行排序
        nums.sort()

        # dp[i] 记录第i个元素能整除的数字列表
        dp = [[i] for i in nums]

        for i in range(1, L):
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[j] + [nums[i]], dp[i], key=len)  # 按数组长度比大小

        return max(dp, key=len)

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.largestDivisibleSubset([1, 2, 3]))
    print(solution.largestDivisibleSubset([1, 2, 4, 8]))
