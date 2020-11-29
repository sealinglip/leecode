#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-21 16:22:42
@LastEditors: Thomas Young
@LastEditTime: 2020-06-21 16:54:52
'''
#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
from typing import List
# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        nums_len = len(nums)
        low, high = 0, nums_len -1

        while low <= high:
            mid = (low + high) >> 1
            mid_val = nums[mid]

            if mid_val < target:
                low = mid + 1
            elif mid_val > target:
                high = mid - 1
            else: # 找到，再确定范围
                # mid 指向就是target，往前推至low，往后推至high，确定左右边界
                l, r = mid, mid
                while low <= l:
                    m = (low + l) >> 1
                    m_val = nums[m]
                    if m_val < target:
                        low = m + 1
                    elif m_val >= target:
                        if m == 0 or nums[m - 1] != target:
                            l = m
                            break
                        l = m - 1
                while r <= high:
                    m = (r + high) >> 1
                    m_val = nums[m]
                    if m_val <= target:
                        if m == nums_len - 1 or nums[m + 1] != target:
                            r = m
                            break
                        r = m + 1
                    elif m_val > target:
                        high = m - 1
                return [l, r]

        return [-1, -1]
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 6))
