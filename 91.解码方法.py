#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-09 08:01:21
LastEditors: Thomas Young
LastEditTime: 2020-10-09 08:27:00
'''
#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#
# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
# 题目数据保证答案肯定是一个 32 位的整数。

# 示例 1：
# 输入："12"
# 输出：2
# 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。

# 示例 2：
# 输入："226"
# 输出：3
# 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

# 示例 3：
# 输入：s = "0"
# 输出：0

# 示例 4：
# 输入：s = "1"
# 输出：1

# 示例 5：
# 输入：s = "2"
# 输出：1

# 提示：
# 1 <= s.length <= 100
# s 只包含数字，并且可以包含前导零。

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if s and s[0] == '0':
            return 0
        elif len(s) <= 1:
            return 1

        # 方法1：递归
        # if len(s) > 1 and (s[0] == '1' or (s[0] == '2' and s[1] < '7')):
        #     return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
        # else:
        #     return self.numDecodings(s[1:])

        # 方法2：迭代
        n1, n2 = int(s[-1] != '0'), 1
        for i in range(len(s)-2, -1, -1): # 从后往前推
            if s[i] == '0':
                n = 0
            elif s[i] == '1' or (s[i] == '2' and s[i+1] < '7'):
                n = n1 + n2
            else:
                n = n1
            n1, n2 = n, n1
        return n1
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.numDecodings("2101"))
    # print(solution.numDecodings("27"))
    # print(solution.numDecodings("12"))
    # print(solution.numDecodings("226"))
    # print(solution.numDecodings("0"))
    # print(solution.numDecodings("1"))
    # print(solution.numDecodings("2"))
