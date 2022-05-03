#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-19 14:09:06
@LastEditors: Thomas Young
@LastEditTime: 2020-07-05 16:26:38
'''
#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
# 给定一个字符串(s) 和一个字符模式(p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
# 两个字符串完全匹配才算匹配成功。

# 说明:

# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
# 示例 1:

# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 示例 2:

# 输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。
# 示例 3:

# 输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
# 示例 4:

# 输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
# 示例 5:

# 输入:
# s = "acdcb"
# p = "a*c?b"
# 输出: false
#

# Hard
# @lc code=start


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}  # 缓存结果

        def match(txt: str, ti: int, pa: str, pi: int) -> bool:
            if ti == len(txt):
                if pi == len(pa):
                    return True
                elif pa[pi] == '*':
                    while pi + 1 < len(pa) and pa[pi + 1] == '*':
                        pi += 1
                    return match(txt, ti, pa, pi + 1)
                else:
                    return False
            elif pi == len(pa):
                return False

            key = (ti, pi)
            if key in cache:
                return cache[key]

            m = False
            if pa[pi] == '*':
                while pi + 1 < len(pa) and pa[pi + 1] == '*':
                    pi += 1
                # greedy
                pi, i = pi + 1, len(s)
                while i >= ti:
                    if match(txt, i, pa, pi):
                        m = True
                        break
                    i -= 1
            elif pa[pi] == '?' or pa[pi] == txt[ti]:
                m = match(txt, ti + 1, pa, pi + 1)

            cache[key] = m
            return m
        return match(s, 0, p, 0)


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.isMatch(
        "aabbbbbaabaaaaabbbabababbbababaabbbababbbbaababbabaaababaaabbbbaabbbbabbbbbbbaabbaabbaaaabbbaababaababaaabbbbbbabbbbbbbbaaaaabbaabbaabaaabbbaabababababaabaabbababbaaaaababaaaaaabaabaabbabaaababbbabbaaba", "a*aa*bb*ba*bbab***ba***baa**a*bbabb***a***ab**abbbb**aaaa**bba*bb**a*****a*b****aa**b**b*****aaaa*a**"))
    print(solution.isMatch(
        "babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab", "***bba**a*bbba**aab**b"))
    print(solution.isMatch("aa", "a"))
    print(solution.isMatch("aa", "*"))
    print(solution.isMatch("cb", "?a"))
