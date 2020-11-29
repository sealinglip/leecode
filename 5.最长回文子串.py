#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-11 19:37:32
LastEditors: Thomas Young
LastEditTime: 2020-09-29 09:18:23
'''
#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

# 示例 1：
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。

# 示例 2：
# 输入: "cbbd"
# 输出: "bb"

# @lc code=start
from typing import Tuple
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s

        totalLen, longestPLen, longestLeft, i = len(s), 0, -1, 0

        while i < totalLen:
            # 以i为中心测试是否存在回文子串
            left, length = self.tryOddPalindrome(s, totalLen, i)
            left2, length2 = self.tryEvenPalindrome(s, totalLen, i)
            if length2 > length:
                length = length2
                left = left2
            if length > longestPLen:
                longestPLen = length
                longestLeft = left
            
            i += 1
        
        return s[longestLeft: longestLeft + longestPLen]

    def tryOddPalindrome(self, s: str, total: int, i: int) -> Tuple:
        distance = 1
        while distance <= i and distance < (total - i) and s[i - distance] == s[i + distance]:
            distance += 1
        return i - distance + 1, (distance << 1) - 1

    def tryEvenPalindrome(self, s: str, total: int, i: int) -> Tuple:
        if i == total - 1 or s[i] != s[i + 1]:
            return i, 0
        distance = 1
        while distance <= i and distance < (total - i - 1) and s[i - distance] == s[i + 1 + distance]:
            distance += 1
        return i - distance + 1, distance << 1
            
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome('babad'))
    print(solution.longestPalindrome('cbbd'))
    print(solution.longestPalindrome('ccc'))

