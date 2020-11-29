#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-14 14:47:03
LastEditors: Thomas Young
LastEditTime: 2020-08-26 08:39:55
'''
#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

from typing import List, Dict
# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: # 如果为空，直接返回
            return []

        # 初始化对照表
        letterMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = [""] # 起始值
        for d in digits:
            letters = letterMap[d]
            res = [r + c for c in letters for r in res]
        return res


# @lc code=end
    #     result = [] # 存储结果的列表
    #     self.combineLetter("", digits, letterMap, result)
    #     return result

    # def combineLetter(self, prefix: str, digits: str, letterMap: Dict, result: List):
    #     if not digits:
    #         result.append(prefix)
    #         return

    #     rest = digits[1:]
    #     for c in letterMap[digits[0]]:
    #         self.combineLetter(prefix + c, rest, letterMap, result)

if __name__ == "__main__":
    solution = Solution()
    print(solution.letterCombinations("23"))
