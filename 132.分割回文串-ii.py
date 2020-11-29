#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-11-08 21:43:37
LastEditors: Thomas Young
LastEditTime: 2020-11-08 22:32:37
'''
#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

# 返回符合要求的最少分割次数。

# 示例:
# 输入: "aab"
# 输出: 1
# 解释: 进行一次分割就可将 s 分割成["aa", "b"] 这样两个回文子串。

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        if not s:
            return 0

        N = len(s)
        if N == 1:
            return 0

        # 预处理
        # 记dp[i][j]代表s[i:j+1]是否回文串
        dp =[[True if i == j else False for j in range(N)] for i in range(N)]
        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                dp[i][j] = s[i] == s[j] and (j == i + 1 or dp[i + 1][j - 1])
        
        # 记ans[i]代表s[0:i]的最小分隔数
        # 状态转移方程为ans[j] = min(ans[i] + 1 if dp[i][j-1])
        ans = [-1]
        for j in range(1, N+1):
            minCut = j
            for i in range(j):
                if dp[i][j-1]:
                    cut = ans[i] + 1
                    if cut < minCut:
                        minCut = cut
            ans.append(minCut)
        
        return ans[-1]
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minCut("aab"))
