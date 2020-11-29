#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-01 09:01:45
LastEditors: Thomas Young
LastEditTime: 2020-09-01 09:32:21
'''
#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

# 示例:

# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#     ["ate", "eat", "tea"],
#     ["nat", "tan"],
#     ["bat"]
# ]
# 说明：
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。

from typing import List
# @lc code=start
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
            
        group = defaultdict(list)
        for s in strs:
            h = tuple(sorted(s))
            group[h].append(s)
        
        return list(group.values())
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
