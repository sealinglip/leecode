#
# @lc app=leetcode.cn id=3443 lang=python3
#
# [3443] K 次修改后的最大曼哈顿距离
#
# https://leetcode.cn/problems/maximum-manhattan-distance-after-k-changes/description/
#
# algorithms
# Medium (47.18%)
# Likes:    24
# Dislikes: 0
# Total Accepted:    9K
# Total Submissions: 14.9K
# Testcase Example:  '"NWSE"\n1'
#
# 给你一个由字符 'N'、'S'、'E' 和 'W' 组成的字符串 s，其中 s[i] 表示在无限网格中的移动操作：
# 'N'：向北移动 1 个单位。
# 'S'：向南移动 1 个单位。
# 'E'：向东移动 1 个单位。
# 'W'：向西移动 1 个单位。
# 
# 初始时，你位于原点 (0, 0)。你 最多 可以修改 k 个字符为任意四个方向之一。
# 请找出在 按顺序 执行所有移动操作过程中的 任意时刻 ，所能达到的离原点的 最大曼哈顿距离。
# 曼哈顿距离 定义为两个坐标点 (xi, yi) 和 (xj, yj) 的横向距离绝对值与纵向距离绝对值之和，即 |xi - xj| + |yi - yj|。
# 
# 
# 示例 1：
# 输入：s = "NWSE", k = 1
# 输出：3
# 解释：
# 将 s[2] 从 'S' 改为 'N' ，字符串 s 变为 "NWNE" 。
# 移动操作        位置 (x, y)   曼哈顿距离      最大值
# s[0] == 'N'   (0, 1)        0 + 1 = 1     1
# s[1] == 'W'   (-1, 1)       1 + 1 = 2     2
# s[2] == 'N'   (-1, 2)       1 + 2 = 3     3
# s[3] == 'E'   (0, 2)        0 + 2 = 2     3
# 执行移动操作过程中，距离原点的最大曼哈顿距离是 3 。
# 
# 示例 2：
# 输入：s = "NSWWEW", k = 3
# 输出：6
# 解释：
# 将 s[1] 从 'S' 改为 'N' ，将 s[4] 从 'E' 改为 'W' 。字符串 s 变为 "NNWWWW" 。
# 执行移动操作过程中，距离原点的最大曼哈顿距离是 6 。
# 
# 
# 提示：
# 1 <= s.length <= 10^5
# 0 <= k <= s.length
# s 仅由 'N'、'S'、'E' 和 'W' 。
# 
# 复习

# @lc code=start
from collections import Counter
# DIRS = {'NW': 'SE', 'NE': 'SW', 'SE': 'NW', 'SW': 'NE'}

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        # 方法1：
        # def tryFurthest(dir: str) -> int:
        #     oppositeDir = DIRS[dir]
        #     res = h = v = 0
        #     ops = k
        #     for c in s:
        #         if c == dir[0]:
        #             v += 1
        #         elif c == dir[1]:
        #             h += 1
        #         elif c == oppositeDir[0]:
        #             if ops > 0:
        #                 ops -= 1
        #                 v += 1
        #             else:
        #                 v -= 1
        #         else:
        #             if ops > 0:
        #                 ops -= 1
        #                 h += 1
        #             else:
        #                 h -= 1
        #         res = max(res, abs(h) + abs(v))
        #     return res
        
        # return max(tryFurthest(dir) for dir in DIRS.keys())
    
        # 方法2：
        maxBenefit = k << 1
        res = h = v = 0
        for i, c in enumerate(s):
            if c == 'N':
                v += 1
            elif c == 'S':
                v -= 1
            elif c == 'E':
                h += 1
            else:
                h -= 1
            res = max(res, min(abs(h) + abs(v) + maxBenefit, i+1))
        
        return res


        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDistance("EWWE", 0)) # 1
    print(solution.maxDistance("NWSE", 1)) # 3
    print(solution.maxDistance("NSWWEW", 3)) # 6
