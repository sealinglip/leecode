#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-11 08:53:06
LastEditors: Thomas Young
LastEditTime: 2020-09-11 09:12:33
'''
#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

# 说明：

# 所有数字都是正整数。
# 解集不能包含重复的组合。

# 示例 1:
# 输入: k = 3, n = 7
# 输出: [[1, 2, 4]]

# 示例 2:
# 输入: k = 3, n = 9
# 输出: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]

from typing import List
# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        # 暴力枚举
        res = []
        stack = []

        def findSolution(c: int, start: int, sum: int):
            if c == 1:
                if 0 < sum <= start:
                    stack.append(sum)
                    res.append(stack[:])
                    stack.pop()
            else:
                c -= 1
                for i in range(min(start, sum - 1), 0, -1):
                    stack.append(i)
                    findSolution(c, i - 1, sum - i)
                    stack.pop()

        findSolution(k, min(n, 9), n)
        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum3(3, 7))
    print(solution.combinationSum3(3, 9))