#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-23 09:31:16
LastEditors: Thomas Young
LastEditTime: 2020-09-23 22:05:02
'''
#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

# 注意:
# 不能使用代码库中的排序函数来解决这道题。

# 示例:
# 输入: [2, 0, 2, 1, 1, 0]
# 输出: [0, 0, 1, 1, 2, 2]

# 进阶：
# 一个直观的解决方案是使用计数排序的两趟扫描算法。
# 首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
# 你能想出一个仅使用常数空间的一趟扫描算法吗？

from typing import List
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums:
            p1, cur, p2 = 0, 0, len(nums) - 1

            while cur <= p2:
                if nums[cur] == 2:
                    nums[cur], nums[p2] = nums[p2], nums[cur]
                    p2 -= 1
                elif nums[cur] == 0:
                    nums[cur], nums[p1] = nums[p1], nums[cur]
                    p1 += 1
                    cur += 1
                else:
                    cur += 1
                
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    list = [1, 2, 0]
    solution.sortColors(list)
    print(list)
    list = [2, 0, 1]
    solution.sortColors(list)
    print(list)
    list = [2, 0, 2, 1, 1, 0]
    solution.sortColors(list)
    print(list)
