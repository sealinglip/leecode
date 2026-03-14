#
# @lc app=leetcode.cn id=1292 lang=python3
#
# [1292] 元素和小于等于阈值的正方形的最大边长
#
# https://leetcode.cn/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/description/
#
# algorithms
# Medium (52.58%)
# Likes:    131
# Dislikes: 0
# Total Accepted:    16.8K
# Total Submissions: 30.7K
# Testcase Example:  '[[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]\n4'
#
# 给你一个大小为 m x n 的矩阵 mat 和一个整数阈值 threshold。
# 
# 请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返回 0 。
# 
# 
# 示例 1：
# 输入：mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# 输出：2
# 解释：总和小于或等于 4 的正方形的最大边长为 2，如图所示。
# 
# 示例 2：
# 输入：mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]],
# threshold = 1
# 输出：0
# 
# 
# 提示：
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 300
# 0 <= mat[i][j] <= 10^4
# 0 <= threshold <= 10^5
# 
# 
#

from typing import List
# @lc code=start
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        # 二维前缀和
        preSum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                preSum[i+1][j+1] = preSum[i+1][j] + preSum[i][j+1] + mat[i][j] - preSum[i][j]

        def check(size: int) -> bool:
            '''
            检查能否边长达到size
            '''
            for i in range(m-size+1):
                for j in range(n-size+1):
                    total = preSum[i+size][j+size] - preSum[i][j+size] - preSum[i+size][j] + preSum[i][j]
                    if total <= threshold:
                        return True
            return False
        
        lo = 0
        hi = min(m, n) + 1
        while lo < hi:
            mi = (lo + hi) >> 1
            if check(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo - 1

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSideLength([[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], 40184)) # 2
    print(solution.maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4)) # 2
    print(solution.maxSideLength([[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], 1)) # 0
