#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2021-01-12 21:53:04
LastEditors: Thomas Young
LastEditTime: 2021-01-12 23:51:48
'''
#
# @lc app=leetcode.cn id=1203 lang=python3
#
# [1203] 项目管理
#
# 公司共有 n 个项目和  m 个小组，每个项目要不无人接手，要不就由 m 个小组之一负责。
# group[i] 表示第 i 个项目所属的小组，如果这个项目目前无人接手，那么 group[i] 就等于 - 1。
# （项目和小组都是从零开始编号的）小组可能存在没有接手任何项目的情况。

# 请你帮忙按要求安排这些项目的进度，并返回排序后的项目列表：

# 同一小组的项目，排序后在列表中彼此相邻。
# 项目之间存在一定的依赖关系，我们用一个列表 beforeItems 来表示，其中 beforeItems[i] 表示在进行第 i 个项目前（位于第 i 个项目左侧）应该完成的所有项目。
# 如果存在多个解决方案，只需要返回其中任意一个即可。如果没有合适的解决方案，就请返回一个 空列表 。

# 示例 1：
# 输入：n = 8, m = 2, group = [-1, -1, 1, 0, 0, 1, 0, -1], beforeItems = [[], [6], [5], [6], [3, 6], [], [], []]
# 输出：[6, 3, 4, 1, 5, 2, 0, 7]

# 示例 2：
# 输入：n = 8, m = 2, group = [-1, -1, 1, 0, 0, 1, 0, -1], beforeItems = [[], [6], [5], [6], [3], [], [4], []]
# 输出：[]
# 解释：与示例 1 大致相同，但是在排序后的列表中，4 必须放在 6 的前面。

# 提示：
# 1 <= m <= n <= 3 * 10^4
# group.length == beforeItems.length == n
# -1 <= group[i] <= m - 1
# 0 <= beforeItems[i].length <= n - 1
# 0 <= beforeItems[i][j] <= n - 1
# i != beforeItems[i][j]
# beforeItems[i] 不含重复元素


from typing import List
# @lc code=start
from collections import defaultdict
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        fakeGrp = m
        for i, grp in enumerate(group):
            if grp == -1:
                group[i] = fakeGrp
                fakeGrp += 1

        groupItems = defaultdict(list)
        depends = {} # 项目依赖关系
        grpDepends = {} # 组依赖关系
        grpDependSet = defaultdict(set)
        for i in range(n):
            groupItems[group[i]].append(i)
            grpDepends[group[i]] = grpDepends.get(group[i], 0)
            depends[i] = depends.get(i, 0)

            for dependency in beforeItems[i]:
                grp = group[dependency]
                if grp == group[i]: # 组内依赖关系
                    depends[dependency] = depends.get(dependency, 0) + 1 # 项目依赖dependency的数量加1
                elif grp not in grpDependSet[group[i]]:
                    grpDepends[grp] = grpDepends.get(grp, 0) + 1  # 组依赖dependency的数量加1
                    grpDependSet[group[i]].add(grp)
                    

        topologicGrpSort = []
        while grpDepends:
            zeroDepends = [key for key in grpDepends if grpDepends[key] == 0]
            if not zeroDepends: # 有环无解
                return []
            topologicGrpSort.extend(zeroDepends)
            for g in zeroDepends:
                for grpDependency in grpDependSet[g]:
                    grpDepends[grpDependency] = grpDepends.get(
                        grpDependency, 0) - 1
                grpDepends.pop(g)

        topologicGrpSort.reverse()
        
        res = []
        for grp in topologicGrpSort:
            items = groupItems[grp]
            topologicItemSort = []
            while items:
                zeroDepends = [
                    key for key in items if depends[key] == 0]  # 没有任何依赖的项目
                if not zeroDepends: # 有环无解
                    return []
                topologicItemSort.extend(zeroDepends)
                for d in zeroDepends:
                    for dependency in beforeItems[d]:
                        if group[dependency] == grp:  # 组内依赖关系
                            depends[dependency] = depends.get(dependency) - 1
                    items.remove(d)
            topologicItemSort.reverse()  # 按优先级从高到低排列的
            res.extend(topologicItemSort)

        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.sortItems(
        5, 3, [0, 0, 2, 1, 0], [[3], [], [], [], [1, 3, 2]]))
    print(solution.sortItems(
        8, 2, [-1, -1, 1, 0, 0, 1, 0, -1], [[], [6], [5], [6], [3, 6], [], [], []]))
    print(solution.sortItems(
        8, 2, [-1, -1, 1, 0, 0, 1, 0, -1], [[], [6], [5], [6], [3], [], [4], []]))
