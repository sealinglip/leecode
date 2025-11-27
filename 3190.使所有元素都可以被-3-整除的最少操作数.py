#
# @lc app=leetcode.cn id=3190 lang=python3
#
# [3190] 使所有元素都可以被 3 整除的最少操作数
#
# https://leetcode.cn/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/
#
# algorithms
# Easy (81.18%)
# Likes:    7
# Dislikes: 0
# Total Accepted:    12K
# Total Submissions: 14.3K
# Testcase Example:  '[1,2,3,4]'
#
# 给你一个整数数组 nums 。一次操作中，你可以将 nums 中的 任意 一个元素增加或者减少 1 。
# 请你返回将 nums 中所有元素都可以被 3 整除的 最少 操作次数。
# 
# 
# 示例 1：
# 输入：nums = [1,2,3,4]
# 输出：3
# 解释：
# 通过以下 3 个操作，数组中的所有元素都可以被 3 整除：
# 将 1 减少 1 。
# 将 2 增加 1 。
# 将 4 减少 1 。
# 
# 示例 2：
# 输入：nums = [3,6,9]
# 输出：0
# 
# 
# 提示：
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 50
# 
# 
#

from typing import List
# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(nums) - sum(0 if x % 3 else 1 for x in nums)
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumOperations([1,2,3,4])) # 3
    print(solution.minimumOperations([3,6,9])) # 0
