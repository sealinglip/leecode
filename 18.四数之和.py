#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-14 20:31:20
LastEditors: Thomas Young
LastEditTime: 2020-10-20 08:17:51
'''
#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
# 使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
# 注意：
# 答案中不可以包含重复的四元组。

# 示例：
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 满足要求的四元组集合为：
# [
#     [-1,  0, 0, 1],
#     [-2, -1, 1, 2],
#     [-2,  0, 0, 2]
# ]

from typing import List

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        
        nums.sort()
        cnt = len(nums)

        res = []
        for a in range(cnt):
            if a == 0 or nums[a] != nums[a - 1]:
                for b in range(a + 1, cnt):
                    if b == a + 1 or nums[b] != nums[b - 1]:
                        for c in range(b + 1, cnt):
                            if c == b + 1 or nums[c] != nums[c - 1]:
                                rest = target - nums[a] - nums[b] - nums[c]
                                if rest < nums[c]: #不符合条件，我们要找的是四数依次递增
                                    break
                                for d in range(c + 1, cnt):
                                    if nums[d] == rest:
                                        res.append(
                                            [nums[a], nums[b], nums[c], nums[d]])
                                        break
        
        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.fourSum([1, 0, -1, 0, -2, 2], 0))
