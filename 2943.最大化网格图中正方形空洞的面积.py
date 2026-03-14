#
# @lc app=leetcode.cn id=2943 lang=python3
#
# [2943] 最大化网格图中正方形空洞的面积
#
# https://leetcode.cn/problems/maximize-area-of-square-hole-in-grid/description/
#
# algorithms
# Medium (39.91%)
# Likes:    18
# Dislikes: 0
# Total Accepted:    8.4K
# Total Submissions: 16.3K
# Testcase Example:  '2\n1\n[2,3]\n[2]'
#
# 给你两个整数 n 和 m，以及两个整数数组 hBars 和 vBars。网格由 n + 2 条水平线和 m + 2 条竖直线组成，形成 1x1
# 的单元格。网格中的线条从 1 开始编号。
# 
# 你可以从 hBars 中 删除 一些水平线条，并从 vBars 中删除一些竖直线条。注意，其他线条是固定的，无法删除。
# 返回一个整数表示移除一些线条（可以不移除任何线条）后，网格中 正方形空洞的最大面积 。
# 
# 
# 示例 1：
# 输入: n = 2, m = 1, hBars = [2,3], vBars = [2]
# 输出: 4
# 解释:
# 左侧图片展示了网格的初始状态。水平线是 [1,2,3,4]，竖直线是 [1,2,3]。
# 构造最大正方形空洞的一种方法是移除水平线 2 和竖直线 2。
# 
# 示例 2：
# 输入: n = 1, m = 1, hBars = [2], vBars = [2]
# 输出: 4
# 解释:
# 移除水平线 2 和竖直线 2，可以得到最大正方形空洞。
# 
# 示例 3：
# 输入: n = 2, m = 3, hBars = [2,3], vBars = [2,4]
# 输出: 4
# 解释:
# 构造最大正方形空洞的一种方法是移除水平线 3 和竖直线 4。
# 
# 
# 提示：
# 1 <= n <= 10^9
# 1 <= m <= 10^9
# 1 <= hBars.length <= 100
# 2 <= hBars[i] <= n + 1
# 1 <= vBars.length <= 100
# 2 <= vBars[i] <= m + 1
# hBars 中所有值互不相同。
# vBars 中所有值互不相同。
# 
# 
#

from typing import List
# @lc code=start
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()

        def maxConsecutiveNums(bars: List[int]) -> int:
            res = cur = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i-1] + 1:
                    cur += 1
                else:
                    cur = 1
                res = max(res, cur)
            return res
        
        return (min(maxConsecutiveNums(hBars), maxConsecutiveNums(vBars)) + 1) ** 2
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximizeSquareHoleArea(3, 2, [3,2,4], [3,2])) # 9
    print(solution.maximizeSquareHoleArea(2, 1, [2,3], [2])) # 4
    print(solution.maximizeSquareHoleArea(1, 1, [2], [2])) # 4
    print(solution.maximizeSquareHoleArea(2, 3, [2,3], [2,4])) # 4
