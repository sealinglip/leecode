#
# @lc app=leetcode.cn id=2132 lang=python3
#
# [2132] 用邮票贴满网格图
#
# 给你一个 m x n 的二进制矩阵 grid ，每个格子要么为 0 （空）要么为 1 （被占据）。

# 给你邮票的尺寸为 stampHeight x stampWidth 。我们想将邮票贴进二进制矩阵中，且满足以下 限制 和 要求 ：

# 覆盖所有 空 格子。
# 不覆盖任何 被占据 的格子。
# 我们可以放入任意数目的邮票。
# 邮票可以相互有 重叠 部分。
# 邮票不允许 旋转 。
# 邮票必须完全在矩阵 内 。
# 如果在满足上述要求的前提下，可以放入邮票，请返回 true ，否则返回 false 。


# 示例 1：
# 输入：grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]], stampHeight = 4, stampWidth = 3
# 输出：true
# 解释：我们放入两个有重叠部分的邮票（图中标号为 1 和 2），它们能覆盖所有与空格子。

# 示例 2：
# 输入：grid = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], stampHeight = 2, stampWidth = 2 
# 输出：false 
# 解释：没办法放入邮票覆盖所有的空格子，且邮票不超出网格图以外。
 
# 提示：
# m == grid.length
# n == grid[r].length
# 1 <= m, n <= 10^5
# 1 <= m * n <= 2 * 10^5
# grid[r][c] 要么是 0 ，要么是 1 。
# 1 <= stampHeight, stampWidth <= 10^5

# Hard
# 二维差分

from typing import List
# @lc code=start
class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])

        # 计算grid前缀和
        s = [[0] * (n+1) for _ in range(m+1)]
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                s[i+1][j+1] = s[i+1][j] + s[i][j+1] - s[i][j] + cell
        
        # 计算二维差分
        d = [[0] * (n+2) for _ in range(m+2)] # 为了方便下一步计算，这里在左和上分别加了一列和一行，下标相应加一
        for i in range(stampHeight, m+1):
            for j in range(stampWidth, n+1):
                i1 = i - stampHeight + 1
                j1 = j - stampWidth + 1
                if s[i][j] - s[i][j1-1] - s[i1-1][j] + s[i1-1][j1-1] == 0:
                    # 判断有能贴邮票的空间，就贴一张
                    d[i1][j1] += 1
                    d[i1][j+1] -= 1
                    d[i+1][j1] -= 1
                    d[i+1][j+1] += 1

        # 从d可以还原出每格贴邮票的张数，如果有格原来为空，但现在贴的张数也为0，则说明没覆盖到
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                d[i+1][j+1] += d[i+1][j] + d[i][j+1] - d[i][j]
                if cell == 0 and d[i+1][j+1] == 0:
                    return False
                
        return True

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.possibleToStamp([[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]], 4, 3)) # True
    print(solution.possibleToStamp([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], 2, 2)) # False
