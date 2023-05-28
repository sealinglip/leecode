#
# @lc app=leetcode.cn id=1377 lang=python3
#
# [1377] T 秒后青蛙的位置
#
# 给你一棵由 n 个顶点组成的无向树，顶点编号从 1 到 n。青蛙从 顶点 1 开始起跳。规则如下：

# 在一秒内，青蛙从它所在的当前顶点跳到另一个 未访问 过的顶点（如果它们直接相连）。
# 青蛙无法跳回已经访问过的顶点。
# 如果青蛙可以跳到多个不同顶点，那么它跳到其中任意一个顶点上的机率都相同。
# 如果青蛙不能跳到任何未访问过的顶点上，那么它每次跳跃都会停留在原地。
# 无向树的边用数组 edges 描述，其中 edges[i] = [ai, bi] 意味着存在一条直接连通 ai 和 bi 两个顶点的边。

# 返回青蛙在 t 秒后位于目标顶点 target 上的概率。与实际答案相差不超过 10-5 的结果将被视为正确答案。


# 示例 1：
# 输入：n = 7, edges = [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t = 2, target = 4
# 输出：0.16666666666666666
# 解释：上图显示了青蛙的跳跃路径。青蛙从顶点 1 起跳，第 1 秒 有 1/3 的概率跳到顶点 2 ，然后第 2 秒 有 1/2 的概率跳到顶点 4，因此青蛙在 2 秒后位于顶点 4 的概率是 1/3 * 1/2 = 1/6 = 0.16666666666666666 。

# 示例 2：
# 输入：n = 7, edges = [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t = 1, target = 7
# 输出：0.3333333333333333
# 解释：上图显示了青蛙的跳跃路径。青蛙从顶点 1 起跳，有 1/3 = 0.3333333333333333 的概率能够 1 秒 后跳到顶点 7 。


# 提示：
# 1 <= n <= 100
# edges.length == n - 1
# edges[i].length == 2
# 1 <= ai, bi <= n
# 1 <= t <= 50
# 1 <= target <= n

# Hard

from collections import defaultdict
from typing import List
# @lc code=start


class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        # 要求从顶点1到顶点target的所有路径中，长度为t的，再将概率相加
        # 先构造路径图
        paths = defaultdict(list)
        for s, e in edges:
            paths[s].append(e)
            paths[e].append(s)

        # 限制深度的深度优先搜索？
        res = []
        visited = set()

        def dfs(node: int, probability: float, level: int):
            if node == target:
                if level < t:
                    # 到早了，如果不是已经无路可走，就不行
                    links = list(
                        filter(lambda k: k not in visited, paths[node]))
                    if len(links) > 0:
                        return
                res.append(probability)
                return
            elif level == t:
                return

            visited.add(node)
            links = list(filter(lambda k: k not in visited, paths[node]))
            if len(links) == 0:
                # 无路可走
                return

            probability /= len(links)
            level += 1
            for l in links:
                dfs(l, probability, level)

            visited.remove(node)

        dfs(1, 1, 0)

        return sum(res)


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.frogPosition(9, [[2, 1], [3, 1], [4, 2], [5, 3], [
          6, 5], [7, 4], [8, 7], [9, 7]], 1, 8))  # 0.0
    print(solution.frogPosition(7, [[1, 2], [1, 3], [1, 7], [
          2, 4], [2, 6], [3, 5]], 20, 6))  # 0.16666666666666666
    print(solution.frogPosition(7, [[1, 2], [1, 3], [1, 7], [
          2, 4], [2, 6], [3, 5]], 2, 4))  # 0.16666666666666666
    print(solution.frogPosition(7, [[1, 2], [1, 3], [1, 7], [
          2, 4], [2, 6], [3, 5]], 1, 7))  # 0.3333333333333333
