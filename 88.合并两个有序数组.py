#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-04 10:18:04
LastEditors: Thomas Young
LastEditTime: 2020-09-04 13:18:42
'''
#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

# 说明:
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

# 示例:
# 输入:
# nums1 = [1, 2, 3, 0, 0, 0], m = 3
# nums2 = [2, 5, 6],       n = 3

# 输出: [1, 2, 2, 3, 5, 6]

from typing import List
# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] < nums2[n]:
                nums1[p] = nums2[n]
                n -= 1
            else:
                nums1[p] = nums1[m]
                m -= 1
            p -= 1

        while n >= 0:
            nums1[p] = nums2[n]
            n -= 1
            p -= 1

# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    list1 = [1, 2, 3, 0, 0, 0]
    solution.merge(list1, 3, [2, 5, 6], 3)
    print(list1)
