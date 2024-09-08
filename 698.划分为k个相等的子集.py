#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#
# 给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。


# 示例 1：
# 输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1, 4），（2, 3），（2, 3）等于总和。

# 示例 2:
# 输入: nums = [1, 2, 3, 4], k = 3
# 输出: false


# 提示：
# 1 <= k <= len(nums) <= 16
# 0 < nums[i] < 10000
# 每个元素的频率在[1, 4] 范围内

# 复习
# 类似于473题
from typing import List
# @lc code=start


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False  # 不能整除
        nums.sort()
        sideLen = total // k
        if nums[-1] > sideLen:
            return False  # 最大的元素不能超过每份大小

        # 考虑要将边长对应nums数组的线段拼接成一个正k边形，放置的方法是：当拼接某个线段后当前边长刚好为sideLen，则拼接后当前边已经拼接完成，开始拼下一条边
        # 如果拼接某个线段后当前边长大于sideLen，则当前方案不合乎要求；如果拼接后长度小于sideLen，那么当前边还得接着拼
        # 因为nums的长度小于等于16，如果用整数从低到高的位i来代表nums[i]是否已经拼接了且合乎要求
        # x的第i位代表第i个数有没有放置
        # 记dp(x) 表示当前放置的边的长度
        # 易知dp(0) = 0：什么都还没放，所以当前边长度为0
        # 如果 x1 &  (1 << k) == 0 (即第k个数还没放)
        # 且 dp(x1) + nums[k] <= quotient，那么
        # 有 dp(x1 | (1 << k)) = (dp(x1) + nums[k]) % sideLen
        # 否则dp(x1 | (1 << k)) = -1 表示状态x | (1 << k)不成立
        # 如果dp((1 << len(nums)) - 1) = 0，表示所有数都放下了，且刚好，则可以拼成正k边形
        # 否则不行
        dp = {}
        dp[0] = 0
        for x in range(1, (1 << len(nums))):
            for k, v in enumerate(nums):
                if x & (1 << k) == 0:
                    continue
                x1 = x & ~(1 << k)  # 这等同于x1 加上第k根火柴为x
                preDp = dp.get(x1, - 1)  # 默认为-1，代表目前还没有dp(x1)的合乎要求的方案（不代表无解，只是当前还没有拼接方案）
                if preDp >= 0 and preDp + v <= sideLen:
                    # 找到一种可行解
                    dp[x] = (preDp + v) % sideLen
                    break

        return dp.get((1 << len(nums)) - 1, -1) == 0


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))  # True
    print(solution.canPartitionKSubsets([1, 2, 3, 4], 3))  # False
