#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-11 22:20:02
@LastEditors: Thomas Young
@LastEditTime: 2020-06-11 23:27:56
'''
#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: #如果为1行，那么直接返回
            return s

        totalLen = len(s)
        period = (numRows << 1) - 2 #循环周期
        times = (totalLen + period - 1) // period  # 包含times个周期
        output = [] #输出
        
        for i in range(times):
            output.append(s[i * period])
            
        for j in range(1, numRows - 1):
            for i in range(times):
                p = i * period + j
                if p < totalLen:
                    output.append(s[p])
                    p = (i + 1) * period - j
                    if p < totalLen:
                        output.append(s[p])
                else:
                    break

        for i in range(times):
            p = i * period + numRows - 1
            if p < totalLen:
                output.append(s[p])
            else:
                break

        return "".join(output)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.convert("LEETCODEISHIRING", 2))
    print(solution.convert("LEETCODEISHIRING", 3))
    print(solution.convert("LEETCODEISHIRING", 4))
