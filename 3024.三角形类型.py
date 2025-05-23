#
# @lc app=leetcode.cn id=3024 lang=python3
#
# [3024] 三角形类型
#
# https://leetcode.cn/problems/type-of-triangle/description/
#
# algorithms
# Easy (63.94%)
# Likes:    6
# Dislikes: 0
# Total Accepted:    15K
# Total Submissions: 23.9K
# Testcase Example:  '[3,3,3]'
#
# 给你一个下标从 0 开始长度为 3 的整数数组 nums ，需要用它们来构造三角形。
# 
# 如果一个三角形的所有边长度相等，那么这个三角形称为 equilateral 。
# 如果一个三角形恰好有两条边长度相等，那么这个三角形称为 isosceles 。
# 如果一个三角形三条边的长度互不相同，那么这个三角形称为 scalene 。
# 
# 如果这个数组无法构成一个三角形，请你返回字符串 "none" ，否则返回一个字符串表示这个三角形的类型。
# 
# 
# 示例 1：
# 输入：nums = [3,3,3]
# 输出："equilateral"
# 解释：由于三条边长度相等，所以可以构成一个等边三角形，返回 "equilateral" 。
# 
# 
# 示例 2：
# 输入：nums = [3,4,5]
# 输出："scalene"
# 解释：
# nums[0] + nums[1] = 3 + 4 = 7 ，大于 nums[2] = 5 。
# nums[0] + nums[2] = 3 + 5 = 8 ，大于 nums[1] = 4 。
# nums[1] + nums[2] = 4 + 5 = 9 ，大于 nums[0] = 3 。
# 由于任意两边之和都大于第三边，所以可以构成一个三角形，因为三条边的长度互不相等，所以返回 "scalene"。
# 
# 
# 提示：
# nums.length == 3
# 1 <= nums[i] <= 100
# 
# 
#

from typing import List
# @lc code=start
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if (max(nums) << 1) >= sum(nums):
            return "none"
        d = {1: "equilateral", 2: "isosceles", 3: "scalene"}
        return d.get(len(set(nums)), "scalene")
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.triangleType([8,4,2])) # "none"
    print(solution.triangleType([3,3,3])) # "equilateral"
    print(solution.triangleType([3,4,5])) # "scalene"
