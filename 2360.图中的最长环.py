#
# @lc app=leetcode.cn id=2360 lang=python3
#
# [2360] 图中的最长环
#
# 给你一个 n 个节点的 有向图 ，节点编号为 0 到 n - 1 ，其中每个节点 至多 有一条出边。
# 图用一个大小为 n 下标从 0 开始的数组 edges 表示，节点 i 到节点 edges[i] 之间有一条有向边。如果节点 i 没有出边，那么 edges[i] == -1 。
# 请你返回图中的 最长 环，如果没有任何环，请返回 -1 。
# 一个环指的是起点和终点是 同一个 节点的路径。


# 示例 1：
# 输入：edges = [3,3,4,2,3]
# 输出去：3
# 解释：图中的最长环是：2 -> 4 -> 3 -> 2 。
# 这个环的长度为 3 ，所以返回 3 。

# 示例 2：
# 输入：edges = [2,-1,3,1]
# 输出：-1
# 解释：图中没有任何环。
 

# 提示：
# n == edges.length
# 2 <= n <= 10^5
# -1 <= edges[i] < n
# edges[i] != i

# Hard

from typing import List
# @lc code=start
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        # 每个节点至多一条出边，那么一个节点最多在一个环里
        # 遍历每个节点是否在环中，并记录环的长度
        visited = [0] * n # 记录访问过的节点，未访问过都为0，访问过的记录第几步访问熬
        
        res = -1
        step = 1
        for i in range(n):
            if visited[i] > 0:
                continue
            
            start = step # 记录当前节点的步数
            j = i
            while j >= 0 and visited[j] == 0:
                visited[j] = step
                step += 1
                j = edges[j]
            if j >= 0 and visited[j] >= start: # 成环了
                res = max(res, step - visited[j])
                 
        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCycle([3,3,4,2,3])) # 3
    print(solution.longestCycle([2,-1,3,1])) # -1
