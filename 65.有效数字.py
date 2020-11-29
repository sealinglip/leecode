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

# 例如:
# "0" = > true
# " 0.1 " = > true
# "abc" = > false
# "1 a" = > false
# "2e10" = > true
# " -90e3   " = > true
# " 1e" = > false
# "e3" = > false
# " 6e-1" = > true
# " 99e2.5 " = > false
# "53.5e93" = > true
# " --6 " = > false
# "-+3" = > false
# "95a54e53" = > false

# 说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。
# 这里给出一份可能存在于有效十进制数字中的字符列表：
# 数字 0-9
# 指数 - "e"
# 正/负号 - "+"/"-"
# 小数点 - "."
# 当然，在输入中，这些字符的上下文也很重要。

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
        finals = [0, 0, 0, 1, 0, 1, 1, 0, 1] # 最终状态3、5、6、8有效

        def type(c:str) -> int: # 将字符转换为类型
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
