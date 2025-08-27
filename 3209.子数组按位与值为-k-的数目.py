#
# @lc app=leetcode.cn id=3209 lang=python3
#
# [3209] 子数组按位与值为 K 的数目
#
# https://leetcode.cn/problems/number-of-subarrays-with-and-value-of-k/description/
#
# algorithms
# Hard (34.80%)
# Likes:    14
# Dislikes: 0
# Total Accepted:    3.3K
# Total Submissions: 9.4K
# Testcase Example:  '[1,1,1]\n1'
#
# 给你一个整数数组 nums 和一个整数 k ，请你返回 nums 中有多少个子数组(数组中连续的非空序列)满足：子数组中所有元素按位 AND 的结果为 k 。
# 
# 
# 示例 1：
# 输入：nums = [1,1,1], k = 1
# 输出：6
# 解释：
# 所有子数组都只含有元素 1 。
# 
# 示例 2：
# 输入：nums = [1,1,2], k = 1
# 输出：3
# 解释：
# 按位 AND 值为 1 的子数组包括：[1,1,2], [1,1,2], [1,1,2] 。
# 
# 示例 3：
# 输入：nums = [1,2,3], k = 2
# 输出：2
# 解释：
# 按位 AND 值为 2 的子数组包括：[1,2,3], [1,2,3] 。
# 
# 
# 提示：
# 1 <= nums.length <= 10^5
# 0 <= nums[i], k <= 10^9
# 
# 复习
#

from collections import defaultdict
from typing import List
# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # # 方法1：记忆化搜索
        # n = len(nums)
        # # 记dp[i]为以i为子数组右边界（包含）时，所有可能的子数组，其AND值的计数
        # dp = [defaultdict(int) for _ in range(n)]
        # dp[0][nums[0]] = 1
        # for i in range(1, n):
        #     dp[i][nums[i]] = 1
        #     for v in dp[i-1]:
        #         dp[i][v & nums[i]] += dp[i-1][v]

        # return sum(d[k] for d in dp)

        # 方法2：滑动窗口
        res = l = r = 0
        for i, x in enumerate(nums):
            for j in range(i-1, -1, -1):
                if nums[j] & x == nums[j]:
                    break
                nums[j] &= x

            while l <= i and nums[l] < k:
                l += 1
            while r <= i and nums[r] <= k:
                r += 1
            res += r - l
        return res        
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countSubarrays([1,1,1], 1)) # 6
    print(solution.countSubarrays([1,1,2], 1)) # 3
    print(solution.countSubarrays([1,2,3], 2)) # 2