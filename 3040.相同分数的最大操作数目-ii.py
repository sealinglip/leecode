#
# @lc app=leetcode.cn id=3040 lang=python3
#
# [3040] 相同分数的最大操作数目 II
#
# 给你一个整数数组 nums ，如果 nums 至少 包含 2 个元素，你可以执行以下操作中的 任意 一个：

# 选择 nums 中最前面两个元素并且删除它们。
# 选择 nums 中最后两个元素并且删除它们。
# 选择 nums 中第一个和最后一个元素并且删除它们。
# 一次操作的 分数 是被删除元素的和。

# 在确保 所有操作分数相同 的前提下，请你求出 最多 能进行多少次操作。

# 请你返回按照上述要求 最多 可以进行的操作次数。


# 示例 1：
# 输入：nums = [3,2,1,2,3,4]
# 输出：3
# 解释：我们执行以下操作：
# - 删除前两个元素，分数为 3 + 2 = 5 ，nums = [1,2,3,4] 。
# - 删除第一个元素和最后一个元素，分数为 1 + 4 = 5 ，nums = [2,3] 。
# - 删除第一个元素和最后一个元素，分数为 2 + 3 = 5 ，nums = [] 。
# 由于 nums 为空，我们无法继续进行任何操作。

# 示例 2：
# 输入：nums = [3,2,6,1,4]
# 输出：2
# 解释：我们执行以下操作：
# - 删除前两个元素，分数为 3 + 2 = 5 ，nums = [6,1,4] 。
# - 删除最后两个元素，分数为 1 + 4 = 5 ，nums = [6] 。
# 至多进行 2 次操作。

# 提示：
# 2 <= nums.length <= 2000
# 1 <= nums[i] <= 1000

from functools import cache
from typing import List
# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        # 第一步最关键，决定了后续的基调（每步操作的分数）
        # 设每步操作分数为k
        # dp(i, span) 为nums[i:i+span]最多可以进行的操作数
        @cache
        def dp(i: int, span: int, k: int) -> int:
            if span < 2:
                return 0
            res = 0
            if nums[i] + nums[i+1] == k:
                res = 1 + dp(i+2, span-2, k)
            if nums[i] + nums[i+span-1] == k:
                res = max(res, 1 + dp(i+1, span-2, k))
            if nums[i+span-2] + nums[i+span-1] == k:
                res = max(res, 1 + dp(i, span-2, k))
            return res
        
        return 1 + max(dp(2, n-2, nums[0] + nums[1]), dp(1, n-2, nums[0] + nums[-1]), 
                       dp(0, n-2, nums[-1] + nums[-2]))

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxOperations([1,1,2,3,2,2,1,3,3])) # 4
    print(solution.maxOperations([3,2,1,2,3,4])) # 3
    print(solution.maxOperations([3,2,6,1,4])) # 2