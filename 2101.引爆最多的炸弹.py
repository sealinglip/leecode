#
# @lc app=leetcode.cn id=2101 lang=python3
#
# [2101] 引爆最多的炸弹
#
# 给你一个炸弹列表。一个炸弹的 爆炸范围 定义为以炸弹为圆心的一个圆。
# 炸弹用一个下标从 0 开始的二维整数数组 bombs 表示，其中 bombs[i] = [xi, yi, ri] 。xi 和 yi 表示第 i 个炸弹的 X 和 Y 坐标，ri 表示爆炸范围的 半径 。
# 你需要选择引爆 一个 炸弹。当这个炸弹被引爆时，所有 在它爆炸范围内的炸弹都会被引爆，这些炸弹会进一步将它们爆炸范围内的其他炸弹引爆。
# 给你数组 bombs ，请你返回在引爆 一个 炸弹的前提下，最多 能引爆的炸弹数目。

# 示例 1：
# 输入：bombs = [[2,1,3],[6,1,4]]
# 输出：2
# 解释：
# 上图展示了 2 个炸弹的位置和爆炸范围。
# 如果我们引爆左边的炸弹，右边的炸弹不会被影响。
# 但如果我们引爆右边的炸弹，两个炸弹都会爆炸。
# 所以最多能引爆的炸弹数目是 max(1, 2) = 2 。

# 示例 2：
# 输入：bombs = [[1,1,5],[10,10,5]]
# 输出：1
# 解释：
# 引爆任意一个炸弹都不会引爆另一个炸弹。所以最多能引爆的炸弹数目为 1 。

# 示例 3：
# 输入：bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
# 输出：5
# 解释：
# 最佳引爆炸弹为炸弹 0 ，因为：
# - 炸弹 0 引爆炸弹 1 和 2 。红色圆表示炸弹 0 的爆炸范围。
# - 炸弹 2 引爆炸弹 3 。蓝色圆表示炸弹 2 的爆炸范围。
# - 炸弹 3 引爆炸弹 4 。绿色圆表示炸弹 3 的爆炸范围。
# 所以总共有 5 个炸弹被引爆。
 

# 提示：
# 1 <= bombs.length <= 100
# bombs[i].length == 3
# 1 <= xi, yi, ri <= 10^5

from collections import defaultdict
from math import sqrt
from typing import List
# @lc code=start
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        # 引爆a，能连锁引爆b的话，说明存在从a到b的一条有向边
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                d = sqrt((bombs[j][0] - bombs[i][0]) ** 2 + (bombs[j][1] - bombs[i][1]) ** 2)
                if d <= bombs[i][2]:
                    graph[i].append(j)
                if d <= bombs[j][2]:
                    graph[j].append(i)

        # 依次遍历每个i，dfs，求引爆数量
        def dfs(i: int) -> int:
            visited = set()
            st = [i]
            visited.add(i)
            d = 0
            while st:
                j = st.pop()
                d += 1
                for k in graph[j]:
                    if k not in visited:
                        visited.add(k)
                        st.append(k)
            return d
        
        res = 0
        for i in range(n):
            res = max(res, dfs(i))

        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumDetonation([[2,1,3],[6,1,4]])) # 2
    print(solution.maximumDetonation([[1,1,5],[10,10,5]])) # 1
    print(solution.maximumDetonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]])) # 5