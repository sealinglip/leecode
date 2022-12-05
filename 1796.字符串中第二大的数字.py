#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2022-12-03 21:31:08
LastEditors: Thomas Young
LastEditTime: 2022-12-03 21:37:53
'''
#
# @lc app=leetcode.cn id=1796 lang=python3
#
# [1796] 字符串中第二大的数字
#
# 给你一个混合字符串 s ，请你返回 s 中 第二大 的数字，如果不存在第二大的数字，请你返回 - 1 。

# 混合字符串 由小写英文字母和数字组成。


# 示例 1：
# 输入：s = "dfa12321afd"
# 输出：2
# 解释：出现在 s 中的数字包括[1, 2, 3] 。第二大的数字是 2 。

# 示例 2：
# 输入：s = "abc1111"
# 输出：- 1
# 解释：出现在 s 中的数字只包含[1] 。没有第二大的数字。


# 提示：
# 1 <= s.length <= 500
# s 只包含小写英文字母和（或）数字。

# @lc code=start
class Solution:
    def secondHighest(self, s: str) -> int:
        highest = secHighest = -1
        for c in s:
            if c.isdigit():
                d = int(c)
                if d > highest:
                    highest, secHighest = d, highest
                elif highest > d > secHighest:
                    secHighest = d
        return secHighest
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.secondHighest("dfa12321afd")) # 2
    print(solution.secondHighest("abc1111"))  # -1
