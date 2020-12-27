#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#
# 给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。

# 示例 1:
# 输入: [[1,1],[2,2],[3,3]]
# 输出: 3
# 解释:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4

# 示例 2:
# 输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出: 4
# 解释:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6

from typing import List
# @lc code=start
from fractions import Fraction
from collections import Counter
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        def K(p1:List[int], p2:List[int]):
            """
            求p1和p2的直线的斜率
            """
            return float("inf") if p1[0] == p2[0] else Fraction(p2[1] - p1[1], p2[0] - p1[0])
        
        N = len(points)
        if N < 3:
            return N

        max_count = 1
        for i in range(N - 1):
            same = sum(1 for j in range(i + 1, N) if points[j] == points[i]) + 1
            kCnt = Counter(K(points[i], points[j]) for j in range(i + 1, N) if points[j] != points[i])
            max_count = max(max_count, same + (kCnt.most_common(1)[0][1] if kCnt else 0) )

        return max_count
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxPoints([[1,1],[2,2],[3,3]]))
    print(solution.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))