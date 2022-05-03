#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-12 07:50:49
@LastEditors: Thomas Young
@LastEditTime: 2020-06-20 12:30:31
'''
#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。


# 示例 1：
# 输入：s = "aa", p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。

# 示例 2:
# 输入：s = "aa", p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

# 示例 3：
# 输入：s = "ab", p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。


# 提示：
# 1 <= s.length <= 20
# 1 <= p.length <= 30
# s 只包含从 a-z 的小写字母。
# p 只包含从 a-z 的小写字母，以及字符 . 和 *。
# 保证每次出现字符 * 时，前面都匹配到有效的字符

# Hard
# @lc code=start
from typing import Dict


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == p:
            return True
        elif not p:  # p为空而s不为空
            return False

        # 方法2 回溯
        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0
        asterisk_stack = []

        while s_idx < s_len:
            if p_idx < p_len:
                c, next_c = p[p_idx], p[p_idx +
                                        1] if p_idx < p_len - 1 else None
                if next_c == '*':  # 后一个是*
                    p_idx += 2
                    if c in [s[s_idx], '.']:
                        asterisk_stack.append([p_idx, c, s_idx])
                    continue
                elif c in [s[s_idx], '.']:
                    s_idx += 1
                    p_idx += 1
                    continue

            if not asterisk_stack:
                return False
            else:
                asterisk_idx, pre_c, s_tmp_idx = asterisk_stack[-1]
                if pre_c in [s[s_tmp_idx], '.']:
                    p_idx = asterisk_idx
                    s_idx = s_tmp_idx + 1
                    asterisk_stack[-1][2] = s_idx
                else:
                    asterisk_stack.pop()

        # 剩下的字符串中，奇数索引处都是*
        return not ((p_len - p_idx) & 1) and all(x == '*' for x in p[p_idx + 1::2])

        # 方法1
        # cache = {} #局部匹配结果缓存
        # return self.matchPart(s, 0, p, 0, cache)

    def matchPart(self, s: str, sIdx: int, p: str, pIdx: int, cache: Dict) -> bool:
        '''
        方法1
        '''
        if pIdx == len(p):  # 模式中没有剩余
            return sIdx == len(s)  # 源串也应该没有才能匹配

        key = (sIdx, pIdx)
        if key in cache:
            return cache[key]

        curP = p[pIdx]
        followByAsterisk = pIdx < len(p) - 1 and p[pIdx + 1] == '*'
        match = False
        if followByAsterisk:  # 有通配符
            # greedy
            i = sIdx
            while i < len(s) and (curP == '.' or curP == s[i]):
                i += 1
            pIdx += 2
            match = self.matchPart(s, i, p, pIdx, cache)
            while not match and i > sIdx:
                i -= 1
                match = self.matchPart(s, i, p, pIdx, cache)
        elif sIdx < len(s) and (curP == '.' or curP == s[sIdx]):
            match = self.matchPart(s, sIdx + 1, p, pIdx + 1, cache)

        cache[key] = match
        return match

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.isMatch("acbbcbcbcbaaacaac", "ac*.a*ac*.*ab*b*ac"))
    print(solution.isMatch("aa", "a"))
    print(solution.isMatch("", "a*"))
    print(solution.isMatch("aaa", "ab*a*c*a"))
    print(solution.isMatch("aabc", "a*bc"))
    print(solution.isMatch("aabbc", "a*.*c"))
    print(solution.isMatch("aabdbc", "a*.*c"))
    print(solution.isMatch("aabdbc", "a*.*cd"))
