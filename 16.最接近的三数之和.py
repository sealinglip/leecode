#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-13 09:06:16
LastEditors: Thomas Young
LastEditTime: 2020-10-05 08:17:37
'''
#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，
# 使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

# 示例：
# 输入：nums = [-1, 2, 1, -4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1=2) 。

# 提示：
# 3 <= nums.length <= 10 ^ 3
# -10 ^ 3 <= nums[i] <= 10 ^ 3
# -10 ^ 4 <= target <= 10 ^ 4

from typing import List
# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) < 3:
            return None
        elif len(nums) == 3:
            return sum(nums)

        nums.sort() # 排序

        cnt, total = len(nums), sum(nums[0:3]) # 数组长度、三数总和
        for first in range(cnt - 2):
            if first == 0 or nums[first] != nums[first - 1]: # 只处理第一个或和前一个不等的（跳过重复）
                b, c = first + 1, cnt - 1
                t = nums[first] + nums[b] + nums[b + 1]
                if t > target: # 已经超了，不用再往后试了
                    if abs(t - target) < abs(total - target):
                        total = t
                    break
                t = nums[first] + nums[-2] + nums[-1]
                if t < target:
                    if abs(t - target) < abs(total - target):
                        total = t
                    continue

                while b < c:
                    t = nums[first] + nums[b] + nums[c]
                    if t > target:
                        c -= 1
                    elif t < target:
                        b += 1
                    else:
                        return target
                    if abs(t - target) < abs(total - target):
                        total = t

        return total

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSumClosest([-1, 2, 1, -4], 1))
    print(solution.threeSumClosest([0, 1, 2], 0))

