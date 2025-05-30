# 现有一棵 无向 树，树中包含 n 个节点，按从 0 到 n - 1 标记。树的根节点是节点 0 。给你一个长度为 n - 1 的二维整数数组 edges，其中 edges[i] = [ai, bi] 表示树中节点 ai 与节点 bi 之间存在一条边。

# 如果一个节点的所有子节点为根的 子树 包含的节点数相同，则认为该节点是一个 好节点。

# 返回给定树中 好节点 的数量。

# 子树 指的是一个节点以及它所有后代节点构成的一棵树。

 
# 示例 1：
# 输入：edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
# 输出：7
# 说明：
# 树的所有节点都是好节点。

# 示例 2：
# 输入：edges = [[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]]
# 输出：6
# 说明：
# 树中有 6 个好节点。上图中已将这些节点着色。

# 示例 3：
# 输入：edges = [[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]]
# 输出：12
# 解释：
# 除了节点 9 以外其他所有节点都是好节点。


# 提示：
# 2 <= n <= 10^5
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# 输入确保 edges 总表示一棵有效的树。

from collections import defaultdict
from typing import List

class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        # 先构建连通图
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # descendantCnt = {}
        res = 0
        # 后序遍历，可得每个节点的所有后代节点数
        def visit(node: int, parent: int) -> int:
            '''
            返回当前节点的所有后代节点数（含自身）
            '''
            nonlocal res
            if len(graph[node]) == 1 and graph[node][0] == parent:
                # 叶子节点都是好节点
                res += 1
                return 1
            else:
                # 非叶子节点
                cnt = 1 # 自己
                preSubCnt = -1
                flag = True
                for c in graph[node]:
                    if c == parent:
                        continue
                    subCnt = visit(c, node)
                    if preSubCnt == -1:
                        preSubCnt = subCnt
                    elif preSubCnt != subCnt:
                        flag = False
                    cnt += subCnt

                if flag:
                    res += 1
                return cnt
            
        visit(0, -1)
        
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.countGoodNodes([[2,0],[4,2],[1,2],[3,1],[5,1]])) # 5
    print(solution.countGoodNodes([[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]])) # 7
    print(solution.countGoodNodes([[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]])) # 6
    print(solution.countGoodNodes([[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]])) # 12
