#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-23 09:42:48
@LastEditors: Thomas Young
@LastEditTime: 2020-06-23 09:58:35
'''
#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []

        a_len, b_len = len(a), len(b)
        min_len = min(a_len, b_len)
        carry_over = 0
        for i in range(1, min_len + 1):
            a1, b1 = a[a_len - i], b[b_len - i]
            sum = int(a1) + int(b1) + carry_over
            carry_over = 1 if sum > 1 else 0
            res.append(str(sum & 1))

        rest = ''
        if len(a) > min_len:
            rest = a[0 : len(a) - min_len]
        elif len(b) > min_len:
            rest = b[0 : len(b) - min_len]

        for i in range(len(rest) - 1, -1, -1):
            c = int(rest[i])
            sum = c + carry_over
            carry_over = 1 if sum > 1 else 0
            res.append(str(sum & 1))
            if not carry_over:
                res.append(rest[0:i])
                break
            
        if carry_over:
            res.append(str(carry_over))
        
        res.reverse()
        return ''.join(res)

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.addBinary('100', '110010'))
    print(solution.addBinary('11', '1'))
    print(solution.addBinary('1010', '1011'))
