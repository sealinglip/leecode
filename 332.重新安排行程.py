#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-08-27 08:49:44
LastEditors: Thomas Young
LastEditTime: 2020-09-23 23:07:37
'''
#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#
# 给定一个机票的字符串二维数组[from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。
# 所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。

# 说明:

# 如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。例如，行程["JFK", "LGA"] 与["JFK", "LGB"] 相比就更小，
# 排序更靠前。
# 所有的机场都用三个大写字母表示（机场代码）。
# 假定所有机票至少存在一种合理的行程。
# 示例 1:

# 输入: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# 输出: ["JFK", "MUC", "LHR", "SFO", "SJC"]

# 示例 2:

# 输入: [["JFK", "SFO"], ["JFK", "ATL"], [
#     "SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
# 输出: ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
# 解释: 另一种有效的行程是["JFK", "SFO", "ATL", "JFK", "ATL", "SFO"]。但是它自然排序更大更靠后。

from typing import List
# @lc code=start
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return []
        elif len(tickets) == 1:
            return tickets[0]
        
        t_dict = defaultdict(list) # key为出发地，value为该地出发的所有行程
        for departure, arrival in tickets:
            t_dict[departure].append(arrival)

        for departure in t_dict: # 将行程排序
            t_dict[departure].sort()

        # 从JFK开始遍历，出口
        itinerary = []
        def dfs(departure):
            while len(t_dict[departure]):
                arrival = t_dict[departure].pop(0)
                dfs(arrival)
            itinerary.append(departure)

        dfs('JFK')
        return itinerary[::-1]
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.findItinerary([["AXA","EZE"],["EZE","AUA"],["ADL","JFK"],["ADL","TIA"],["AUA","AXA"],["EZE","TIA"],["EZE","TIA"],["AXA","EZE"],["EZE","ADL"],["ANU","EZE"],["TIA","EZE"],["JFK","ADL"],["AUA","JFK"],["JFK","EZE"],["EZE","ANU"],["ADL","AUA"],["ANU","AXA"],["AXA","ADL"],["AUA","JFK"],["EZE","ADL"],["ANU","TIA"],["AUA","JFK"],["TIA","JFK"],["EZE","AUA"],["AXA","EZE"],["AUA","ANU"],["ADL","AXA"],["EZE","ADL"],["AUA","ANU"],["AXA","EZE"],["TIA","AUA"],["AXA","EZE"],["AUA","SYD"],["ADL","JFK"],["EZE","AUA"],["ADL","ANU"],["AUA","TIA"],["ADL","EZE"],["TIA","JFK"],["AXA","ANU"],["JFK","AXA"],["JFK","ADL"],["ADL","EZE"],["AXA","TIA"],["JFK","AUA"],["ADL","EZE"],["JFK","ADL"],["ADL","AXA"],["TIA","AUA"],["AXA","JFK"],["ADL","AUA"],["TIA","JFK"],["JFK","ADL"],["JFK","ADL"],["ANU","AXA"],["TIA","AXA"],["EZE","JFK"],["EZE","AXA"],["ADL","TIA"],["JFK","AUA"],["TIA","EZE"],["EZE","ADL"],["JFK","ANU"],["TIA","AUA"],["EZE","ADL"],["ADL","JFK"],["ANU","AXA"],["AUA","AXA"],["ANU","EZE"],["ADL","AXA"],["ANU","AXA"],["TIA","ADL"],["JFK","ADL"],["JFK","TIA"],["AUA","ADL"],["AUA","TIA"],["TIA","JFK"],["EZE","JFK"],["AUA","ADL"],["ADL","AUA"],["EZE","ANU"],["ADL","ANU"],["AUA","AXA"],["AXA","TIA"],["AXA","TIA"],["ADL","AXA"],["EZE","AXA"],["AXA","JFK"],["JFK","AUA"],["ANU","ADL"],["AXA","TIA"],["ANU","AUA"],["JFK","EZE"],["AXA","ADL"],["TIA","EZE"],["JFK","AXA"],["AXA","ADL"],["EZE","AUA"],["AXA","ANU"],["ADL","EZE"],["AUA","EZE"]]))
    print(solution.findItinerary([["EZE", "TIA"], ["EZE", "HBA"], ["AXA", "TIA"], ["JFK", "AXA"], ["ANU", "JFK"], ["ADL", "ANU"], ["TIA", "AUA"], ["ANU", "AUA"], ["ADL", "EZE"], [
          "ADL", "EZE"], ["EZE", "ADL"], ["AXA", "EZE"], ["AUA", "AXA"], ["JFK", "AXA"], ["AXA", "AUA"], ["AUA", "ADL"], ["ANU", "EZE"], ["TIA", "ADL"], ["EZE", "ANU"], ["AUA", "ANU"]]))
    print(solution.findItinerary([["EZE", "AXA"], ["TIA", "ANU"], ["ANU", "JFK"], ["JFK", "ANU"], [
          "ANU", "EZE"], ["TIA", "ANU"], ["AXA", "TIA"], ["TIA", "JFK"], ["ANU", "TIA"], ["JFK", "TIA"]]))
    print(solution.findItinerary(
        [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
    print(solution.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], [
          "SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
