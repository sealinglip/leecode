#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-04 09:10:28
LastEditors: Thomas Young
LastEditTime: 2020-10-06 07:31:04
'''
#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#
# 格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
# 给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。即使有多个不同答案，
# 你也只需要返回其中一种。

# 格雷编码序列必须以 0 开头。

# 示例 1:
# 输入: 2
# 输出: [0, 1, 3, 2]
# 解释:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2

# 对于给定的 n，其格雷编码序列并不唯一。
# 例如，[0, 2, 3, 1] 也是一个有效的格雷编码序列。

# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1

# 示例 2:
# 输入: 0
# 输出: [0]
# 解释: 我们定义格雷编码序列必须以 0 开头。
# 给定编码总位数为 n 的格雷编码序列，其长度为 2^n。当 n = 0 时，长度为 2^0 = 1。
# 因此，当 n = 0 时，其格雷编码序列为[0]。

from typing import List
# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        # 流氓手段
        return [i ^ i >> 1 for i in range(2 ** n)]
    
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.grayCode())
