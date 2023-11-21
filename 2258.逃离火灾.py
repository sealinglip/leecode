#
# @lc app=leetcode.cn id=2258 lang=python3
#
# [2258] 逃离火灾
#
# 给你一个下标从 0 开始大小为 m x n 的二维整数数组 grid ，它表示一个网格图。每个格子为下面 3 个值之一：

# 0 表示草地。
# 1 表示着火的格子。
# 2 表示一座墙，你跟火都不能通过这个格子。
# 一开始你在最左上角的格子 (0, 0) ，你想要到达最右下角的安全屋格子 (m - 1, n - 1) 。每一分钟，你可以移动到 相邻 的草地格子。每次你移动 之后 ，着火的格子会扩散到所有不是墙的 相邻 格子。

# 请你返回你在初始位置可以停留的 最多 分钟数，且停留完这段时间后你还能安全到达安全屋。如果无法实现，请你返回 -1 。如果不管你在初始位置停留多久，你 总是 能到达安全屋，请你返回 10^9 。

# 注意，如果你到达安全屋后，火马上到了安全屋，这视为你能够安全到达安全屋。

# 如果两个格子有共同边，那么它们为 相邻 格子。

# 示例 1：
# 输入：grid = [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]
# 输出：3
# 解释：上图展示了你在初始位置停留 3 分钟后的情形。
# 你仍然可以安全到达安全屋。
# 停留超过 3 分钟会让你无法安全到达安全屋。

# 示例 2：
# 输入：grid = [[0,0,0,0],[0,1,2,0],[0,2,0,0]]
# 输出：-1
# 解释：上图展示了你马上开始朝安全屋移动的情形。
# 火会蔓延到你可以移动的所有格子，所以无法安全到达安全屋。
# 所以返回 -1 。

# 示例 3：
# 输入：grid = [[0,0,0],[2,2,0],[1,2,0]]
# 输出：1000000000
# 解释：上图展示了初始网格图。
# 注意，由于火被墙围了起来，所以无论如何你都能安全到达安全屋。
# 所以返回 10^9 。
 

# 提示：
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 300
# 4 <= m * n <= 2 * 10^4
# grid[i][j] 是 0 ，1 或者 2 。
# grid[0][0] == grid[m - 1][n - 1] == 0

# Hard
# 复习
# 牢记广度优先遍历要用两个列表轮换遍历，不要只用一个先进先出队列，以避免遍历重复元素
from collections import deque
from typing import List
# @lc code=start
class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        

        DIR = [(1,0), (-1,0), (0,1), (0,-1)]
        q = []
        # 先把代表墙的“2”变成“-1”，不然有点碍事
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 2:
                    grid[x][y] = -1
                elif grid[x][y] == 1:
                    q.append((x, y))
        # 标记一下到最后每块草地格子着火的时间(grid里的数比实际着火时间大1)
        i = 1
        while q:
            newQ = []
            i += 1
            for x, y in q:
                for dx, dy in DIR:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                        grid[nx][ny] = i
                        newQ.append((nx ,ny))
            q = newQ

        # 下面的方法会TLE
        UB = 10 ** 9
        def getArriveTime(stayTime: int) -> int:
            '''
            在（0, 0）位置待stayTime分钟，到达安全屋的最短时间
            '''
            q = [(0, 0, stayTime)]
            visited = set((0, 0))
            while q:
                newQ = []
                for x, y, s in q: # 坐标和步数
                    s += 1
                    
                    for dx, dy in DIR:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > -1 and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            g = grid[nx][ny]-1 if grid[nx][ny] else UB # 本格着火时间，如果永不着火，就是10^9
                            if nx == m - 1 and ny == n - 1: # 到终点了
                                if g >=s: # 终点格人和火可以同时到
                                    return s
                            elif g > s:
                                newQ.append((nx, ny, s))
                q = newQ
            
            # 没路可达或者火拦路
            return -1
        
        t = getArriveTime(0) # 一刻不停，看能不能到
        if t == -1:
            return -1
        
        if grid[-1][-1] == 0:
            return UB
        
        stay = grid[-1][-1] - 1 - t
        return stay if getArriveTime(stay) > 0 else stay - 1



# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumMinutes([[0,0,0,0,0],[0,2,0,2,0],[0,2,0,2,0],[0,2,1,2,0],[0,2,2,2,0],[0,0,0,0,0]])) # 1
    print(solution.maximumMinutes([[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]])) # 3
    print(solution.maximumMinutes([[0,0,0,0],[0,1,2,0],[0,2,0,0]])) # -1
    print(solution.maximumMinutes([[0,0,0],[2,2,0],[1,2,0]])) # 1000000000