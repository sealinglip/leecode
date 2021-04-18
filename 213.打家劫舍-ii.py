#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
# 同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。

# 示例 1：
# 输入：nums = [2, 3, 2]
# 输出：3
# 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

# 示例 2：
# 输入：nums = [1, 2, 3, 1]
# 输出：4
# 解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
# 偷窃到的最高金额 = 1 + 3 = 4 。

# 示例 3：
# 输入：nums = [0]
# 输出：0

# 提示：
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000

from typing import List
# @lc code=start


class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 4:
            return max(nums)
        # 动态规划

        def robMax(arr: List[int]) -> int:
            # 不考虑首尾相接的限制的话
            # 定义dp[i] 为选中arr[:i]能选出的最大值
            # dp[i] = max(dp[i - 1], arr[i - 1] + dp[i - 2]) if i > 2
            # dp[i] = 0 if i == 0
            # dp[i] = max(dp[i - 1], arr[i - 1]) if i == 1
            pre, cur = 0, 0
            for n in arr:
                pre, cur = cur, max(cur, n + pre)
            return cur

        # 考虑首尾相连
        # 最大值为robMax(nums[1:])和robMax(nums[:N-1])的最大值
        return max(robMax(nums[1:]), robMax(nums[:-1]))


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.rob([2, 3, 2]))
    print(solution.rob([1, 2, 3, 1]))
    print(solution.rob([0]))
