#
# @lc app=leetcode.cn id=1498 lang=python3
#
# [1498] 满足条件的子序列数目
#
# https://leetcode.cn/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/
#
# algorithms
# Medium (39.43%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    19.3K
# Total Submissions: 44.2K
# Testcase Example:  '[3,5,6,7]\n9'
#
# 给你一个整数数组 nums 和一个整数 target 。
# 请你统计并返回 nums 中能满足其最小元素与最大元素的 和 小于或等于 target 的 非空 子序列的数目。
# 由于答案可能很大，请将结果对 10^9 + 7 取余后返回。
# 
# 
# 示例 1：
# 输入：nums = [3,5,6,7], target = 9
# 输出：4
# 解释：有 4 个子序列满足该条件。
# [3] -> 最小元素 + 最大元素 <= target (3 + 3 <= 9)
# [3,5] -> (3 + 5 <= 9)
# [3,5,6] -> (3 + 6 <= 9)
# [3,6] -> (3 + 6 <= 9)
# 
# 示例 2：
# 输入：nums = [3,3,6,8], target = 10
# 输出：6
# 解释：有 6 个子序列满足该条件。（nums 中可以有重复数字）
# [3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
# 
# 示例 3：
# 输入：nums = [2,3,3,4,6,7], target = 12
# 输出：61
# 解释：共有 63 个非空子序列，其中 2 个不满足条件（[6,7], [7]）
# 有效序列总数为（63 - 2 = 61）
# 
# 
# 提示：
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^6
# 1 <= target <= 10^6
# 
#

from typing import List
# @lc code=start
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        l = 0
        r = len(nums) - 1
        res = 0
        while l <= r:
            while r >= l and nums[l] + nums[r] > target:
                r -= 1
            if r < l:
                break
            # 此时 nums[l:k] (l < k <= r) 在两头都包含的情况下，中间的元素有 2 ^ (k-l-1) 种组合情况
            # 以l为左边界，右边界和左边界不重合的非空子序列共有2^0 + 2^1 + … + 2^(r-l-1)个，再加上左右边界重合到l的一种情况，共2^(r-l)个
            res = (res + (1 << (r-l))) % MOD
            l += 1
        
        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.numSubseq([3,5,6,7], 9)) # 4
    print(solution.numSubseq([3,3,6,8], 10)) # 6
    print(solution.numSubseq([2,3,3,4,6,7], 12)) # 61
