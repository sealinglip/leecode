#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-08-31 16:30:34
LastEditors: Thomas Young
LastEditTime: 2020-08-31 16:41:04
'''
#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
# 给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。
# 如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

# 如果不存在最后一个单词，请返回 0。
# 说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。

# 示例:
# 输入: "Hello World"
# 输出: 5

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        
        wEnd = len(s) - 1
        while wEnd >= 0 and s[wEnd] == ' ':
            wEnd -= 1
        if wEnd < 0:
            return 0
        
        wBegin = wEnd - 1
        while wBegin >= 0 and s[wBegin] != ' ':
            wBegin -= 1
        
        return wEnd - wBegin
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLastWord("Hello world"))
    print(solution.lengthOfLastWord(" "))
    print(solution.lengthOfLastWord("a"))
