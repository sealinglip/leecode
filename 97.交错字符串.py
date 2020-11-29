#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-23 22:05:33
LastEditors: Thomas Young
LastEditTime: 2020-10-25 21:32:59
'''
#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#
# 给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

# 示例 1：
# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出：true

# 示例 2：
# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出：false

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1:
            return s2 == s3
        elif not s2:
            return s1 == s3
        elif not s3 or len(s1) + len(s2) != len(s3):
            return False

        l1, l2 = len(s1), len(s2)
        # 动态规划
        # 倒着来看s3的构成
        # 用dp(p1, p2)来表示s1[p1:]和s2[p2:]是否能交错组成s3[p1+p2:]
        # dp(p1, p2) = True if p1 == l1 and p2 == l2
        #            = s1[p1:] == s3[p1+p2:] if p2 == l2
        #            = s2[p2:] == s3[p1+p2:] if p1 == l1
        #            = any(s1[p1:p1'] == s3[p1+p2:p1'+p2] and dp(p1', p2))  0 <= p1 < p1' < l1
        #            or any(s2[p2:p2'] == s3[p1+p2:p1+p2'] and dp(p1, p2'))  0 <= p2 < p2' < l2
        # 求dp(0, 0)
        dp = {}
        def getDp(p1: int, p2: int) -> bool:
            key = (p1, p2)
            if key in dp:
                return dp[key]
            res = False
            if p1 == l1 and p2 == l2:
                res = True
            elif p1 == l1:
                res = s2[p2:] == s3[p1+p2:]
            elif p2 == l2:
                res = s1[p1:] == s3[p1+p2:]
            else:
                for i in range(p1 + 1, l1 + 1):
                    if s1[p1:i] == s3[p1+p2:i+p2] and getDp(i, p2):
                        res = True
                        break
                else:
                    for i in range(p2 + 1, l2 + 1):
                        if s2[p2:i] == s3[p1+p2:p1+i] and getDp(p1, i):
                            res = True
                            break
            dp[key] = res
            return res

        return getDp(0, 0)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
    print(solution.isInterleave("aabcc", "dbbca", "aadbbbaccc"))
