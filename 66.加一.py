#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-01 09:32:36
LastEditors: Thomas Young
LastEditTime: 2020-09-01 09:45:31
'''
#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。

# 示例 1:
# 输入: [1, 2, 3]
# 输出: [1, 2, 4]
# 解释: 输入数组表示数字 123。

# 示例 2:
# 输入: [4, 3, 2, 1]
# 输出: [4, 3, 2, 2]
# 解释: 输入数组表示数字 4321。

from typing import List
# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits:
            for i in range(len(digits)-1, -1, -1):
                digits[i] += 1
                if digits[i] < 10:
                    break
                else: # 有进位
                    digits[i] = 0
            else:
                digits.insert(0, 1)

        return digits
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([4, 3, 2, 1]))
    print(solution.plusOne([1, 2, 3]))
    print(solution.plusOne([9]))
    print(solution.plusOne([9, 9]))
