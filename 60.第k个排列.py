#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-05 21:34:14
LastEditors: Thomas Young
LastEditTime: 2020-09-05 22:28:03
'''
#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#
# 给出集合[1, 2, 3, …, n]，其所有元素共有 n! 种排列。

# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 给定 n 和 k，返回第 k 个排列。

# 说明：
# 给定 n 的范围是[1, 9]。
# 给定 k 的范围是[1,  n!]。

# 示例 1:
# 输入: n = 3, k = 3
# 输出: "213"

# 示例 2:
# 输入: n = 4, k = 9
# 输出: "2314"

# 提示：
# 1 <= n <= 9
# 1 <= k <= n!

# Hard
# @lc code=start


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # n位数，固定前几位，后面的m位数字共有m!种可能
        rank = [1] * n
        for i in range(1, n):
            rank[i] = rank[i - 1] * i
        rank = rank[::-1]  # 倒转数组

        used = [False] * n  # 数字已使用情况

        def getNthDigit(nth: int) -> str:
            '''
            获取从小到大的第N个数字
            '''
            i, c = 0, -1
            while i < n:
                if not used[i]:
                    c += 1
                    if c == nth:
                        used[i] = True
                        return str(i + 1)
                i += 1
            else:
                return ""  # 不应该到这

        digits = []
        k -= 1  # 换成以0为基
        for i in range(n):
            if k < rank[i]:
                digits.append(getNthDigit(0))
            else:
                nth = k // rank[i]
                digits.append(getNthDigit(nth))
                k -= nth * rank[i]

        return "".join(digits)

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.getPermutation(3, 3))
    print(solution.getPermutation(4, 9))
