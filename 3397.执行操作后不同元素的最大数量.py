#
# @lc app=leetcode.cn id=3397 lang=python3
#
# [3397] 执行操作后不同元素的最大数量
#
# https://leetcode.cn/problems/maximum-number-of-distinct-elements-after-operations/description/
#
# algorithms
# Medium (36.82%)
# Likes:    28
# Dislikes: 0
# Total Accepted:    11.9K
# Total Submissions: 23.1K
# Testcase Example:  '[1,2,2,3,3,4]\n2'
#
# 给你一个整数数组 nums 和一个整数 k。
# 你可以对数组中的每个元素 最多 执行 一次 以下操作：
# 
# 将一个在范围 [-k, k] 内的整数加到该元素上。
# 返回执行这些操作后，nums 中可能拥有的不同元素的 最大 数量。
# 
# 
# 示例 1：
# 输入： nums = [1,2,2,3,3,4], k = 2
# 输出： 6
# 解释：
# 对前四个元素执行操作，nums 变为 [-1, 0, 1, 2, 3, 4]，可以获得 6 个不同的元素。
# 
# 示例 2：
# 输入： nums = [4,4,4,4], k = 1
# 输出： 3
# 解释：
# 对 nums[0] 加 -1，以及对 nums[1] 加 1，nums 变为 [3, 5, 4, 4]，可以获得 3 个不同的元素。
# 
# 
# 提示：
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 0 <= k <= 10^9
# 
# 
#

from math import inf
from typing import List
# @lc code=start
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        # 策略是尽量离散化
        nums.sort()
        res = 0
        lb = -inf
        for x in nums:
            if x + k > lb:
                lb = max(lb+1, x-k)
                res += 1

        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDistinctElements([1,2,2,3,3,4], 2)) # 6
    print(solution.maxDistinctElements([4,4,4,4], 1)) # 3
    print(solution.maxDistinctElements([1,4,4,4,4,4,4,4,4,4,4,1000], 1)) # 5
    print(solution.maxDistinctElements([1,1,1,1,1,6], 1)) # 6
