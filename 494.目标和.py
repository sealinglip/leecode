#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#
# 给你一个整数数组 nums 和一个整数 target 。
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

# 示例 1：
# 输入：nums = [1, 1, 1, 1, 1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3

# 示例 2：
# 输入：nums = [1], target = 1
# 输出：1

# 提示：
# 1 <= nums.length <= 20
# 0 <= nums[i] <= 1000
# 0 <= sum(nums[i]) <= 1000
# -1000 <= target <= 100

from typing import List
# @lc code=start


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 方法1：回溯+哈希
        cache = {}
        # 计dp(i, k)为前i个数输出k的方法数
        # 则有dp(i, k) = dp(i - 1, k - nums[i]) + dp(i - 1, k + nums[i])
        # dp(0, k) = 1 if k == 0 else 0

        def dp(i, k):
            if i == -1:
                return 1 if k == 0 else 0
            key = (i, k)
            if key in cache:
                return cache[key]
            else:
                res = dp(i - 1, k - nums[i]) + dp(i - 1, k + nums[i])
                cache[key] = res
                return res

        return dp(len(nums) - 1, target)

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findTargetSumWays([1, 1, 1, 1, 1], 3))
