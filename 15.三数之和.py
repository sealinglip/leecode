#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-12 09:09:05
@LastEditors: Thomas Young
@LastEditTime: 2020-06-12 11:13:51
'''
#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import List
# @lc code=start
from typing import Dict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numCount = {} # 所有数字计数
        for num in nums:
            if num in numCount:
                numCount[num] += 1
            else:
                numCount[num] = 1
        
        l = list(numCount.keys()) #找到所有数字（去重）
        res = []
        resKey = set()
        for i in range(len(l)):
            a, aCnt = l[i], numCount[l[i]]
            for j in range(i, len(l)):
                if j == i and aCnt == 1:
                    continue
                b = l[j]
                c = - a - b
                if c in numCount: # 余数也在集合中
                    # 要判断够不够数
                    if c == a:
                        if aCnt < (3 if a == b else 2): # 如果三数相等，实际上只能都是0了
                            continue
                    elif c == b:
                        if numCount[b] < 2:
                            continue

                    r = [a, b, c]
                    r.sort() # 排序方便去重
                    key = tuple(r)
                    if key not in resKey:
                        resKey.add(key)
                        res.append(r)
        
        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
