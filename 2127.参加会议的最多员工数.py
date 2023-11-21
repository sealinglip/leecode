#
# @lc app=leetcode.cn id=2127 lang=python3
#
# [2127] 参加会议的最多员工数
#
# 一个公司准备组织一场会议，邀请名单上有 n 位员工。公司准备了一张 圆形 的桌子，可以坐下 任意数目 的员工。

# 员工编号为 0 到 n - 1 。每位员工都有一位 喜欢 的员工，每位员工 当且仅当 他被安排在喜欢员工的旁边，他才会参加会议。每位员工喜欢的员工 不会 是他自己。

# 给你一个下标从 0 开始的整数数组 favorite ，其中 favorite[i] 表示第 i 位员工喜欢的员工。请你返回参加会议的 最多员工数目 。


# 示例 1：
# 输入：favorite = [2, 2, 1, 2]
# 输出：3
# 解释：
# 上图展示了公司邀请员工 0，1 和 2 参加会议以及他们在圆桌上的座位。
# 没办法邀请所有员工参与会议，因为员工 2 没办法同时坐在 0，1 和 3 员工的旁边。
# 注意，公司也可以邀请员工 1，2 和 3 参加会议。
# 所以最多参加会议的员工数目为 3 。

# 示例 2：
# 输入：favorite = [1, 2, 0]
# 输出：3
# 解释：
# 每个员工都至少是另一个员工喜欢的员工。所以公司邀请他们所有人参加会议的前提是所有人都参加了会议。
# 座位安排同图 1 所示：
# - 员工 0 坐在员工 2 和 1 之间。
# - 员工 1 坐在员工 0 和 2 之间。
# - 员工 2 坐在员工 1 和 0 之间。
# 参与会议的最多员工数目为 3 。

# 示例 3：
# 输入：favorite = [3, 0, 1, 4, 1]
# 输出：4
# 解释：
# 上图展示了公司可以邀请员工 0，1，3 和 4 参加会议以及他们在圆桌上的座位。
# 员工 2 无法参加，因为他喜欢的员工 0 旁边的座位已经被占领了。
# 所以公司只能不邀请员工 2 。
# 参加会议的最多员工数目为 4 。


# 提示：
# n == favorite.length
# 2 <= n <= 10^5
# 0 <= favorite[i] <= n - 1
# favorite[i] != i

# Hard
# 复习

from collections import deque
from typing import List
# @lc code=start


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        # 统计入度：几个人喜欢他/她
        indegree = [0] * n
        for f in favorite:
            indegree[f] += 1

        visited = [False] * n
        f = [1] * n  # 记录以每个节点为终点的最长喜爱链长度
        # 把所有没人喜欢的人放到队列，从他们出发找环
        q = deque(i for i in range(n) if indegree[i] == 0)
        # 基环内向树
        while q:
            # 以下的效果是遍历所有不在环上的点
            p = q.popleft()
            visited[p] = True
            v = favorite[p]
            f[v] = max(f[v], f[p] + 1)  # 状态转移
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

        maxRing = maxBin = 0  # maxRing是最大环的大小；maxBin是环长为2时的最长双向游走路径之和
        for i in range(n):
            # 所有未被访问过的，都是在环上的点
            if not visited[i]:
                visited[i] = True
                j = favorite[i]
                if favorite[j] == i:  # 二人环
                    maxBin = maxBin + f[i] + f[j]
                    visited[j] = True
                else:  # 找出来环多大
                    ringSize = 1
                    while j != i:
                        visited[j] = True
                        ringSize += 1
                        j = favorite[j]
                    maxRing = max(maxRing, ringSize)

        return max(maxRing, maxBin)


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumInvitations(
        [1, 0, 3, 2, 5, 6, 7, 4, 9, 8, 11, 10, 11, 12, 10]))  # 11
    print(solution.maximumInvitations([2, 2, 1, 2]))  # 3
    print(solution.maximumInvitations([1, 2, 0]))  # 3
    print(solution.maximumInvitations([3, 0, 1, 4, 1]))  # 4
