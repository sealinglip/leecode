#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-08 12:45:26
LastEditors: Thomas Young
LastEditTime: 2020-10-08 12:49:41
'''
#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#
# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
# 你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

# 示例 1：
# 输入：["h", "e", "l", "l", "o"]
# 输出：["o", "l", "l", "e", "h"]

# 示例 2：
# 输入：["H", "a", "n", "n", "a", "h"]
# 输出：["h", "a", "n", "n", "a", "H"]

from typing import List
# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if s:
            l = len(s)
            for i in range(l >> 1):
                s[i], s[l-i-1] = s[l-i-1], s[i]
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    list = ["h", "e", "l", "l", "o"]
    solution.reverseString(list)
    print(list)

    list = ["H", "a", "n", "n", "a", "h"]
    solution.reverseString(list)
    print(list)
