#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-17 10:13:32
@LastEditors: Thomas Young
@LastEditTime: 2020-06-17 10:22:16
'''
#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#
# 实现 strStr() 函数。
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回 - 1 。

# 说明：
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

# 示例 1：
# 输入：haystack = "hello", needle = "ll"
# 输出：2

# 示例 2：
# 输入：haystack = "aaaaa", needle = "bba"
# 输出：- 1

# 示例 3：
# 输入：haystack = "", needle = ""
# 输出：0

# 提示：
# 0 <= haystack.length, needle.length <= 5 * 10^4
# haystack 和 needle 仅由小写英文字符组成

# @lc code=start


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        elif not haystack:
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                match = True
                j = 1
                while j < len(needle):
                    if haystack[i + j] != needle[j]:
                        match = False
                        break
                    j += 1
                if match:
                    return i

        return -1


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.strStr('hello', 'll'))
    print(solution.strStr('aaaaa', 'bba'))
