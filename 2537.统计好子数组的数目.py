#
# @lc app=leetcode.cn id=2537 lang=python3
#
# [2537] 统计好子数组的数目
#
# https://leetcode.cn/problems/count-the-number-of-good-subarrays/description/
#
# algorithms
# Medium (56.55%)
# Likes:    92
# Dislikes: 0
# Total Accepted:    18.5K
# Total Submissions: 29.8K
# Testcase Example:  '[1,1,1,1,1]\n10'
#
# 给你一个整数数组 nums 和一个整数 k ，请你返回 nums 中 好 子数组的数目。
# 一个子数组 arr 如果有 至少 k 对下标 (i, j) 满足 i < j 且 arr[i] == arr[j] ，那么称它是一个 好 子数组。
# 子数组 是原数组中一段连续 非空 的元素序列。
# 
# 
# 示例 1：
# 
# 输入：nums = [1,1,1,1,1], k = 10
# 输出：1
# 解释：唯一的好子数组是这个数组本身。
# 
# 
# 示例 2：
# 
# 输入：nums = [3,1,4,3,2,2,4], k = 2
# 输出：4
# 解释：总共有 4 个不同的好子数组：
# - [3,1,4,3,2,2] 有 2 对。
# - [3,1,4,3,2,2,4] 有 3 对。
# - [1,4,3,2,2,4] 有 2 对。
# - [4,3,2,2,4] 有 2 对。
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i], k <= 10^9
# 
# 

from collections import defaultdict
from typing import List

# @lc code=start
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = r = goods = res = 0 # 左边界（包含），右边界（不含），好子数组数量，结果 均初始化为0
        stat = defaultdict(int)
        # 遍历每个子数组的左边界l，求满足好子数组条件的最小右边界r，这样可以求出对于每个l，好子数组数量为n-r+1
        for l in range(n):
            while goods < k and r < n:
                goods += stat[nums[r]]
                stat[nums[r]] += 1
                r += 1
            if goods >= k:
                res += n - r + 1
            stat[nums[l]] -= 1
            goods -= stat[nums[l]]
            if r == n and goods < k:
                break    

        return res

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countGood([2,3,3,3,3,1,3,1,3,2], 19)) # 0
    print(solution.countGood([1,1,1,1,1], 10)) # 1
    print(solution.countGood([3,1,4,3,2,2,4], 2)) # 4

