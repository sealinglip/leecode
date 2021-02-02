#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2021-02-02 21:16:14
LastEditors: Thomas Young
LastEditTime: 2021-02-02 21:39:12
'''
#
# @lc app=leetcode.cn id=424 lang=python3
#
# [424] 替换后的最长重复字符
#
# 给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。
# 在执行上述操作后，找到包含重复字母的最长子串的长度。
# 注意：字符串长度 和 k 不会超过 104。

# 示例 1：
# 输入：s = "ABAB", k = 2
# 输出：4
# 解释：用两个'A'替换为两个'B', 反之亦然。

# 示例 2：
# 输入：s = "AABABBA", k = 1
# 输出：4
# 解释：
# 将中间的一个'A'替换为'B', 字符串变为 "AABBBBA"。
# 子串 "BBBB" 有最长重复字母, 答案为 4。

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26 # 记录窗口内字符统计
        N = len(s)

        maxn = l = r = 0 # 分别为区间内最多的相同字符数，左边界，右边界

        while r < N:
            count[ord(s[r]) - ord('A')] += 1
            maxn = max(maxn, count[ord(s[r]) - ord('A')]) # 更新区间内最多的字符
            if r - l + 1 - maxn > k: # 区间内字符不满足异类小于k的条件
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            r += 1

        return r - l
        
# @lc code=end

