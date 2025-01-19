#
# @lc app=leetcode.cn id=1847 lang=python3
#
# [1847] 最近的房间
#
# 一个酒店里有 n 个房间，这些房间用二维整数数组 rooms 表示，其中 rooms[i] = [roomIdi, sizei] 表示有一个房间号为 roomIdi 的房间且它的面积为 sizei 。每一个房间号 roomIdi 保证是 独一无二 的。

# 同时给你 k 个查询，用二维数组 queries 表示，其中 queries[j] = [preferredj, minSizej] 。第 j 个查询的答案是满足如下条件的房间 id ：

# 房间的面积 至少 为 minSizej ，且
# abs(id - preferredj) 的值 最小 ，其中 abs(x) 是 x 的绝对值。
# 如果差的绝对值有 相等 的，选择 最小 的 id 。如果 没有满足条件的房间 ，答案为 -1 。

# 请你返回长度为 k 的数组 answer ，其中 answer[j] 为第 j 个查询的结果。


# 示例 1：
# 输入：rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]
# 输出：[3,-1,3]
# 解释：查询的答案如下：
# 查询 [3,1] ：房间 3 的面积为 2 ，大于等于 1 ，且号码是最接近 3 的，为 abs(3 - 3) = 0 ，所以答案为 3 。
# 查询 [3,3] ：没有房间的面积至少为 3 ，所以答案为 -1 。
# 查询 [5,2] ：房间 3 的面积为 2 ，大于等于 2 ，且号码是最接近 5 的，为 abs(3 - 5) = 2 ，所以答案为 3 。

# 示例 2：
# 输入：rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]]
# 输出：[2,1,3]
# 解释：查询的答案如下：
# 查询 [2,3] ：房间 2 的面积为 3 ，大于等于 3 ，且号码是最接近的，为 abs(2 - 2) = 0 ，所以答案为 2 。
# 查询 [2,4] ：房间 1 和 3 的面积都至少为 4 ，答案为 1 因为它房间编号更小。
# 查询 [2,5] ：房间 3 是唯一面积大于等于 5 的，所以答案为 3 。
 

# 提示：
# n == rooms.length
# 1 <= n <= 10^5
# k == queries.length
# 1 <= k <= 10^4
# 1 <= roomIdi, preferredj <= 10^7
# 1 <= sizei, minSizej <= 10^7

# Hard
# 复习

from typing import List

import sortedcontainers
# @lc code=start

class Event:
    """
    op: 事件的类型，0 表示房间，1 表示询问
    size: 房间的 size 或者询问的 minSize
    idx: 房间的 roomId 或者询问的 preferred
    origin: 房间在数组 room 中的原始编号或者询问在数组 queries 中的原始编号
    """
    def __init__(self, op: int, size: int, idx: int, origin: int):
        self.op = op
        self.size = size
        self.idx = idx
        self.origin = origin

    """
    自定义比较函数，按照事件的 size 降序排序
    如果 size 相同，优先考虑房间
    """
    def __lt__(self, other: "Event") -> bool:
        return self.size > other.size or (self.size == other.size and self.op < other.op)
    
class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(queries)

        events = list()
        for i, (roomId, size) in enumerate(rooms):
            # 房间事件
            events.append(Event(0, size, roomId, i))

        for i, (minSize, preferred) in enumerate(queries):
            # 询问事件
            events.append(Event(1, preferred, minSize, i))

        events.sort()

        ans = [-1] * n
        # 存储房间 roomId 的有序集合
        # 需要导入 sortedcontainers 库
        valid = sortedcontainers.SortedList()
        for event in events:
            if event.op == 0:
                # 房间事件，将 roomId 加入有序集合
                valid.add(event.idx)
            else:
                # 询问事件
                dist = float("inf")
                # 查找最小的大于等于 preferred 的元素
                x = valid.bisect_left(event.idx)
                if x != len(valid) and valid[x] - event.idx < dist:
                    dist = valid[x] - event.idx
                    ans[event.origin] = valid[x]
                if x != 0:
                    # 查找最大的严格小于 preferred 的元素
                    x -= 1
                    if event.idx - valid[x] <= dist:
                        dist = event.idx - valid[x]
                        ans[event.origin] = valid[x]
            
        return ans
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.closestRoom([[2,2],[1,2],[3,2]], [[3,1],[3,3],[5,2]])) # [3,-1,3]
    print(solution.closestRoom([[1,4],[2,3],[3,5],[4,1],[5,2]], [[2,3],[2,4],[2,5]])) # [2,1,3]

