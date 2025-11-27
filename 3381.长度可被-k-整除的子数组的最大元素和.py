#
# @lc app=leetcode.cn id=3381 lang=python3
#
# [3381] 长度可被 K 整除的子数组的最大元素和
#
# https://leetcode.cn/problems/maximum-subarray-sum-with-length-divisible-by-k/description/
#
# algorithms
# Medium (32.34%)
# Likes:    33
# Dislikes: 0
# Total Accepted:    8.8K
# Total Submissions: 20.6K
# Testcase Example:  '[1,2]\n1'
#
# 给你一个整数数组 nums 和一个整数 k 。
# 
# 返回 nums 中一个 非空子数组 的 最大 和，要求该子数组的长度可以 被 k 整除。
# 
# 
# 示例 1：
# 输入： nums = [1,2], k = 1
# 输出： 3
# 解释：
# 子数组 [1, 2] 的和为 3，其长度为 2，可以被 1 整除。
# 
# 示例 2：
# 输入： nums = [-1,-2,-3,-4,-5], k = 4
# 输出： -10
# 解释：
# 满足题意且和最大的子数组是 [-1, -2, -3, -4]，其长度为 4，可以被 4 整除。
# 
# 示例 3：
# 输入： nums = [-5,1,2,-3,4], k = 2
# 输出： 4
# 解释：
# 满足题意且和最大的子数组是 [1, 2, -3, 4]，其长度为 4，可以被 2 整除。
# 
# 
# 提示：
# 
# 
# 1 <= k <= nums.length <= 2 * 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 复习
#

from math import inf
from typing import List
# @lc code=start
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preSum = 0
        res = -inf
        kSum = [inf] * k
        kSum[k-1] = 0
        
        for i in range(n):
            r = i % k
            preSum += nums[i]
            res = max(res, preSum - kSum[r])
            kSum[r] = min(kSum[r], preSum)

        return res

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubarraySum([1,2], 1)) # 3
    print(solution.maxSubarraySum([-1,-2,-3,-4,-5], 4)) # -10
    print(solution.maxSubarraySum([-5,1,2,-3,4], 2)) # 4
