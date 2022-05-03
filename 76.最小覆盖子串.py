#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-15 07:56:26
LastEditors: Thomas Young
LastEditTime: 2020-09-20 09:24:32
'''
#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。


# 注意：

# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。


# 示例 1：
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"

# 示例 2：
# 输入：s = "a", t = "a"
# 输出："a"

# 示例 3:
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。

# 提示：
# 1 <= s.length, t.length <= 10^5
# s 和 t 由英文字母组成


# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？

# Hard
# @lc code=start
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        cnt = Counter(t)  # 目标计数
        l = len(s)  # 字符串长度
        lb = 0
        rb = 1
        minWin = None
        # accum = Counter() # 累计计数
        requirement = len(t)  # 换一种判断是否满足要求的方法
        while rb <= l:
            c = s[rb - 1]
            # accum.update(c)
            if c in cnt:
                if cnt[c] > 0:
                    requirement -= 1
                cnt.subtract(c)
            # if all([accum[c] >= cnt[c] for c in cnt]): # 满足要求
            if requirement == 0:  # 满足要求
                while lb < rb:
                    if minWin is None or rb - lb < len(minWin):
                        minWin = s[lb:rb]
                    c = s[lb]
                    # accum.subtract(c)
                    if c in cnt:
                        if cnt[c] >= 0:
                            requirement += 1
                        cnt.update(c)

                    lb += 1  # 左边界右移
                    # if not all([accum[c] >= cnt[c] for c in cnt]):  # 不满足要求
                    if requirement:  # 不满足要求
                        break
            rb += 1  # 右边界右移

        return minWin if minWin else ""

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.minWindow("ADOBECODEBANC", "ABC"))
