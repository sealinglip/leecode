#
# @lc app=leetcode.cn id=2741 lang=python3
#
# [2741] 特别的排列
#
# 给你一个下标从 0 开始的整数数组 nums ，它包含 n 个 互不相同 的正整数。如果 nums 的一个排列满足以下条件，我们称它是一个特别的排列：

# 对于 0 <= i < n - 1 的下标 i ，要么 nums[i] % nums[i+1] == 0 ，要么 nums[i+1] % nums[i] == 0 。
# 请你返回特别排列的总数目，由于答案可能很大，请将它对 10^9 + 7 取余 后返回。


# 示例 1：
# 输入：nums = [2,3,6]
# 输出：2
# 解释：[3,6,2] 和 [2,6,3] 是 nums 两个特别的排列。

# 示例 2：
# 输入：nums = [1,4,3]
# 输出：2
# 解释：[3,1,4] 和 [4,1,3] 是 nums 两个特别的排列。
 

# 提示：
# 2 <= nums.length <= 14
# 1 <= nums[i] <= 10^9

# 复习

from typing import List
# @lc code=start
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        n = len(nums)
        # 动规
        # 因为数字不多，可以用bit_mask来表示哪些数用了，哪些没用
        # 记dp(mask, i) 为mask表示的子序列，以第i个元素结尾时，总的特别排列数，mask满足 mask & (1<<i) == (1<<i)
        # 有 dp(mask, i) = sum(dp(mask', j) for j in each bit of mask')   mask' = mask & (~(1<<i))
        dp = [[0] * n for _ in range(1<<n)]
        for i in range(n):
            dp[1 << i][i] = 1

        for mask in range(1, 1<<n):
            for i, x in enumerate(nums):
                if mask & (1 << i) == 0:
                    continue
                for j, y in enumerate(nums):
                    if i == j or (mask & (1 << j) == 0):
                        continue
                    if x % y == 0 or y % x == 0:
                        dp[mask][i] = (dp[mask][i] + dp[mask ^ (1 << i)][j]) % MOD
        
        return sum(dp[(1 << n) - 1][i] for i in range(n)) % MOD        


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.specialPerm([2,3,6])) # 2
    print(solution.specialPerm([1,4,3])) # 2