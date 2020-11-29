#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-12 07:46:21
@LastEditors: Thomas Young
@LastEditTime: 2020-06-12 07:50:21
'''
#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: #负数一定不是回文数
            return False

        s = str(x)
        l = len(s) >> 1 #一半

        isPalindrome = True
        for i in range(l):
            if s[i] != s[-i -1]:
                isPalindrome = False
                break
        
        return isPalindrome

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(-121))
    print(solution.isPalindrome(121))
    print(solution.isPalindrome(10))
    print(solution.isPalindrome(1))