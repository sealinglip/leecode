#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-11-26 22:53:41
LastEditors: Thomas Young
LastEditTime: 2020-11-26 23:19:20
'''
#
# @lc app=leetcode.cn id=164 lang=python3
#
# [164] 最大间距
#
# 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
# 如果数组元素个数小于 2，则返回 0。

# 示例 1:
# 输入: [3, 6, 9, 1]
# 输出: 3
# 解释: 排序后的数组是[1, 3, 6, 9], 其中相邻元素(3, 6) 和(6, 9) 之间都存在最大差值 3。

# 示例 2:
# 输入: [10]
# 输出: 0
# 解释: 数组元素个数小于 2，因此返回 0。

# 说明:
# 你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
# 请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9

# Hard
from typing import List
# @lc code=start


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return 0

        # 求左右边界
        L = R = nums[0]
        for n in nums:
            if n < L:
                L = n
            if n > R:
                R = n

        # 桶大小
        width = math.ceil((R-L)/(len(nums)-1))
        if width == 0:
            return 0

        # 求每个桶的最大值和最小值
        MAX = R+1
        MIN = L-1
        minbucket = [MAX for _ in range((R-L)//width+1)]
        maxbucket = [MIN for _ in range(len(minbucket))]
        for n in nums:
            idx = (n-L)//width
            if n < minbucket[idx]:
                minbucket[idx] = n
            if n > maxbucket[idx]:
                maxbucket[idx] = n
        prev = MAX

        res = 0
        for i, j in zip(minbucket, maxbucket):
            if i != MAX:
                if i-prev > res:
                    res = i-prev
                prev = j
        return res

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumGap([3, 6, 9, 1]))
    print(solution.maximumGap([10]))
