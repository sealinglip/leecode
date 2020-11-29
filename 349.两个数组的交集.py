#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-11-02 00:14:20
LastEditors: Thomas Young
LastEditTime: 2020-11-02 00:18:17
'''
#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#
# 给定两个数组，编写一个函数来计算它们的交集。

# 示例 1：
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]

# 示例 2：
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4]
 
# 说明：
# 输出结果中的每个元素一定是唯一的。
# 我们可以不考虑输出结果的顺序。

from typing import List
# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return None
        # 流氓做法
        return list(set(nums1).intersection(nums2))
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.intersection([4, 9, 5], [9, 4, 9, 8, 4]))
    print(solution.intersection([1, 2, 2, 1], [2, 2]))
