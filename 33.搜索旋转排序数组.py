#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-20 13:22:45
LastEditors: Thomas Young
LastEditTime: 2020-10-02 09:04:32
'''
#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。

# (例如，数组[0, 1, 2, 4, 5, 6, 7] 可能变为[4, 5, 6, 7, 0, 1, 2])。

# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 - 1 。

# 你可以假设数组中不存在重复的元素。

# 你的算法时间复杂度必须是 O(log n) 级别。

# 示例 1:
# 输入: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
# 输出: 4

# 示例 2:
# 输入: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
# 输出: -1

from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) >> 1
            if nums[mid] == target:
                return mid
            # 判断哪一部分可以用二分查找
            if nums[mid] >= nums[0]:  # 左半部分可以二分查找（mid可能和0重合）
                if nums[0] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else: # 右半部分可以二分查找
                if nums[mid] < target <= nums[-1]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.search([3, 1], 1))
    print(solution.search([3, 1], 0))
    print(solution.search([1, 3], 0))
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))
