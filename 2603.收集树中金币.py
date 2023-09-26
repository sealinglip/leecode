#
# @lc app=leetcode.cn id=2603 lang=python3
#
# [2603] 收集树中金币
#
# 给你一个 n 个节点的无向无根树，节点编号从 0 到 n - 1 。给你整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间有一条边。再给你一个长度为 n 的数组 coins ，其中 coins[i] 可能为 0 也可能为 1 ，1 表示节点 i 处有一个金币。

# 一开始，你需要选择树中任意一个节点出发。你可以执行下述操作任意次：

# 收集距离当前节点距离为 2 以内的所有金币，或者
# 移动到树中一个相邻节点。
# 你需要收集树中所有的金币，并且回到出发节点，请你返回最少经过的边数。

# 如果你多次经过一条边，每一次经过都会给答案加一。


# 示例 1：
# 输入：coins = [1, 0, 0, 0, 0, 1], edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
# 输出：2
# 解释：从节点 2 出发，收集节点 0 处的金币，移动到节点 3 ，收集节点 5 处的金币，然后移动回节点 2 。

# 示例 2：
# 输入：coins = [0, 0, 0, 1, 1, 0, 0, 1], edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [5, 6], [5, 7]]
# 输出：2
# 解释：从节点 0 出发，收集节点 4 和 3 处的金币，移动到节点 2 处，收集节点 7 处的金币，移动回节点 0 。


# 提示：
# n == coins.length
# 1 <= n <= 3 * 104
# 0 <= coins[i] <= 1
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# edges 表示一棵合法的树。

# Hard
# 复习

from collections import defaultdict, deque
from typing import List
# @lc code=start


class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        # 构建关系
        n = len(coins)
        graph = defaultdict(list)  # 记录每个点能连到的点
        cnt = [0] * n  # 记录每个点上的边数
        for u, v in edges:
            graph[u].append(v)
            cnt[u] += 1
            graph[v].append(u)
            cnt[v] += 1

        # 定义最外层为边数为1的点
        # 先去掉最外层点钟coins为零的
        valueless = deque(
            [i for i in range(n) if cnt[i] == 1 and coins[i] == 0])
        while valueless:
            i = valueless.popleft()
            cnt[i] = 0  # 从图中删除该节点
            # 跟它相连的节点cnt减一
            for j in graph[i]:
                if cnt[j] > 0:
                    cnt[j] -= 1
                    if cnt[j] == 1 and coins[j] == 0:
                        valueless.append(j)

        # 剩下的节点中，再去掉两层
        for j in range(2):
            leaves = [i for i in range(n) if cnt[i] == 1]
            for i in leaves:
                cnt[i] = 0  # 从图中删除该节点
                # 跟它相连的节点cnt减一
                for k in graph[i]:
                    if cnt[k] > 0:
                        cnt[k] -= 1

        # 剩下的节点都要走到，就看最少步数遍历了——好像怎么走都是 (点数-1)*2
        left = (n - cnt.count(0))
        return max((left - 1) << 1, 0)
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.collectTheCoins(
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0], [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [4, 6], [2, 7], [7, 8], [3, 9], [8, 10], [8, 11], [6, 12], [7, 13], [11, 14], [10, 15]]))  # 4
    print(solution.collectTheCoins([0], []))  # 0
    print(solution.collectTheCoins([1, 0, 0, 0, 0, 1], [
          [0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]))  # 2
    print(solution.collectTheCoins([0, 0, 0, 1, 1, 0, 0, 1], [
          [0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [5, 6], [5, 7]]))  # 2
