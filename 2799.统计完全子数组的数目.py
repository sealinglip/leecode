#
# @lc app=leetcode.cn id=2799 lang=python3
#
# [2799] 统计完全子数组的数目
#
# https://leetcode.cn/problems/count-complete-subarrays-in-an-array/description/
#
# algorithms
# Medium (67.22%)
# Likes:    72
# Dislikes: 0
# Total Accepted:    22.4K
# Total Submissions: 31.4K
# Testcase Example:  '[1,3,1,2,2]'
#
# 给你一个由 正 整数组成的数组 nums 。
# 如果数组中的某个子数组满足下述条件，则称之为 完全子数组 ：
# 子数组中 不同 元素的数目等于整个数组不同元素的数目。
# 返回数组中 完全子数组 的数目。
# 子数组 是数组中的一个连续非空序列。
# 
# 
# 示例 1：
# 输入：nums = [1,3,1,2,2]
# 输出：4
# 解释：完全子数组有：[1,3,1,2]、[1,3,1,2,2]、[3,1,2] 和 [3,1,2,2] 。
# 
# 
# 示例 2：
# 输入：nums = [5,5,5,5]
# 输出：10
# 解释：数组仅由整数 5 组成，所以任意子数组都满足完全子数组的条件。子数组的总数为 10 。
# 
# 
# 提示：
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2000
# 

from typing import Counter, List
from math import comb
# @lc code=start
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        res = 0
        cnt = {} # 对不同数字计数
        n = len(nums)
        r = 0 # 滑动窗口右界
        distinct = len(set(nums))
        for l in range(n):
            if l > 0:
                out = nums[l-1]
                cnt[out] -= 1
                if cnt[out] == 0:
                    del cnt[out]
            while r < n and len(cnt) < distinct:
                add = nums[r]
                cnt[add] = cnt.get(add, 0) + 1
                r += 1
            if len(cnt) == distinct:
                res += n - r + 1
        return res

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countCompleteSubarrays([1,3,1,2,2])) # 4
    print(solution.countCompleteSubarrays([5,5,5,5])) # 10
