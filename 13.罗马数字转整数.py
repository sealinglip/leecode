#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-12 15:03:30
@LastEditors: Thomas Young
@LastEditTime: 2020-07-01 10:20:21
'''
#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0

        res = 0
        curChar, mark, idx, l = s[0], 0, 1, len(s) #首字母，标记位置，当前索引，总长度
        while idx < l:
            char = s[idx]
            if char != curChar:
                if (curChar == 'I' and (char == 'V' or char == 'X')) \
                    or (curChar == 'X' and (char == 'L' or char == 'C')) \
                    or (curChar == 'C' and (char == 'D' or char == 'M')):
                    idx += 1
                    res += self.partToInt(s[mark : idx])
                    mark = idx
                    if idx < l:
                        curChar = s[idx]
                else:
                    res += self.partToInt(s[mark: idx])
                    mark = idx
                    curChar = char
            idx += 1

        res += self.partToInt(s[mark : idx])
        return res

    def partToInt(self, part: str) -> int:
        if not part:
            return 0
            
        if part[0] == part[-1]:
            unit = 1
            if part[0] == 'V':
                unit = 5
            elif part[0] == 'X':
                unit = 10
            elif part[0] == 'L':
                unit = 50
            elif part[0] == 'C':
                unit = 100
            elif part[0] == 'D':
                unit = 500
            elif part[0] == 'M':
                unit = 1000
            return unit * len(part)
        elif part == "IV":
            return 4
        elif part == "IX":
            return 9
        elif part == "XL":
            return 40
        elif part == "XC":
            return 90
        elif part == "CD":
            return 400
        elif part == "CM":
            return 900

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    # print(solution.romanToInt("XII"))
    # print(solution.romanToInt("III"))
    print(solution.romanToInt("IV"))
    print(solution.romanToInt("IX"))
    print(solution.romanToInt("LVIII"))
    print(solution.romanToInt("MCMXCIV"))

