#
# @lc app=leetcode.cn id=2809 lang=python3
#
# [2809] 使数组和小于等于 x 的最少时间
#
# 给你两个长度相等下标从 0 开始的整数数组 nums1 和 nums2 。每一秒，对于所有下标 0 <= i < nums1.length ，nums1[i] 的值都增加 nums2[i] 。
# 操作 完成后 ，你可以进行如下操作：

# 选择任一满足 0 <= i < nums1.length 的下标 i ，并使 nums1[i] = 0 。
# 同时给你一个整数 x 。

# 请你返回使 nums1 中所有元素之和 小于等于 x 所需要的 最少 时间，如果无法实现，那么返回 -1 。


# 示例 1：
# 输入：nums1 = [1,2,3], nums2 = [1,2,3], x = 4
# 输出：3
# 解释：
# 第 1 秒，我们对 i = 0 进行操作，得到 nums1 = [0,2+2,3+3] = [0,4,6] 。
# 第 2 秒，我们对 i = 1 进行操作，得到 nums1 = [0+1,0,6+3] = [1,0,9] 。
# 第 3 秒，我们对 i = 2 进行操作，得到 nums1 = [1+1,0+2,0] = [2,2,0] 。
# 现在 nums1 的和为 4 。不存在更少次数的操作，所以我们返回 3 。

# 示例 2：
# 输入：nums1 = [1,2,3], nums2 = [3,3,3], x = 4
# 输出：-1
# 解释：不管如何操作，nums1 的和总是会超过 x 。
 

# 提示：
# 1 <= nums1.length <= 10^3
# 1 <= nums1[i] <= 10^3
# 0 <= nums2[i] <= 10^3
# nums1.length == nums2.length
# 0 <= x <= 10^6

# Hard

from typing import List
# @lc code=start
class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        s1 = sum(nums1)
        if s1 <= x:
            return 0
        
        n = len(nums1)
        # 每个位置最多操作一次——因为多次操作同一位置只会让其他数位增加，没有意义，所以最多n次
        # 先证明调整k次的最优解，一定是按nums2从小到大调整。证明如下：
        # 设按规则调整k次的最优解，对应每次调整索引为x1,x2,…,xk，假设nums2[xi]不是升序，
        # 比如，存在0 <= i < j <= k-1，有nums2[xi] > nums2[xj]，那么第i次和第j次的调整，对总和带来的变化为：
        # sum(nums2) - nums1[xi] - nums2[xi] * xi + sum(nums2) - nums1[xj] - nums2[xj] * xj 
        # 很显然，如果把第i次和第j次调整的索引互换，那么对总和带来的变化更大（减少得更多），与x1,x2,…,xk为最优解矛盾，
        # 所以如果是最优解，那么nums2一定是按升序调整的。
        # 将zip(nums1, nums2) 按nums2 升序排列，按顺序重置——优先重置增长速度慢的位置
        # 记dp(i, j) 为前i个元素进行j次操作，可以减少的最大总值，dp(i, 0) = 0
        # 第i-1个元素，可以选择对它操作或者不操作
        # dp(i, j) = max(dp(i-1, j), dp(i-1, j-1) + nums2[i-1] * i + nums1[i-1])
        # 因为dp(*, j)只依赖dp(*, j-1)，所以可以压缩
        dp = [0] * (n + 1)
        for i, (n2, n1) in enumerate(sorted(zip(nums2, nums1)), 1):
            for j in range(i, 0, -1):
                # dp[j]保存的是调整j次，可以减少的最大总值
                dp[j] = max(dp[j], dp[j-1] + j * n2 + n1)

        s2 = sum(nums2)
        for i in range(0, n+1):
            if s2 * i + s1 - dp[i] <= x:
                return i
        
        return -1
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumTime([1,2,3], [1,2,3], 4)) # 3
    print(solution.minimumTime([1,2,3], [3,3,3], 4)) # -1