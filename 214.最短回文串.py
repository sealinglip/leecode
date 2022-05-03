#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-08-29 22:00:54
LastEditors: Thomas Young
LastEditTime: 2020-08-31 16:05:50
'''
#
# @lc app=leetcode.cn id=214 lang=python3
#
# [214] 最短回文串
#
# 给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

# 示例 1:

# 输入: "aacecaaa"
# 输出: "aaacecaaa"
# 示例 2:

# 输入: "abcd"
# 输出: "dcbabcd"

# 提示：
# 0 <= s.length <= 5 * 10^4
# s 仅由小写英文字母组成

# Hard

# @lc code=start


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        # 暴力法
        # def isPalindrome(txt: str) -> bool:
        #     return txt == txt[::-1]

        # c0 = s[0] # 第0个字符
        # offset, s_len = -1, len(s)
        # while offset > -s_len:
        #     if s[offset] == c0 and isPalindrome(s[1:offset]): # 判断此时是否构成回文子串
        #         break
        #     else:
        #         offset -= 1

        # return s[-1:offset:-1] + s

        # KMP法
        s_len = len(s)
        next = [-1] * s_len  # next的第i个元素代表s[:i+1]这个子串，前缀和后缀重合字符数减1
        for i in range(1, s_len):  # 从1开始
            j = next[i - 1]
            while j != -1 and s[j + 1] != s[i]:
                j = next[j]
            if s[j + 1] == s[i]:
                next[i] = j + 1

        best = -1
        for i in range(s_len - 1, -1, -1):  # 倒着来
            while best != -1 and s[best + 1] != s[i]:
                best = next[best]
            if s[best + 1] == s[i]:
                best += 1

        add = ("" if best == s_len - 1 else s[best+1:])
        return add[::-1] + s


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.shortestPalindrome("aacecaaa"))
    print(solution.shortestPalindrome("abcab"))
    print(solution.shortestPalindrome("abcd"))
