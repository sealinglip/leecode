#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#
# '[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
# 给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示
# 等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。
# 另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。
# 返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。

# 注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。

# 示例 1：
# 输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# 输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
# 解释：
# 条件：a / b = 2.0, b / c = 3.0
# 问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# 结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]

# 示例 2：
# 输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# 输出：[3.75000,0.40000,5.00000,0.20000]

# 示例 3：
# 输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# 输出：[0.50000,2.00000,-1.00000,-1.00000]
 
# 提示：
# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj 由小写英文字母与数字组成

from typing import List
# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        vars = []
        varIdx = {}
        for i, e in enumerate(equations):
            x, y = e[0], e[1]
            xi, yi = varIdx.get(x, -1), varIdx.get(y, -1)
            if xi == -1: # x未收录
                if yi == -1: # y未收录
                    d = {}
                    d[x] = (y, values[i])
                    d[y] = (y, 1)
                    varIdx[x] = len(vars)
                    varIdx[y] = len(vars)
                    vars.append(d)
                else: # y已收录
                    d = vars[yi]
                    base, factor = d[y]
                    d[x] = (base, factor * values[i])
                    varIdx[x] = yi
            elif yi == -1: # x已收录，y未收录
                d = vars[xi]
                base, factor = d[x]
                d[y] = (base, factor / values[i])
                varIdx[y] = xi
            elif yi != xi: # x，y均已收录，但不在一个组
                # 两边基数的比值为
                f = vars[yi][y][1] / vars[xi][x][1] * values[i]
                d = vars[yi]
                d2 = vars[xi]
                newBase = d[y][0]
                for var in d2:
                    base, factor = d2[var]
                    d[var] = (newBase, factor * f)
                    varIdx[var] = yi

        res = []
        for x, y in queries:
            xi, yi = varIdx.get(x, -1), varIdx.get(y, -1)
            if xi != -1 and xi == yi:
                d = vars[xi]
                res.append(d[x][1] / d[y][1])
            else:
                res.append(-1)

        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.calcEquation([["a", "b"], ["c", "d"], ["e", "f"], ["a", "c"], ["c", "f"]], [2.0, 3.0, 4.0, 5.0, 6.0],
                                [["c", "e"]]))
    print(solution.calcEquation([["a", "b"], ["e", "f"], ["b", "e"]], [3.4, 1.4, 2.3], 
          [["b", "a"], ["a", "f"], ["f", "f"], ["e", "e"], ["c", "c"], ["a", "c"], ["f", "e"]]))
    print(solution.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0], [
          ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
    print(solution.calcEquation([["a", "b"], ["b", "c"], ["bc", "cd"]], [
          1.5, 2.5, 5.0], [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]))
    print(solution.calcEquation([["a", "b"]], [0.5], [
          ["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]))
