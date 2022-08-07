#
# @lc app=leetcode.cn id=749 lang=python3
#
# [749] 隔离病毒
#
# 病毒扩散得很快，现在你的任务是尽可能地通过安装防火墙来隔离病毒。

# 假设世界由 m x n 的二维矩阵 isInfected 组成， isInfected[i][j] == 0 表示该区域未感染病毒，而  isInfected[i][j] == 1 表示该区域已感染病毒。可以在任意 2 个相邻单元之间的共享边界上安装一个防火墙（并且只有一个防火墙）。

# 每天晚上，病毒会从被感染区域向相邻未感染区域扩散，除非被防火墙隔离。现由于资源有限，每天你只能安装一系列防火墙来隔离其中一个被病毒感染的区域（一个区域或连续的一片区域），且该感染区域对未感染区域的威胁最大且 保证唯一 。

# 你需要努力使得最后有部分区域不被病毒感染，如果可以成功，那么返回需要使用的防火墙个数; 如果无法实现，则返回在世界被病毒全部感染时已安装的防火墙个数。


# 示例 1：
# 输入: isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
# 输出: 10
# 解释:一共有两块被病毒感染的区域。
# 在第一天，添加 5 墙隔离病毒区域的左侧。病毒传播后的状态是:

# 第二天，在右侧添加 5 个墙来隔离病毒区域。此时病毒已经被完全控制住了。

# 示例 2：
# 输入: isInfected = [[1,1,1],[1,0,1],[1,1,1]]
# 输出: 4
# 解释: 虽然只保存了一个小区域，但却有四面墙。
# 注意，防火墙只建立在两个不同区域的共享边界上。

# 示例 3:
# 输入: isInfected = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
# 输出: 13
# 解释: 在隔离右边感染区域后，隔离左边病毒区域只需要 2 个防火墙。


# 提示:
# m == isInfected.length
# n == isInfected[i].length
# 1 <= m, n <= 50
# isInfected[i][j] is either 0 or 1
# 在整个描述的过程中，总有一个相邻的病毒区域，它将在下一轮 严格地感染更多未受污染的方块

# Hard
# 复习

from typing import List, Set, Tuple
from collections import deque
# @lc code=start


class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        DIR = ((1, 0), (-1, 0), (0, 1), (0, -1))
        m, n = len(isInfected), len(isInfected[0])  # 得到整个区域的尺寸
        # vis = [[False] * n for _ in range(m)] # 记录访问状态

        def bfs(r: int, c: int, s1: Set[Tuple[int]], s2: Set[Tuple[int]], vis: List[List[bool]]) -> int:
            '''
            广度优先遍历(r, c)所在点对应感染区域当前的感染区域和下一步的扩散区域，返回围堵这一区域需要的防火墙数量
            '''
            res = 0
            s1.add((r, c))
            dq = deque(s1)
            vis[r][c] = True
            while dq:
                r1, c1 = dq.popleft()
                for dr, dc in DIR:
                    nr, nc = r1 + dr, c1 + dc
                    if 0 <= nr < m and 0 <= nc < n and not vis[nr][nc]:
                        # 在区域内且未访问过
                        if isInfected[nr][nc] == 1:
                            s1.add((nr, nc))
                            vis[nr][nc] = True
                            dq.append((nr, nc))
                        elif isInfected[nr][nc] == 0:
                            s2.add((nr, nc))
                            res += 1  # 代表一种从当前感染格到本格的传播途径——如果要阻断，此处要建墙
            return res

        def defendMaxSpread() -> int:
            '''
            得到各感染区块中单块的最大的扩展范围，返回围堵这一范围需要的防火墙数量，并完成其他区域的扩散感染
            '''
            maxSpread = res = 0
            maxIdx = -1
            vis = [[False] * n for _ in range(m)]  # 记录访问状态
            # l1 保存每个感染连通区域的点集；l2 保存每个感染连通区域下一步的扩散区域点集
            l1 = []
            l2 = []
            for r in range(m):
                for c in range(n):
                    if isInfected[r][c] == 1 and not vis[r][c]:
                        # s1 当前感染区域的点集；s2 当前感染区域下一步的扩散区域
                        s1 = set()
                        s2 = set()
                        b = bfs(r, c, s1, s2, vis)
                        a = len(s2)
                        if a > maxSpread:
                            maxSpread = a
                            res = b
                            maxIdx = len(l1)  # 记住最大块对应的索引
                        l1.append(s1)
                        l2.append(s2)

            for i in range(len(l1)):
                if i == maxIdx:  # 最大块要完成隔离，感染区域标记为-1
                    for r, c in l1[i]:
                        isInfected[r][c] = -1
                else:  # 其他区域要完成传播扩散
                    for r, c in l2[i]:
                        isInfected[r][c] = 1

            return res

        res = 0
        while True:
            walls = defendMaxSpread()
            if walls == 0:
                # 完全控制住了或者已经挂了
                break
            res += walls

        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.containVirus([[0, 1, 0, 0, 0, 0, 0, 1], [
          0, 1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]]))  # 10
    print(solution.containVirus([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))  # 4
    print(solution.containVirus([[1, 1, 1, 0, 0, 0, 0, 0, 0], [
          1, 0, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0, 0, 0]]))  # 13
