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
# 给你一个字符串 S、一个字符串 T 。请你设计一种算法，可以在 O(n) 的时间复杂度内，
# 从字符串 S 里面找出：包含 T 所有字符的最小子串。

# 示例：
# 输入：S = "ADOBECODEBANC", T = "ABC"
# 输出："BANC"

# 提示：
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。

# @lc code=start
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        cnt = Counter(t) # 目标计数
        l = len(s) # 字符串长度
        lb = 0
        rb = 1
        minWin = None
        # accum = Counter() # 累计计数 
        requirement = len(t) # 换一种判断是否满足要求的方法
        while rb <= l:
            c = s[rb - 1]
            # accum.update(c)
            if c in cnt:
                if cnt[c] > 0:
                    requirement -= 1
                cnt.subtract(c)
            # if all([accum[c] >= cnt[c] for c in cnt]): # 满足要求
            if requirement == 0: # 满足要求
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
            rb += 1 # 右边界右移
        
        return minWin if minWin else ""

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minWindow("ADOBECODEBANC", "ABC"))
