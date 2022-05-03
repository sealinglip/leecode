#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-03 09:24:43
LastEditors: Thomas Young
LastEditTime: 2020-09-03 13:47:56
'''
#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#
# 验证给定的字符串是否可以解释为十进制数字。

# 有效数字（按顺序）可以分成以下几个部分：

# 一个 小数 或者 整数
# （可选）一个 'e' 或 'E' ，后面跟着一个 整数
# 小数（按顺序）可以分成以下几个部分：

# （可选）一个符号字符（'+' 或 '-'）
# 下述格式之一：
# 至少一位数字，后面跟着一个点 '.'
# 至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
# 一个点 '.' ，后面跟着至少一位数字
# 整数（按顺序）可以分成以下几个部分：

# （可选）一个符号字符（'+' 或 '-'）
# 至少一位数字
# 部分有效数字列举如下：

# ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10",
#     "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
# 部分无效数字列举如下：

# ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
# 给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。


# 示例 1：
# 输入：s = "0"
# 输出：true

# 示例 2：
# 输入：s = "e"
# 输出：false

# 示例 3：
# 输入：s = "."
# 输出：false

# 示例 4：
# 输入：s = ".1"
# 输出：true


# 提示：
# 1 <= s.length <= 20
# s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，或者点 '.' 。

# Hard
# @lc code=start


class Solution:
    def isNumber(self, s: str) -> bool:
        # # 流氓
        # try:
        #     float(s)
        # except:
        #     return False
        # else:
        #     return True

        if not s:
            return False
        # Deterministic finite automaton (DFA, 确定有穷状态自动机)
        # 状态转移表
        # state blank   +/- 0-9 .   e   other
        # 0     0   	1   6	2   -1  -1
        # 1     -1      -1	6	2   -1  -1
        # 2     -1      -1	3   -1  -1  -1
        # 3     8       -1	3   -1	4   -1
        # 4     -1  	7	5   -1  -1  -1
        # 5     8       -1	5   -1  -1  -1
        # 6     8       -1	6	3	4   -1
        # 7     -1      -1	5   -1  -1  -1
        # 8     8       -1  -1  -1  -1  -1
        transfer = [[0, 1, 6, 2, -1, -1],
                    [-1, -1, 6, 2, -1, -1],
                    [-1, -1, 3, -1, -1, -1],
                    [8, -1, 3, -1, 4, -1],
                    [-1, 7, 5, -1, -1, -1],
                    [8, -1, 5, -1, -1, -1],
                    [8, -1, 6, 3, 4, -1],
                    [-1, -1, 5, -1, -1, -1],
                    [8, -1, -1, -1, -1, -1]]
        finals = [0, 0, 0, 1, 0, 1, 1, 0, 1]  # 最终状态3、5、6、8有效

        def type(c: str) -> int:  # 将字符转换为类型
            if c == ' ':
                return 0
            elif c == '+' or c == '-':
                return 1
            elif c >= '0' and c <= '9':
                return 2
            elif c == '.':
                return 3
            elif c == 'e' or c == 'E':
                return 4
            else:
                return 5

        state = 0
        for c in s:
            state = transfer[state][type(c)]
            if state < 0:
                return False
        return finals[state] == 1


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.isNumber(""))
    print(solution.isNumber("53.5e93"))
    print(solution.isNumber("53."))
    print(solution.isNumber("-.5e93"))
    print(solution.isNumber("+.5e93"))
    print(solution.isNumber(".5e93"))
    print(solution.isNumber("53.5"))
    print(solution.isNumber(" 6e-1"))
    print(solution.isNumber(" 6e+1"))
    print(solution.isNumber(" -90e3   "))
    print(solution.isNumber("1 a"))
    print(solution.isNumber(" 0.1 "))
    print(solution.isNumber("5abc"))
    print(solution.isNumber("2e10"))
    print(solution.isNumber(" 99e2.5  "))
