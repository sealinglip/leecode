#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-12 21:06:49
@LastEditors: Thomas Young
@LastEditTime: 2020-07-05 19:22:45
'''
#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

# 示例:

# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# @lc code=start
from typing import Dict

class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0

        resultCache = [0 for i in range(n + 1)] #第0个元素不用，其他元素保存对应的结果
        def getNumTrees(n: int, resultCache: Dict) -> int:
            if n <= 1:
                return 1

            if resultCache[n]:
                return resultCache[n]

            num = 0
            # 状态转移 f(n) = Sigma(i from 0 ~ n-1) f(i)f(n-i-1)
            for i in range(n):
                num += getNumTrees(i, resultCache) * \
                    getNumTrees(n - i - 1, resultCache)

            resultCache[n] = num
            return num
        return getNumTrees(n, resultCache)

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.numTrees(4))
    print(solution.numTrees(17))
