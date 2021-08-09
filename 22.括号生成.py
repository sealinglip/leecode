#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-14 21:44:10
@LastEditors: Thomas Young
@LastEditTime: 2020-06-14 22:44:38
'''
#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

# 示例 1：
# 输入：n = 3
# 输出：["((()))", "(()())", "(())()", "()(())", "()()()"]

# 示例 2：
# 输入：n = 1
# 输出：["()"]

# 提示：
# 1 <= n <= 8

from typing import List
# @lc code=start


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.innerGenerate("", n, 0, n << 1, res)
        return res

    def innerGenerate(self, prefix: str, left: int, balance: int, rest: int, res: List):
        if rest == 0:
            res.append(prefix)
            return

        if balance > 0:  # 可以加右括号
            self.innerGenerate(prefix + ')', left, balance - 1, rest - 1, res)
        if left > 0:  # 可以加左括号
            self.innerGenerate(
                prefix + '(', left - 1, balance + 1, rest - 1, res)

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(3))
