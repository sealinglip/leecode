#
# @lc app=leetcode.cn id=593 lang=python3
#
# [593] 有效的正方形
#
# 给定2D空间中四个点的坐标 p1, p2, p3 和 p4，如果这四个点构成一个正方形，则返回 true 。

# 点的坐标 pi 表示为 [xi, yi] 。输入 不是 按任何顺序给出的。

# 一个 有效的正方形 有四条等边和四个等角(90度角)。


# 示例 1:
# 输入: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# 输出: True

# 示例 2:
# 输入：p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
# 输出：false

# 示例 3:
# 输入：p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
# 输出：true


# 提示:
# p1.length == p2.length == p3.length == p4.length == 2
# -10^4 <= xi, yi <= 10^4


from typing import List
# @lc code=start


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def isPerpendicular(p: List[int], a: List[int], b: List[int]) -> bool:
            '''
            判断连线pa是否垂直于连线pb
            '''
            # 判断两线垂直，向量点积为零
            return (p[0] - a[0]) * (p[0] - b[0]) + (p[1] - a[1]) * (p[1] - b[1]) == 0

        def distanceSquare(a: List[int], b: List[int]) -> int:
            '''
            得到两点距离的平方
            '''
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        # 随便选一个点，判断它到另外三点的距离平方，应该有两个是相等的，其和等于剩下的一个
        d2 = distanceSquare(p1, p2)
        d3 = distanceSquare(p1, p3)
        d4 = distanceSquare(p1, p4)

        if d2 == d3:
            edge = d2
            diag = d4
            a = p2
            b = p3
            c = p4
        elif d2 == d4:
            edge = d2
            diag = d3
            a = p2
            b = p4
            c = p3
        elif d3 == d4:
            edge = d3
            diag = d2
            a = p3
            b = p4
            c = p2
        else:
            return False

        if (edge << 1) != diag or edge == 0:
            return False

        if not (isPerpendicular(p1, a, b) and isPerpendicular(c, a, b)):
            return False

        if distanceSquare(a, c) != edge or distanceSquare(b, c) != edge:
            return False

        return True

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.validSquare([0, 0], [0, 0], [0, 0], [0, 0]))  # False
    print(solution.validSquare([0, 0], [1, 1], [1, 0], [0, 1]))  # True
    print(solution.validSquare([0, 0], [1, 1], [1, 0], [0, 12]))  # False
    print(solution.validSquare([1, 0], [-1, 0],
                               [0, 1],  [0, -1]))  # True
