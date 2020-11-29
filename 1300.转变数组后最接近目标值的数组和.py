#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-14 08:48:26
@LastEditors: Thomas Young
@LastEditTime: 2020-06-14 14:29:41
'''
#
# @lc app=leetcode.cn id=1300 lang=python3
#
# [1300] 转变数组后最接近目标值的数组和
#
from typing import List

# @lc code=start
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        avg = round(target / len(arr)) # 平均值
        min, max, sum, numCnt = 100000, 1, 0, {} # 最小值、最大值、总和、数字计数：根据提示信息，设定初始值
        
        for num in arr:
            sum += num
            if num < min:
                min = num
            if num > max:
                max = num
            numCnt[num] = numCnt.get(num, 0) + 1
        
        # 数字去重，排序
        nums = list(numCnt.keys())
        nums.sort()

        if target >= sum:
            return max
        elif min >= avg:
            return avg
        else: #需要削峰
            # 从平均值往上尝试
            accum, accumCnt = 0, 0 #从小往大遍历，累计数字和和数字个数
            value, minDelta = 0, target 
            for i, num in enumerate(nums):                    
                if accum > target:
                    break
                else:
                    if num >= avg:
                        tryValue = round((target - accum) / (len(arr) - accumCnt))
                        if i > 0 and tryValue < nums[i - 1]:
                            break
                        if tryValue < num:
                            delta = target - accum - (len(arr) - accumCnt) * tryValue
                            if delta < minDelta or (delta == minDelta and value > tryValue):
                                minDelta = delta
                                value = tryValue

                    accum += num * numCnt[num]
                    accumCnt += numCnt[num]
            return value


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.findBestValue([2,3,5], 10))
    print(solution.findBestValue([4,9,3], 10))
    print(solution.findBestValue([60864, 25176, 27249, 21296, 20204], 56803))
    print(solution.findBestValue([1547, 83230, 57084, 93444, 70879], 71237))
