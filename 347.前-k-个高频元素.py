#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-07 07:59:04
LastEditors: Thomas Young
LastEditTime: 2020-09-07 08:06:58
'''
#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

# 示例 1:
# 输入: nums = [1, 1, 1, 2, 2, 3], k = 2
# 输出: [1, 2]

# 示例 2:
# 输入: nums = [1], k = 1
# 输出: [1]


# 提示：
# 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
# 你的算法的时间复杂度必须优于 O(n log n), n 是数组的大小。
# 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
# 你可以按任意顺序返回答案。

from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 偷懒的做法
        cnt = Counter(nums)
        return [num for num, _ in cnt.most_common(k)]
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
