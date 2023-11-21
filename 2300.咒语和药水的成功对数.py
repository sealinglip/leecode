#
# @lc app=leetcode.cn id=2300 lang=python3
#
# [2300] 咒语和药水的成功对数
#
# 给你两个正整数数组 spells 和 potions ，长度分别为 n 和 m ，其中 spells[i] 表示第 i 个咒语的能量强度，
# potions[j] 表示第 j 瓶药水的能量强度。
# 同时给你一个整数 success 。一个咒语和药水的能量强度 相乘 如果 大于等于 success ，那么它们视为一对 成功 的组合。
# 请你返回一个长度为 n 的整数数组 pairs，其中 pairs[i] 是能跟第 i 个咒语成功组合的 药水 数目。

# 示例 1：
# 输入：spells = [5,1,3], potions = [1,2,3,4,5], success = 7
# 输出：[4,0,3]
# 解释：
# - 第 0 个咒语：5 * [1,2,3,4,5] = [5,10,15,20,25] 。总共 4 个成功组合。
# - 第 1 个咒语：1 * [1,2,3,4,5] = [1,2,3,4,5] 。总共 0 个成功组合。
# - 第 2 个咒语：3 * [1,2,3,4,5] = [3,6,9,12,15] 。总共 3 个成功组合。
# 所以返回 [4,0,3] 。

# 示例 2：
# 输入：spells = [3,1,2], potions = [8,5,8], success = 16
# 输出：[2,0,2]
# 解释：
# - 第 0 个咒语：3 * [8,5,8] = [24,15,24] 。总共 2 个成功组合。
# - 第 1 个咒语：1 * [8,5,8] = [8,5,8] 。总共 0 个成功组合。
# - 第 2 个咒语：2 * [8,5,8] = [16,10,16] 。总共 2 个成功组合。
# 所以返回 [2,0,2] 。
 

# 提示：
# n == spells.length
# m == potions.length
# 1 <= n, m <= 10^5
# 1 <= spells[i], potions[i] <= 10^5
# 1 <= success <= 10^10

# 复习

from bisect import bisect_left
from collections import Counter
from math import ceil
from typing import List
# @lc code=start
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)
        # c = Counter(potions)
        # indices = sorted(c) # potion去重清单
        # cnt = [c[i] for i in indices]
        
        # 下面这个解法会TLE
        # res = []
        # for s in spells:
        #     k = ceil(success / s)
        #     res.append(sum(cnt[bisect_left(indices, k):]))
        
        # 优化spells的处理——还是会TLE
        # res = [0] * len(spells)
        # spells = sorted((x, i) for i, x in enumerate(spells))
        # lb = ceil(success / indices[-1]) # 小于lb的spell，组合数量一定是0
        # ub = ceil(success / indices[0]) # 大于等于ub的spell，组合数量一定是potions的长度
        # start = bisect_left(spells, (lb, 0))
        # end = bisect_left(spells, (ub, 0))
        # for i in range(start, end):
        #     s, pos = spells[i]
        #     k = ceil(success / s)
        #     res[pos] = sum(cnt[bisect_left(indices, k):])

        # for i in range(end, n):
        #     _, pos = spells[i]
        #     res[pos] = m

        # return res

        # 粗暴一点
        potions.sort()
        return [m - bisect_left(potions, ceil(success / s)) for s in spells]

    
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.successfulPairs([5,1,1,1,20,19,59,60,5,23,25,28,34,1,1], [1,2,3,2,1], 59)) # [0, 0, 0, 0, 1, 0, 5, 5, 0, 1, 1, 1, 3, 0, 0]
    print(solution.successfulPairs([5,1,3], [1,2,3,4,5], 7)) # [4,0,3]
    print(solution.successfulPairs([3,1,2], [8,5,8], 16)) # [2,0,2]