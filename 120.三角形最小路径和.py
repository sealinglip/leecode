#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
# https://leetcode.cn/problems/triangle/description/
#
# algorithms
# Medium (69.29%)
# Likes:    1483
# Dislikes: 0
# Total Accepted:    446.7K
# Total Submissions: 641.5K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# 给定一个三角形 triangle ，找出自顶向下的最小路径和。
# 
# 每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1
# 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
# 
# 
# 
# 示例 1：
# 输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# 输出：11
# 解释：如下面简图所示：
# ⁠  2
# ⁠ 3 4
# ⁠6 5 7
# 4 1 8 3
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
# 
# 示例 2：
# 输入：triangle = [[-10]]
# 输出：-10
# 
# 
# 提示：
# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -10^4 <= triangle[i][j] <= 10^4
# 
# 
# 
# 
# 进阶：
# 你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？
# 
# 
#

from typing import List

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 记dp(i)为走到当前层的第i个点的最短路径
        # 那么结果为最后一层的min(dp)
        n = len(triangle)
        dp = [0] * n
        for i, row in enumerate(triangle):
            newDp = [0] * n
            for j, x in enumerate(row):
                if j == 0:
                    newDp[j] = x + dp[j]
                elif j == i:
                    newDp[j] = x + dp[j-1]
                else:
                    newDp[j] = x + min(dp[j-1], dp[j])
            dp = newDp
        return min(dp) 

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])) # 11
    print(solution.minimumTotal([[-10]])) # -10
