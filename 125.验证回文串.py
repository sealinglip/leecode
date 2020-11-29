#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-19 13:46:05
@LastEditors: Thomas Young
@LastEditTime: 2020-06-19 14:08:26
'''
#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
# @lc code=start
from typing import Tuple
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        def nextChar(txt: str, idx: int, dir: bool) -> Tuple:
            c = None
            while (dir and idx < len(txt) - 1) or (not dir and idx > 0):
                idx += 1 if dir else -1
                c = txt[idx]
                if c.isdigit() or c.isalpha():
                    break
                else:
                    c = None
            return c.lower() if c else None, idx

        l, r = nextChar(s, -1, True), nextChar(s, len(s), False)
        palindrome = True
        while l[1] < r[1]:
            if l[0] and l[0] != r[0]:
                palindrome = False
                break
            l, r = nextChar(s, l[1], True), nextChar(s, r[1], False)
        
        return palindrome

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(" "))
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))
