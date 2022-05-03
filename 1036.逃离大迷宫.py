#
# @lc app=leetcode.cn id=1036 lang=python3
#
# [1036] 逃离大迷宫
#
# 在一个 10^6 x 10^6 的网格中，每个网格上方格的坐标为 (x, y) 。

# 现在从源方格 source = [sx, sy] 开始出发，意图赶往目标方格 target = [tx, ty] 。数组 blocked 是封锁的方格列表，其中每个 blocked[i] = [xi, yi] 表示坐标为(xi, yi) 的方格是禁止通行的。

# 每次移动，都可以走到网格中在四个方向上相邻的方格，只要该方格 不 在给出的封锁列表 blocked 上。同时，不允许走出网格。

# 只有在可以通过一系列的移动从源方格 source 到达目标方格 target 时才返回 true。否则，返回 false。


# 示例 1：
# 输入：blocked = [[0, 1], [1, 0]], source = [0, 0], target = [0, 2]
# 输出：false
# 解释：
# 从源方格无法到达目标方格，因为我们无法在网格中移动。
# 无法向北或者向东移动是因为方格禁止通行。
# 无法向南或者向西移动是因为不能走出网格。

# 示例 2：
# 输入：blocked = [], source = [0, 0], target = [999999, 999999]
# 输出：true
# 解释：
# 因为没有方格被封锁，所以一定可以到达目标方格。
#  

# 提示：
# 0 <= blocked.length <= 200
# blocked[i].length == 2
# 0 <= xi, yi < 10^6
# source.length == target.length == 2
# 0 <= sx, sy, tx, ty < 10^6
# source != target
# 题目数据保证 source 和 target 不在封锁列表内

# Hard

from typing import List, Tuple
# @lc code=start
from collections import deque

DIRS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
DIM = 10 ** 6


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked:
            return True

        L = len(blocked)
        LIMIT = L * (L - 1) // 2  # BFS的退出阈值

        blocked = set(tuple(p) for p in blocked)  # 便于查找

        def search(s: Tuple[int], t: Tuple[int]) -> int:
            q = deque()
            q.append(s)
            visited = set()
            visited.add(s)

            visitCnt = 1
            while q and visitCnt <= LIMIT:
                p = q.popleft()

                for deltaX, deltaY in DIRS:
                    p1 = (p[0] + deltaX, p[1] + deltaY)
                    if p1 == t:
                        return 1
                    if 0 <= p1[0] < DIM and 0 <= p1[1] < DIM and p1 not in visited and p1 not in blocked:
                        q.append(p1)
                        visited.add(p1)
                        visitCnt += 1

            if q:
                return 0  # s没有被围住，但不确定是否能达到t
            else:
                return -1  # s被围住了

        if (res := search(tuple(source), tuple(target))) == 1:
            return True
        elif res == -1:
            return False
        elif search(tuple(target), tuple(source)) == -1:
            return False
        else:
            return True

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.isEscapePossible(
        [[100059, 100063], [100060, 100064], [100061, 100065], [100062, 100066], [100063, 100067], [100064, 100068], [100065, 100069], [100066, 100070], [100067, 100071], [100068, 100072], [100069, 100073], [100070, 100074], [100071, 100075], [100072, 100076], [100073, 100077], [100074, 100078], [100075, 100079], [100076, 100080], [100077, 100081], [100078, 100082], [100079, 100083], [100080, 100082], [100081, 100081], [100082, 100080], [100083, 100079], [100084, 100078], [100085, 100077], [100086, 100076], [100087, 100075], [100088, 100074], [100089, 100073], [100090, 100072], [100091, 100071], [100092, 100070], [100093, 100069], [100094, 100068], [100095, 100067], [100096, 100066], [100097, 100065], [100098, 100064], [
            100099, 100063], [100098, 100062], [100097, 100061], [100096, 100060], [100095, 100059], [100094, 100058], [100093, 100057], [100092, 100056], [100091, 100055], [100090, 100054], [100089, 100053], [100088, 100052], [100087, 100051], [100086, 100050], [100085, 100049], [100084, 100048], [100083, 100047], [100082, 100046], [100081, 100045], [100080, 100044], [100079, 100043], [100078, 100044], [100077, 100045], [100076, 100046], [100075, 100047], [100074, 100048], [100073, 100049], [100072, 100050], [100071, 100051], [100070, 100052], [100069, 100053], [100068, 100054], [100067, 100055], [100066, 100056], [100065, 100057], [100064, 100058], [100063, 100059], [100062, 100060], [100061, 100061], [100060, 100062]],
        [100079, 100063], [999948, 999967]))  # False
    print(solution.isEscapePossible(
        [[0, 1], [1, 0]], [0, 0], [0, 2]))  # False
    print(solution.isEscapePossible([], [0, 0], [999999, 999999]))  # True
