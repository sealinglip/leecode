#
# @lc app=leetcode.cn id=1483 lang=python3
#
# [1483] 树节点的第 K 个祖先
#
# 给你一棵树，树上有 n 个节点，按从 0 到 n-1 编号。树以父节点数组的形式给出，其中 parent[i] 是节点 i 的父节点。树的根节点是编号为 0 的节点。

# 树节点的第 k 个祖先节点是从该节点到根节点路径上的第 k 个节点。

# 实现 TreeAncestor 类：

# TreeAncestor（int n， int[] parent） 对树和父数组中的节点数初始化对象。
# getKthAncestor(int node, int k) 返回节点 node 的第 k 个祖先节点。如果不存在这样的祖先节点，返回 - 1 。


# 示例 1：
# 输入：
# ["TreeAncestor", "getKthAncestor", "getKthAncestor", "getKthAncestor"]
# [[7, [-1, 0, 0, 1, 1, 2, 2]], [3, 1], [5, 2], [6, 3]]
# 输出：
# [null, 1, 0, -1]
# 解释：
# TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])

# treeAncestor.getKthAncestor(3, 1)
# // 返回 1 ，它是 3 的父节点
# treeAncestor.getKthAncestor(5, 2)
# // 返回 0 ，它是 5 的祖父节点
# treeAncestor.getKthAncestor(6, 3)
# // 返回 - 1 因为不存在满足要求的祖先节点


# 提示：
# 1 <= k <= n <= 5 * 10^4
# parent[0] == -1 表示编号为 0 的节点是根节点。
# 对于所有的 0 < i < n ，0 <= parent[i] < n 总成立
# 0 <= node < n
# 至多查询 5 * 10^4 次

# Hard
# 直接写会TLE
# 复习

from typing import List
# @lc code=start


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        # 定义ancestors[i][j]表示节点 i 的第 2^j 个祖先
        # 因为节点数最多50000，那么j < 16 (2^16 = 65535 > 50000)
        self.log = 16
        self.ancestors = [[-1] * self.log for _ in range(n)]
        for i in range(n):
            self.ancestors[i][0] = parent[i]
        for j in range(1, self.log):
            for i in range(n):
                if self.ancestors[i][j-1] != -1:
                    self.ancestors[i][j] = self.ancestors[self.ancestors[i][j-1]][j-1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for j in range(self.log):
            if ((k >> j) & 1):
                node = self.ancestors[node][j]
                if node == -1:
                    break
        # 下面的实现会TLE，加了缓存还是会TLE
        # key = (node, k)
        # if key in self.cache:
        #     return self.cache[key]

        # if k > 0 and node != -1:
        #     node = self.getKthAncestor(self.parent[node], k-1)

        # self.cache[key] = node

        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
# @lc code=end
if __name__ == "__main__":
    treeAncestor = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
    print(treeAncestor.getKthAncestor(3, 1))  # 1
    print(treeAncestor.getKthAncestor(5, 2))  # 0
    print(treeAncestor.getKthAncestor(6, 3))  # -1
    print(treeAncestor.getKthAncestor(6, 2))  # 0
