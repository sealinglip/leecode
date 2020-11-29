#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-26 08:58:43
LastEditors: Thomas Young
LastEditTime: 2020-10-26 09:10:43
'''
#
# @lc app=leetcode.cn id=1365 lang=python3
#
# [1365] 有多少小于当前数字的数字
#
# 给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。
# 换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。
# 以数组形式返回答案。

# 示例 1：
# 输入：nums = [8, 1, 2, 2, 3]
# 输出：[4, 0, 1, 1, 3]
# 解释：
# 对于 nums[0] = 8 存在四个比它小的数字：（1，2，2 和 3）。
# 对于 nums[1] = 1 不存在比它小的数字。
# 对于 nums[2] = 2 存在一个比它小的数字：（1）。
# 对于 nums[3] = 2 存在一个比它小的数字：（1）。
# 对于 nums[4] = 3 存在三个比它小的数字：（1，2 和 2）。

# 示例 2：
# 输入：nums = [6, 5, 4, 8]
# 输出：[2, 1, 0, 3]

# 示例 3：
# 输入：nums = [7, 7, 7, 7]
# 输出：[0, 0, 0, 0]

# 提示：
# 2 <= nums.length <= 500
# 0 <= nums[i] <= 100

from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        counter = Counter(nums)
        keys = list(counter.keys())
        keys.sort()
        accum = 0
        accumDict = {}
        for key in keys:
            cnt = counter[key]
            accumDict[key] = accum
            accum += cnt

        res = []
        for num in nums:
            res.append(accumDict[num])

        return res

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
    print(solution.smallerNumbersThanCurrent([6, 5, 4, 8]))
    print(solution.smallerNumbersThanCurrent([7, 7, 7, 7]))
