#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-02 09:30:50
LastEditors: Thomas Young
LastEditTime: 2020-11-04 08:12:49
'''
#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。


# 示例 1：
# 输入：intervals = [[1, 3], [6, 9]], newInterval = [2, 5]
# 输出：[[1, 5], [6, 9]]

# 示例 2：
# 输入：intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval = [4, 8]
# 输出：[[1, 2], [3, 10], [12, 16]]
# 解释：这是因为新的区间[4, 8] 与[3, 5], [6, 7], [8, 10] 重叠。

# 示例 3：
# 输入：intervals = [], newInterval = [5, 7]
# 输出：[[5, 7]]

# 示例 4：
# 输入：intervals = [[1, 5]], newInterval = [2, 3]
# 输出：[[1, 5]]

# 示例 5：
# 输入：intervals = [[1, 5]], newInterval = [2, 7]
# 输出：[[1, 7]]


# 提示：
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= intervals[i][0] <= intervals[i][1] <= 10^5
# intervals 根据 intervals[i][0] 按 升序 排列
# newInterval.length == 2
# 0 <= newInterval[0] <= newInterval[1] <= 10^5

from typing import List
# @lc code=start


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        idx, curLb, curUb = 0, float('-inf'), float('-inf')
        nLb, nUb = newInterval
        state = 0  # 新区间上下界都未完成合并
        while idx < len(intervals) and state < 2:
            # 先定位到要插入的位置
            nextLb, nextUb = intervals[idx]
            if state > 0:
                if nUb < nextLb:
                    state = 2
                    break
                else:
                    intervals[idx - 1][1] = nUb if nUb >= nextUb else nextUb
                    del intervals[idx]
                    continue
            elif nLb >= curLb and nLb < nextLb:
                if nLb <= curUb:
                    if nUb <= curUb:  # 完全被包含了
                        state = 2
                        break  # 直接搞定了
                    else:
                        intervals[idx - 1][1] = nUb if (nUb <
                                                        nextLb or nUb >= nextUb) else nextUb
                        if nUb >= nextLb:
                            del intervals[idx]
                            state = 1  # 下界完成了合并
                            continue
                        else:
                            state = 2
                            break  # 直接搞定了
                elif nUb >= nextLb:
                    intervals[idx][0] = nLb
                    state = 1  # 完成下界合并
                    if nUb <= nextUb:
                        state = 2
                        break  # 直接搞定了
                    else:
                        intervals[idx][1] = nUb
                else:
                    intervals.insert(idx, newInterval)
                    state = 2
                    break  # 直接搞定了

            curLb, curUb = intervals[idx]
            idx += 1

        if state == 0:
            if curUb < nLb:  # 不搭
                intervals.append(newInterval)
            elif curUb < nUb:
                intervals[-1][1] = nUb

        return intervals
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.insert([[0, 5], [8, 9]], [2, 4]))
    print(solution.insert([[1, 5]], [2, 7]))
    print(solution.insert([[1, 5]], [2, 3]))
    print(solution.insert([[1, 2]], [5, 7]))
    # print(solution.insert([[1, 3], [6, 9]], [2, 5]))
    # print(solution.insert([[3, 5], [6, 9]], [1, 2]))
    # print(solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
