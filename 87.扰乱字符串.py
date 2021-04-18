#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-21 09:03:36
LastEditors: Thomas Young
LastEditTime: 2020-09-21 23:28:06
'''
#
# @lc app=leetcode.cn id=87 lang=python3
#
# [87] 扰乱字符串
#
# 给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。

# 下图是字符串 s1 = "great" 的一种可能的表示形式。

#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
# 在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。

# 例如，如果我们挑选非叶节点 "gr" ，交换它的两个子节点，将会产生扰乱字符串 "rgeat" 。

#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# 我们将 "rgeat” 称作 "great" 的一个扰乱字符串。

# 同样地，如果我们继续交换节点 "eat" 和 "at" 的子节点，将会产生另一个新的扰乱字符串 "rgtae" 。

#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# 我们将 "rgtae” 称作 "great" 的一个扰乱字符串。

# 给出两个长度相等的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。

# 示例 1:
# 输入: s1 = "great", s2 = "rgeat"
# 输出: true

# 示例 2:
# 输入: s1 = "abcde", s2 = "caebd"
# 输出: false

from functools import cache
# @lc code=start
from collections import Counter


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        elif s1 is None or s2 is None or len(s1) != len(s2):  # 长度不一致
            return False

        l = len(s1)
        if l == 2:
            return s1 == s2[::-1]

        # 方法1：会超时
        # 可进行改进，缓存局部结果
        # c1 = Counter()
        # c2 = Counter()
        # for i in range(l - 1):
        #     c1.update(s1[i])
        #     c2.update(s2[i])
        #     if c1 == c2:
        #         leftScramble = self.isScramble(s1[:i+1], s2[:i+1])
        #         if leftScramble and self.isScramble(s1[i+1:], s2[i+1:]):
        #             return True

        # c1.clear() # reset
        # c2.clear() # reset
        # for i in range(l - 1):
        #     c1.update(s1[i])
        #     c2.update(s2[-1 - i])
        #     if c1 == c2:
        #         leftScramble = self.isScramble(s1[:i+1], s2[l-1-i:])
        #         if leftScramble and self.isScramble(s1[i+1:], s2[:l-1-i]):
        #             return True
        # return False

        @cache
        def dfs(i1: int, i2: int, length: int) -> bool:
            """
            第一个字符串从 i1 开始，第二个字符串从 i2 开始，子串的长度为 length，是否和谐
            """

            # 判断两个子串是否相等
            if s1[i1:i1+length] == s2[i2:i2+length]:
                return True

            # 判断是否存在字符 c 在两个子串中出现的次数不同
            if Counter(s1[i1:i1+length]) != Counter(s2[i2:i2+length]):
                return False

            # 枚举分割位置
            for i in range(1, length):
                # 不交换的情况
                if dfs(i1, i2, i) and dfs(i1 + i, i2 + i, length - i):
                    return True
                # 交换的情况
                if dfs(i1, i2 + length - i, i) and dfs(i1 + i, i2, length - i):
                    return True

            return False

        ans = dfs(0, 0, len(s1))
        dfs.cache_clear()
        return ans
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.isScramble("abcdbdacbdac", "bdacabcdbdac"))
    print(solution.isScramble("eebaacbcbcadaaedceaaacadccd",
                              "eadcaacabaddaceacbceaabeccd"))
    # print(solution.isScramble("great", "rgeat"))
    # print(solution.isScramble("abcde", "caebd"))
