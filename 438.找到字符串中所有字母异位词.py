#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2021-11-28 23:00:08
LastEditors: Thomas Young
LastEditTime: 2021-11-28 23:20:36
'''
#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。


# 示例 1:
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0, 6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

# 示例 2:
# 输入: s = "abab", p = "ab"
# 输出: [0, 1, 2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。


# 提示:
# 1 <= s.length, p.length <= 3 * 10^4
# s 和 p 仅包含小写字母


from typing import List
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 滑动窗口
        s_len = len(s)
        p_len = len(p)

        if s_len < p_len:
            return []

        ret = []
        count = [0] * 26
        for i in range(p_len):
            count[ord(s[i]) - ord('a')] -= 1
            count[ord(p[i]) - ord('a')] += 1

        # 计算差异
        diff = len([c for c in count if c != 0])
        if diff == 0:
            ret.append(0)

        for i in range(s_len - p_len):
            if count[ord(s[i]) - ord('a')] == -1:
                diff -= 1
            elif count[ord(s[i]) - ord('a')] == 0:
                diff += 1
            count[ord(s[i]) - ord('a')] += 1
            
            if count[ord(s[i + p_len]) - ord('a')] == 1:
                diff -= 1
            elif count[ord(s[i + p_len]) - ord('a')] == 0:
                diff += 1
            count[ord(s[i + p_len]) - ord('a')] -= 1

            if diff == 0:
                ret.append(i + 1)
        
        return ret
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.findAnagrams("cbaebabacd", "abc"))  # [0, 6]
    print(solution.findAnagrams("abab", "ab"))  # [0, 1, 2]
