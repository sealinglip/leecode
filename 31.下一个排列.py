#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-17 10:22:38
LastEditors: Thomas Young
LastEditTime: 2020-11-10 08:43:17
'''
#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 必须原地修改，只允许使用额外常数空间。

# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1, 2, 3 → 1, 3, 2
# 3, 2, 1 → 1, 2, 3
# 1, 1, 5 → 1, 5, 1

from typing import List
# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums:
            # 从后往前找，找到最后一个升序的对，比如i-1, i，调整位置(找到比i-1位置大的最小值，交换再翻转)
            # 如果一直没找到，整个数组转置
            swap = False
            total = len(nums)
            for i in range(total - 1, 0, -1):
                if nums[i] > nums[i - 1]:
                    swap = True
                    # 先确定需要翻转的区间，从后往前找，找到最接近nums[i - 1]的数nums[r]
                    # 此时nums[i : r + 1]为降序排列，且元素均大于nums[i - 1]
                    r = total - 1
                    while nums[r] <= nums[i - 1]:
                        r -= 1
                    # 然后交换i-1和r
                    # 交换之后nums[i : total]为降序排列
                    nums[r], nums[i - 1] = nums[i - 1], nums[r]

                    # 翻转区间[i, total - 1]
                    l, r = i, total - 1
                    while l < r:
                        nums[l], nums[r] = nums[r], nums[l]
                        l += 1
                        r -= 1
                    break

            if not swap:
                for i in range(total >> 1):
                    nums[i], nums[total - i - 1] = nums[total - i - 1], nums[i]

        return nums
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.nextPermutation([3, 2, 1]))
    print(solution.nextPermutation([2, 3, 1]))
    print(solution.nextPermutation([2, 3, 4, 1]))
    print(solution.nextPermutation([2, 4, 3, 1]))
    print(solution.nextPermutation([3, 2, 1]))
    print(solution.nextPermutation([1, 3, 2, 1]))
