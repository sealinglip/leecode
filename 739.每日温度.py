#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-11 09:25:46
@LastEditors: Thomas Young
@LastEditTime: 2020-06-11 09:40:27
'''
#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#
from typing import List
from collections import deque
# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        total = len(T) # 总天数
        # 从日期倒着遍历，维护一个最高气温的列表，
        stack = deque()
        res = []
        d = total - 1
        while d > -1:
            curT = T[d] # 当前温度
            nearestHigher = None #最近的比自己高的那天
            while len(stack):
                tv, di = stack[0]
                if tv <= curT:
                    stack.popleft() #比当前温度低，不符合条件，而且出栈了
                else:
                    nearestHigher = di
                    break
            stack.appendleft((curT, d)) # 当前温度入栈
            if nearestHigher:
                res.append(nearestHigher - d)
            else:
                res.append(0)
            d -= 1

        res.reverse() # 翻转
        return res
        
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    # solution.dailyTemperatures()
    # solution.dailyTemperatures()
