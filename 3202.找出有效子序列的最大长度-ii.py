#
# @lc app=leetcode.cn id=3202 lang=python3
#
# [3202] 找出有效子序列的最大长度 II
#
# https://leetcode.cn/problems/find-the-maximum-length-of-valid-subsequence-ii/description/
#
# algorithms
# Medium (45.61%)
# Likes:    26
# Dislikes: 0
# Total Accepted:    9.8K
# Total Submissions: 17.4K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个整数数组 nums 和一个 正 整数 k 。
# nums 的一个 子序列 sub 的长度为 x ，如果其满足以下条件，则称其为 有效子序列 ：
# 
# (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x
# - 1]) % k
# 返回 nums 的 最长有效子序列 的长度。
# 
# 
# 示例 1：
# 输入：nums = [1,2,3,4,5], k = 2
# 输出：5
# 解释：
# 最长有效子序列是 [1, 2, 3, 4, 5] 。
# 
# 示例 2：
# 输入：nums = [1,4,2,3,1,4], k = 3
# 输出：4
# 解释：
# 最长有效子序列是 [1, 4, 1, 4] 。
# 
# 
# 提示：
# 2 <= nums.length <= 10^3
# 1 <= nums[i] <= 10^7
# 1 <= k <= 10^3
# 
# 复习
#

from typing import List
# @lc code=start
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # 对k同余的两个序列
        # 预处理
        nums = [num % k for num in nums]
        res = 0
        for i in range(k): # 相邻两数和的余数为i的情况
            dp = [0] * k
            for num in nums:
                dp[num] = dp[(i + k - num) % k] + 1
            res = max(res, max(dp))
        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumLength([1,2,3,4,5], 2)) # 5
    print(solution.maximumLength([1,4,2,3,1,4], 3)) # 4
