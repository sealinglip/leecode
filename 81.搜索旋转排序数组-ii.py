#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-26 18:14:46
LastEditors: Thomas Young
LastEditTime: 2020-10-02 09:15:01
'''
#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。

# (例如，数组[0, 0, 1, 2, 2, 5, 6] 可能变为[2, 5, 6, 0, 0, 1, 2])。

# 编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

# 示例 1:
# 输入: nums = [2, 5, 6, 0, 0, 1, 2], target = 0
# 输出: true

# 示例 2:
# 输入: nums = [2, 5, 6, 0, 0, 1, 2], target = 3
# 输出: false

# 进阶:
# 这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
# 这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？

from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) >> 1
            if nums[mid] == target:
                return True
            # 判断哪一部分可以用二分查找
            if nums[mid] > nums[low]:  # 左半部分可以二分查找
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] == nums[low]:
                low += 1
            else:  # 右半部分可以二分查找
                if nums[mid] < target <= nums[-1]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.search([3, 1], 1))
    print(solution.search([1, 3, 1, 1, 1], 3))
    print(solution.search([2, 5, 6, 0, 0, 1, 2], 0))
    print(solution.search([2, 5, 6, 0, 0, 1, 2], 3))
