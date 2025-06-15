#
# @lc app=leetcode.cn id=2359 lang=python3
#
# [2359] 找到离给定两个节点最近的节点
#
# https://leetcode.cn/problems/find-closest-node-to-given-two-nodes/description/
#
# algorithms
# Medium (32.61%)
# Likes:    37
# Dislikes: 0
# Total Accepted:    11.3K
# Total Submissions: 32.8K
# Testcase Example:  '[2,2,3,-1]\n0\n1'
#
# 给你一个 n 个节点的 有向图 ，节点编号为 0 到 n - 1 ，每个节点 至多 有一条出边。
# 
# 有向图用大小为 n 下标从 0 开始的数组 edges 表示，表示节点 i 有一条有向边指向 edges[i] 。如果节点 i 没有出边，那么
# edges[i] == -1 。
# 
# 同时给你两个节点 node1 和 node2 。
# 
# 请你返回一个从 node1 和 node2 都能到达节点的编号，使节点 node1 和节点 node2 到这个节点的距离
# 较大值最小化。如果有多个答案，请返回 最小 的节点编号。如果答案不存在，返回 -1 。
# 
# 注意 edges 可能包含环。
# 
# 示例 1：
# 输入：edges = [2,2,3,-1], node1 = 0, node2 = 1
# 输出：2
# 解释：从节点 0 到节点 2 的距离为 1 ，从节点 1 到节点 2 的距离为 1 。
# 两个距离的较大值为 1 。我们无法得到一个比 1 更小的较大值，所以我们返回节点 2 。
# 
# 
# 示例 2：
# 输入：edges = [1,2,-1], node1 = 0, node2 = 2
# 输出：2
# 解释：节点 0 到节点 2 的距离为 2 ，节点 2 到它自己的距离为 0 。
# 两个距离的较大值为 2 。我们无法得到一个比 2 更小的较大值，所以我们返回节点 2 。
# 
# 
# 提示：
# n == edges.length
# 2 <= n <= 10^5
# -1 <= edges[i] < n
# edges[i] != i
# 0 <= node1, node2 < n
# 
#

from typing import Dict, List, Set
# @lc code=start
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def path(node: int) -> List[int]:
            '''
            返回从node出发的路径
            '''
            path = [] # 记录从node出发的路径
            visited = set()
            while node != -1 and node not in visited:
                visited.add(node)
                path.append(node)
                node = edges[node]
            return path
        
        dist1 = {x: i for i, x in enumerate(path(node1))}
        ma = res = n = len(edges)
        for i, x in enumerate(path(node2)):
            if x in dist1:
                if (y := max(dist1[x], i)) <= ma:
                    if y < ma or x < res:
                        res = x
                        ma = y

        return res if res < n else -1
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.closestMeetingNode([5,4,5,4,3,6,-1], 0, 1)) # -1
    print(solution.closestMeetingNode([4,4,4,5,1,2,2], 1, 1)) # 1
    print(solution.closestMeetingNode([2,2,3,-1], 0, 1)) # 2
    print(solution.closestMeetingNode([1,2,-1], 0, 2)) # 2
