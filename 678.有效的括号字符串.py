#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2021-09-12 15:36:35
LastEditors: Thomas Young
LastEditTime: 2021-09-12 16:15:05
'''
#
# @lc app=leetcode.cn id=678 lang=python3
#
# [678] 有效的括号字符串
#
# 给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：

# 任何左括号(必须有相应的右括号)。
# 任何右括号) 必须有相应的左括号(。
# 左括号(必须在对应的右括号之前)。
# * 可以被视为单个右括号) ，或单个左括号(，或一个空字符串。
# 一个空字符串也被视为有效字符串。

# 示例 1:
# 输入: "()"
# 输出: True

# 示例 2:
# 输入: "(*)"
# 输出: True

# 示例 3:
# 输入: "(*))"
# 输出: True

# 注意:
# 字符串大小将在[1，100] 范围内。

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        unmatchedleftParenthesisCnt = [0, 0] # 最少未匹配的左括号数和最多未匹配的左括号数
        for c in s:
            if c == '(':
                unmatchedleftParenthesisCnt[0] += 1
                unmatchedleftParenthesisCnt[1] += 1
            elif c == ')':
                if unmatchedleftParenthesisCnt[0] > 0:
                    unmatchedleftParenthesisCnt[0] -= 1
                unmatchedleftParenthesisCnt[1] -= 1
                if unmatchedleftParenthesisCnt[1] < 0:
                    return False
            elif c == '*':
                if unmatchedleftParenthesisCnt[0] > 0:
                    unmatchedleftParenthesisCnt[0] -= 1
                unmatchedleftParenthesisCnt[1] += 1
        
        return unmatchedleftParenthesisCnt[0] == 0


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.checkValidString(
        "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))  # False
    print(solution.checkValidString("()")) # True
    print(solution.checkValidString("(*)")) # True
    print(solution.checkValidString("(*))")) # True
