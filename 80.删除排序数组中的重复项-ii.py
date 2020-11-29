#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-21 08:48:48
LastEditors: Thomas Young
LastEditTime: 2020-09-21 08:59:10
'''
#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
#
# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

# 示例 1:
# 给定 nums = [1, 1, 1, 2, 2, 3],
# 函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
# 你不需要考虑数组中超出新长度后面的元素。

# 示例 2:
# 给定 nums = [0, 0, 1, 1, 1, 1, 2, 3, 3],
# 函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。

# 你不需要考虑数组中超出新长度后面的元素。
# 说明:
# 为什么返回数值是整数，但输出的答案是数组呢?

# 请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

# 你可以想象内部操作如下:
# // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
# int len = removeDuplicates(nums)

# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
# for (int i=0; i < len; i++) {
#     print(nums[i])
# }

from typing import List
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        l = len(nums)
        next = None
        times = 0
        for i in range(l - 1, -1, -1): # 从尾巴往前
            val = nums[i]
            if val == next:
                if times == 2:
                    del nums[i]
                else:
                    times += 1
            else:
                times = 1
            next = val

        return len(nums)
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    print(solution.removeDuplicates(nums))
    print(nums)
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(solution.removeDuplicates(nums))
    print(nums)
