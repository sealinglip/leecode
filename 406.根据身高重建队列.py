#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-11-16 08:43:44
LastEditors: Thomas Young
LastEditTime: 2020-11-16 13:33:49
'''
#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#
# 假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，
# k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

# 注意：
# 总人数少于1100人。

# 示例
# 输入:
# [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
# 输出:
# [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]

from typing import List
# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return people
        
        L = len(people)
        people.sort(key = lambda p: p[0] * 10000 - p[1]) # 按h升序，k降序排列
        res = [None] * L
        availPos = [i for i in range(L)]
        for p in people:
            pos = availPos[p[1]]
            res[pos] = p
            del availPos[p[1]]

        return res


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.reconstructQueue(
        [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
