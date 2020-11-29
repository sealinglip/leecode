#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-13 09:00:36
@LastEditors: Thomas Young
@LastEditTime: 2020-06-13 09:06:00
'''
#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack:
                    return False
                pre = stack.pop()
                if (c == ')' and pre != '(') \
                    or (c == '}' and pre != '{') \
                    or (c == ']' and pre != '['):
                    return False
        return not stack # 必须为空才合理
# @lc code=end

