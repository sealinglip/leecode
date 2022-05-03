#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-14 17:43:32
@LastEditors: Thomas Young
@LastEditTime: 2020-06-14 20:30:36
'''
#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。


# 示例 1：

# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
# 示例 2：

# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
# 示例 3：

# 输入：s = ""
# 输出：0


# 提示：

# 0 <= s.length <= 3 * 10^4
# s[i] 为 '(' 或 ')'

# Hard
# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        '''
        用delta来记录，从文本开头到当前位置（含），累计左括号数减右括号数，
        这样可以建立一个delta和索引的映射，同样的delta，我们只保存最小的索
        引，这样拿当前位置减掉同delta的最小索引，得到有效子串长度
        '''
        if not s:
            return 0

        delta, deltaMap, maxLen = 0, {0: -1}, 0  # 记录偏差值、偏差值对照表、当前最大子串长度
        for i, c in enumerate(s):
            if c == '(':
                delta += 1
            elif c == ')':
                delta -= 1
            # 从deltaMap中清除比delta大的key
            keyToRemove = [k for k in deltaMap.keys() if k > delta]
            for k in keyToRemove:
                del deltaMap[k]

            if delta in deltaMap:
                l = i - deltaMap[delta]
                if l > maxLen:
                    maxLen = l
            else:
                deltaMap[delta] = i

        return maxLen
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestValidParentheses("()(()"))
    print(solution.longestValidParentheses("()"))
    print(solution.longestValidParentheses("(()"))
    print(solution.longestValidParentheses(")()())"))
    print(solution.longestValidParentheses(")()())(()((()))())"))
