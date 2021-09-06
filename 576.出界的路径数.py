#
# @lc app=leetcode.cn id=576 lang=python3
#
# [576] 出界的路径数
#
# 给你一个大小为 m x n 的网格和一个球。球的起始坐标为[startRow, startColumn] 。你可以将球移到在四个方向上相邻的单元格内（可以穿过网格边界到达网格之外）。你 最多 可以移动 maxMove 次球。
# 给你五个整数 m、n、maxMove、startRow 以及 startColumn ，找出并返回可以将球移出边界的路径数量。因为答案可能非常大，返回对 109 + 7 取余 后的结果。


# 示例 1：
# 输入：m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# 输出：6

# 示例 2：
# 输入：m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# 输出：12


# 提示：
# 1 <= m, n <= 50
# 0 <= maxMove <= 50
# 0 <= startRow < m
# 0 <= startColumn < n


# @lc code=start
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7

        cache = {}

        def paths(maxMove: int, r: int, c: int):
            if 0 <= r < m and 0 <= c < n:
                if maxMove:
                    key = (maxMove, r, c)
                    if key in cache:
                        return cache[key]
                    maxMove -= 1
                    sum = paths(maxMove, r + 1, c) + paths(maxMove, r - 1, c) \
                        + paths(maxMove, r, c + 1) + paths(maxMove, r, c - 1)
                    sum %= MOD
                    cache[key] = sum
                    return sum
                else:
                    return 0
            else:
                return 1

        return paths(maxMove, startRow, startColumn)

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findPaths(2, 2, 2, 0, 0))
    print(solution.findPaths(1, 3, 3, 0, 1))
