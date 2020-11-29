#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-08-31 09:22:38
LastEditors: Thomas Young
LastEditTime: 2020-09-01 08:17:14
'''
#
# @lc app=leetcode.cn id=841 lang=python3
#
# [841] 钥匙和房间
#
# 有 N 个房间，开始时你位于 0 号房间。每个房间有不同的号码：0，1，2，...，N-1，并且房间里可能有一些钥匙能使你进入下一个房间。
# 在形式上，对于每个房间 i 都有一个钥匙列表 rooms[i]，每个钥匙 rooms[i][j] 由[0, 1，...，N-1] 中的一个整数表示，其中 
# N = rooms.length。 钥匙 rooms[i][j] = v 可以打开编号为 v 的房间。

# 最初，除 0 号房间外的其余所有房间都被锁住。
# 你可以自由地在房间之间来回走动。
# 如果能进入每个房间返回 true，否则返回 false。

# 示例 1：
# 输入: [[1], [2], [3], []]
# 输出: true
# 解释:
# 我们从 0 号房间开始，拿到钥匙 1。
# 之后我们去 1 号房间，拿到钥匙 2。
# 然后我们去 2 号房间，拿到钥匙 3。
# 最后我们去了 3 号房间。
# 由于我们能够进入每个房间，我们返回 true。

# 示例 2：
# 输入：[[1, 3], [3, 0, 1], [2], [0]]
# 输出：false
# 解释：我们不能进入 2 号房间。
# 提示：
# 1 <= rooms.length <= 1000
# 0 <= rooms[i].length <= 1000
# 所有房间中的钥匙数量总计不超过 3000。

from typing import List
# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return True
        
        N = len(rooms) # 房间数
        visit = [False] * N # 标记是否可以获取某房间的KEY
        keys = [0]  # 待处理的🔑栈，0号房间无锁，相当于已经拿到钥匙
        while keys:
            key = keys.pop() # 拿到下一个钥匙
            if visit[key]: # 已经访问过该房间了
                continue
            else:
                keys.extend(rooms[key]) # 将对应房间内的🔑入栈
                visit[key] = True

        return all(visit)

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.canVisitAllRooms([[1], [2], [3], []]))
    print(solution.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))

