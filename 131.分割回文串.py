#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-11-08 17:44:50
LastEditors: Thomas Young
LastEditTime: 2020-11-08 21:43:01
'''
#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

# 返回 s 所有可能的分割方案。

# 示例:
# 输入: "aab"
# 输出:
# [
#     ["aa", "b"],
#     ["a", "a", "b"]
# ]

from typing import List
# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
            
        N = len(s)
        if N == 1:
            return [[s]]

        # 记res[i] 为partition(s[:i+1])的结果（即前i+1个字符的结果）
        # 那么res[i+1] = [
        #   r + [s[i+1]] for r in res #上一步的结果加上新字符
        #   r[0:-1] + [r[-1]+s[i+1]] for r in res if r[-1] == s[i+1] # 上一步的结果中最后一个元素等于新字符的，直接修改最后一个元素为叠字
        #   r[0:-2] + [r[-2]+r[-1]+s[i+1]] for r in res if len(r) > 1 and r[-2] == s[i+1] # 上一步的结果中倒数第二个元素等于新字符的，拼接后两个元素加新字符得新的最后一个元素
        # ]
        res = [[s[0]]]
        for i in range(1, N):
            newRes = []
            for r in res:
                newRes.append(r + [s[i]])
                if r[-1] == s[i]:
                    newRes.append(r[:-1] + [r[-1] + s[i]])
                if len(r) > 1 and r[-2] == s[i]:
                    newRes.append(r[:-2] + [r[-2] + r[-1] + s[i]])
            res = newRes

        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.partition("aab"))
