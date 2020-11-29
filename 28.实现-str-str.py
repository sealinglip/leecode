#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-17 10:13:32
@LastEditors: Thomas Young
@LastEditTime: 2020-06-17 10:22:16
'''
#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        elif not haystack:
            return -1
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                match = True
                j = 1
                while j < len(needle):
                    if haystack[i + j] != needle[j]:
                        match = False
                        break
                    j += 1
                if match:
                    return i

        return -1
        
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.strStr('hello', 'll'))
    print(solution.strStr('aaaaa', 'bba'))
