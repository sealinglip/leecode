#
# @lc app=leetcode.cn id=1695 lang=python3
#
# [1695] 删除子数组的最大得分
#
# https://leetcode.cn/problems/maximum-erasure-value/description/
#
# algorithms
# Medium (59.97%)
# Likes:    122
# Dislikes: 0
# Total Accepted:    37.8K
# Total Submissions: 60.4K
# Testcase Example:  '[4,2,4,5,6]'
#
# 给你一个正整数数组 nums ，请你从中删除一个含有 若干不同元素 的子数组。删除子数组的 得分 就是子数组各元素之 和 。
# 返回 只删除一个 子数组可获得的 最大得分 。
# 如果数组 b 是数组 a 的一个连续子序列，即如果它等于 a[l],a[l+1],...,a[r] ，那么它就是 a 的一个子数组。
# 
# 
# 示例 1：
# 输入：nums = [4,2,4,5,6]
# 输出：17
# 解释：最优子数组是 [2,4,5,6]
# 
# 示例 2：
# 输入：nums = [5,2,1,2,5,2,1,2,5]
# 输出：8
# 解释：最优子数组是 [5,2,1] 或 [1,2,5]
# 
# 
# 提示：
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
# 
#

from collections import Counter
from typing import List
# @lc code=start
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # 题目绕来绕去说半天就是要求nums的最大连续子序列，其中不能包含重复数据
        # 可以通过双指针来解决
        res = curSum = l = r = 0
        n = len(nums)
        subset = set()
        while r < n:
            if nums[r] in subset:
                while nums[l] != nums[r]:
                    subset.remove(nums[l])
                    curSum -= nums[l]
                    l += 1
                l += 1
            else:
                subset.add(nums[r])
                curSum += nums[r]
            r += 1
            res = max(res, curSum)
        
        return res
        
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumUniqueSubarray([4,2,4,5,6])) # 17
    print(solution.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5])) # 8
