#
# @lc app=leetcode.cn id=2867 lang=python3
#
# [2867] 统计树中的合法路径数目
#
# 给你一棵 n 个节点的无向树，节点编号为 1 到 n 。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ui, vi] 表示节点 ui 和 vi 在树中有一条边。

# 请你返回树中的 合法路径数目 。

# 如果在节点 a 到节点 b 之间 恰好有一个 节点的编号是质数，那么我们称路径 (a, b) 是 合法的 。

# 注意：

# 路径 (a, b) 指的是一条从节点 a 开始到节点 b 结束的一个节点序列，序列中的节点 互不相同 ，且相邻节点之间在树上有一条边。
# 路径 (a, b) 和路径 (b, a) 视为 同一条 路径，且只计入答案 一次 。
 

# 示例 1：
# 输入：n = 5, edges = [[1,2],[1,3],[2,4],[2,5]]
# 输出：4
# 解释：恰好有一个质数编号的节点路径有：
# - (1, 2) 因为路径 1 到 2 只包含一个质数 2 。
# - (1, 3) 因为路径 1 到 3 只包含一个质数 3 。
# - (1, 4) 因为路径 1 到 4 只包含一个质数 2 。
# - (2, 4) 因为路径 2 到 4 只包含一个质数 2 。
# 只有 4 条合法路径。

# 示例 2：
# 输入：n = 6, edges = [[1,2],[1,3],[2,4],[3,5],[3,6]]
# 输出：6
# 解释：恰好有一个质数编号的节点路径有：
# - (1, 2) 因为路径 1 到 2 只包含一个质数 2 。
# - (1, 3) 因为路径 1 到 3 只包含一个质数 3 。
# - (1, 4) 因为路径 1 到 4 只包含一个质数 2 。
# - (1, 6) 因为路径 1 到 6 只包含一个质数 3 。
# - (2, 4) 因为路径 2 到 4 只包含一个质数 2 。
# - (3, 6) 因为路径 3 到 6 只包含一个质数 3 。
# 只有 6 条合法路径。
 

# 提示：
# 1 <= n <= 10^5
# edges.length == n - 1
# edges[i].length == 2
# 1 <= ui, vi <= n
# 输入保证 edges 形成一棵合法的树。

# Hard
# 复习

from collections import defaultdict
from typing import List
# @lc code=start
class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        def isPrime(x: int) -> bool:
            '''
            判断传入整数是否为质数
            '''
            if x == 1:
                return False
            if x == 2 or x == 3:
                return True
            if (r:= x % 6) != 1 and r != 5:
                return False
            for i in range(5, int(x ** 0.5) + 1, 6):
                if x % i == 0 or x % (i + 2) == 0:
                    return False
            return True
        
        # 先找出1~n中所有的质数
        primes = set([i for i in range(2, n+1) if isPrime(i)])

        # 构建路径图
        conn = defaultdict(list)
        for u, v in edges:
            conn[u].append(v)
            conn[v].append(u)

        # 感觉大概率要TLE，但暂时没有更好的想法 —— 果然TLE了，吐血
        # 以每个质数节点为根，求其各子树节点数量，遍历子树时碰到质数节点就跳过不处理
        # @cache
        # def subTreeNodesCount(parent: int, current: int) -> int:
        #     cnt = 1
        #     for child in conn[current]:
        #         if child == parent or isPrime(child):
        #             continue
        #         cnt += subTreeNodesCount(current, child)
        #     return cnt

        # res = 0
        # for p in primes:
        #     accum = 1
        #     for c in conn[p]:
        #         if c in primes:
        #             continue
        #         nc = subTreeNodesCount(p, c)
        #         res += nc * accum
        #         accum += nc
            
        # return res
            
        # 👆🏻的解法之所以超时，是因为重复求了很多遍子树节点数量，换个角度，子树的父都是质数节点，子树实际上是非质数节点的连通分量，子树节点数就是连通分量大小
        # 先求出连通分量大小，标记，然后再遍历质数节点求解 —— 总算过了
        def markConnectedComposite(parent: int, current: int, visited: List[int]) -> None:
            visited.append(current)
            for child in conn[current]:
                if child == parent or isPrime(child):
                    continue
                markConnectedComposite(current, child, visited)
        
        cntCheatsheet = [0] * (n + 1)
        res = 0
        for p in primes:
            accum = 1 # 累计的节点，现在只有自己
            for c in conn[p]:
                if c in primes:
                    continue
                if cntCheatsheet[c] == 0:
                    visited = []
                    markConnectedComposite(p, c, visited)
                    cnt = len(visited) # 连通分量大小
                    for node in visited:
                        cntCheatsheet[node] = cnt
                res += accum * cntCheatsheet[c] # 每个累计的节点跟新连通集的每个节点都可以有一条合法路径
                accum += cntCheatsheet[c] # 更新累计节点数量

        return res        

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countPaths(5, [[1,2],[1,3],[2,4],[2,5]])) # 4
    print(solution.countPaths(6, [[1,2],[1,3],[2,4],[3,5],[3,6]])) # 6