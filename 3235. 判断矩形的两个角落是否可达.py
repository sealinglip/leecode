# 给你两个正整数 xCorner 和 yCorner 和一个二维整数数组 circles ，其中 circles[i] = [xi, yi, ri] 表示一个圆心在 (xi, yi) 半径为 ri 的圆。
# 坐标平面内有一个左下角在原点，右上角在 (xCorner, yCorner) 的矩形。你需要判断是否存在一条从左下角到右上角的路径满足：路径 完全 在矩形内部，不会 
# 触碰或者经过 任何 圆的内部和边界，同时 只 在起点和终点接触到矩形。

# 如果存在这样的路径，请你返回 true ，否则返回 false 。


# 示例 1：
# 输入：X = 3, Y = 4, circles = [[2,1,1]]
# 输出：true
# 解释：
# 黑色曲线表示一条从 (0, 0) 到 (3, 4) 的路径。

# 示例 2：
# 输入：X = 3, Y = 3, circles = [[1,1,2]]
# 输出：false
# 解释：
# 不存在从 (0, 0) 到 (3, 3) 的路径。

# 示例 3：
# 输入：X = 3, Y = 3, circles = [[2,1,1],[1,2,1]]
# 输出：false
# 解释：
# 不存在从 (0, 0) 到 (3, 3) 的路径。

# 示例 4：
# 输入：X = 4, Y = 4, circles = [[5,5,1]]
# 输出：true


# 提示：
# 3 <= xCorner, yCorner <= 10^9
# 1 <= circles.length <= 1000
# circles[i].length == 3
# 1 <= xi, yi, ri <= 10^9

# Hard

from typing import List
# @lc code=start

class UnionFind:
    def __init__(self, n: int):
        self.group = list(range(n))

    def findGroup(self, x: int) -> int:
        if self.group[x] == x:
            return x
        self.group[x] = self.findGroup(self.group[x])
        return self.group[x]

    def union(self, x: int, y: int):
        x, y = self.findGroup(x), self.findGroup(y)
        if x != y:
            self.group[x] = y

    def isConnected(self, x: int, y: int) -> bool:
        return self.findGroup(x) == self.findGroup(y)
    
class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: List[List[int]]) -> bool:
        # 连通图 + 并查集
        # 四条边和每个圆都相当于一个图元，如果两个图元相交或接触，说明它们是连通的，连通关系可以传递
        # 当下列图元最终处于连通状态时，返回False，否则返回True：
        # 左边-右边，左边-下边，上边-右边，上边-下边
        n = len(circles)
        # n ~ n + 3 分别代表矩阵的上右下左
        uf = UnionFind(n + 4)

        for i, (x, y, r) in enumerate(circles):
            # 先排除掉完全在矩形外的圆，以免连通是在矩形外发生的，影响判断
            if x - r >= xCorner or y - r >= yCorner:
                continue

            # 判断跟之前的圆相不相交
            for j in range(i):
                xj, yj, rj = circles[j]
                # 只有两个圆相交区域跟矩形有交集，才做合并
                if (xj - x) ** 2 + (yj - y) ** 2 <= (rj + r) ** 2 and x * rj + xj * r < (r + rj) * xCorner and y * rj + yj * r < (r + rj) * yCorner:
                    uf.union(i, j)

            # 判断圆跟四边相不相交
            # 判断圆和线段相不相交比想像的复杂
            # 判断和左相不相交
            if x <= r and (y <= yCorner or (x ** 2 + (y - yCorner) ** 2 <= r ** 2)):
                uf.union(i, n+3)
            # 判断和下相不相交
            if y <= r and (x <= xCorner or ((x - xCorner) ** 2 + y ** 2 <= r ** 2)):
                uf.union(i, n+2)
            # 判断和右相不相交
            if xCorner - r <= x <= xCorner + r and (y <= yCorner or ((x - xCorner) ** 2 + (y - yCorner) ** 2 <= r ** 2)):
                uf.union(i, n+1)
            # 判断和上相不相交
            if yCorner - r <= y <= yCorner + r and (x <= xCorner or ((x - xCorner) ** 2 + (y - yCorner) ** 2 <= r ** 2)):
                uf.union(i, n)

        return not (uf.isConnected(n, n+1) or uf.isConnected(n, n+2) or uf.isConnected(n+3, n+2) or uf.isConnected(n+3, n+1))

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.canReachCorner(15, 15, [[1,99,85],[99,1,85]])) # True
    # 下面的用例1，两个圆彼此相交，也分别和上边和右边相交，但是从矩形的外部连通的，所以应该返回True
    print(solution.canReachCorner(3, 3, [[2,1000,997],[1000,2,997]])) # True
    print(solution.canReachCorner(3, 4, [[2,1,1]])) # True
    print(solution.canReachCorner(3, 3, [[1,1,2]])) # False
    print(solution.canReachCorner(3, 3, [[2,1,1],[1,2,1]])) # False
    print(solution.canReachCorner(4, 4, [[5,5,1]])) # True
