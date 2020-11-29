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

        if balance > 0: # 可以加右括号
            self.innerGenerate(prefix + ')', left, balance - 1, rest - 1, res)
        if left > 0: # 可以加左括号
            self.innerGenerate(prefix + '(', left - 1, balance + 1, rest - 1, res)

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(3))
