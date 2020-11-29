#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-27 09:38:51
@LastEditors: Thomas Young
@LastEditTime: 2020-06-27 10:34:55
'''
#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        len_num1, len_num2 = len(num1), len(num2)
        res = [0 for i in range(len_num1 + len_num2)]  # 存放结果
        for i in range(len(num1)):
            a = int(num1[i])
            for j in range(len(num2)):
                b = int(num2[j])
                product = a * b
                carry = product // 10
                remainder = product - (carry * 10)
                bit = len_num1 + len_num2 - i - j - 2
                res[bit] += remainder
                if res[bit] >= 10:
                    carry += 1
                    res[bit] -= 10
                bit += 1
                while carry > 0:
                    res[bit] += carry
                    if res[bit] >= 10:
                        carry = 1
                        res[bit] -= 10
                    else:
                        carry = 0
                    bit += 1
        s = []
        bit = len(res) - 1
        while bit >= 0 and res[bit] == 0:
            bit -= 1
        while bit >= 0:
            s.append(str(res[bit]))
            bit -= 1
        return "".join(s)

# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.multiply('123', '456'))
