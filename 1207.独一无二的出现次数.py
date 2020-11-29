#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-28 08:35:32
LastEditors: Thomas Young
LastEditTime: 2020-10-28 08:40:32
'''
#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#
# 给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。

# 如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。

# 示例 1：
# 输入：arr = [1, 2, 2, 1, 1, 3]
# 输出：true
# 解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。

# 示例 2：
# 输入：arr = [1, 2]
# 输出：false

# 示例 3：
# 输入：arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
# 输出：true

# 提示：
# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000

from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        if not arr:
            return True

        cntStat = Counter(arr)
        cntSet = set()
        for num in cntStat:
            cnt = cntStat[num]
            if cnt in cntSet:
                return False
            else:
                cntSet.add(cnt)

        return True
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.uniqueOccurrences([1, 2, 2, 1, 1, 3]))
    print(solution.uniqueOccurrences([1, 2]))
    print(solution.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
