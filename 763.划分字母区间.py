#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-22 11:26:15
LastEditors: Thomas Young
LastEditTime: 2020-10-22 12:58:08
'''
#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#
# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。
# 返回一个表示每个字符串片段的长度的列表。

# 示例 1：
# 输入：S = "ababcbacadefegdehijhklij"
# 输出：[9, 7, 8]
# 解释：
# 划分结果为 "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。

# 提示：
# S的长度在[1, 500]之间。
# S只包含小写字母 'a' 到 'z' 。

from typing import List
# @lc code=start
from collections import defaultdict
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return []
        
        regionDict = defaultdict(list) # 每个字符对应的起止区间（闭区间）
        for i, c in enumerate(S):
            region = regionDict[c]
            if len(region) < 2:
                region.append(i)
            else:
                region[-1] = i

        # 对region根据起始位置进行排序
        regions = list(regionDict.values())
        regions.sort(key=lambda region: region[0])

        res = []
        prevRegion = None
        for region in regions:
            if prevRegion:
                if region[0] > prevRegion[-1]: # 前面的可以是一个独立的片段
                    res.append(prevRegion[-1] - prevRegion[0] + 1)
                    prevRegion = region
                else:
                    prevRegion[-1] = max(prevRegion[-1], region[-1])
            else:
                prevRegion = region
        res.append(prevRegion[-1] - prevRegion[0] + 1)
        return res

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.partitionLabels("ababcbacadefegdehijhklij"))
