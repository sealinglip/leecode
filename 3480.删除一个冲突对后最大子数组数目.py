#
# @lc app=leetcode.cn id=3480 lang=python3
#
# [3480] 删除一个冲突对后最大子数组数目
#
# https://leetcode.cn/problems/maximize-subarrays-after-removing-one-conflicting-pair/description/
#
# algorithms
# Hard (44.68%)
# Likes:    14
# Dislikes: 0
# Total Accepted:    2K
# Total Submissions: 3.4K
# Testcase Example:  '4\n[[2,3],[1,4]]'
#
# 给你一个整数 n，表示一个包含从 1 到 n 按顺序排列的整数数组 nums。此外，给你一个二维数组 conflictingPairs，其中
# conflictingPairs[i] = [a, b] 表示 a 和 b 形成一个冲突对。
# 
# 从 conflictingPairs 中删除 恰好 一个元素。然后，计算数组 nums 中的非空子数组数量，这些子数组都不能同时包含任何剩余冲突对 [a,
# b] 中的 a 和 b。
# 
# 返回删除 恰好 一个冲突对后可能得到的 最大 子数组数量。
# 子数组 是数组中一个连续的 非空 元素序列。
# 
# 
# 示例 1
# 输入： n = 4, conflictingPairs = [[2,3],[1,4]]
# 输出： 9
# 解释：
# 从 conflictingPairs 中删除 [2, 3]。现在，conflictingPairs = [[1, 4]]。
# 在 nums 中，存在 9 个子数组，其中 [1, 4] 不会一起出现。它们分别是 [1]，[2]，[3]，[4]，[1, 2]，[2, 3]，[3,
# 4]，[1, 2, 3] 和 [2, 3, 4]。
# 删除 conflictingPairs 中一个元素后，能够得到的最大子数组数量是 9。
# 
# 示例 2
# 输入： n = 5, conflictingPairs = [[1,2],[2,5],[3,5]]
# 输出： 12
# 解释：
# 从 conflictingPairs 中删除 [1, 2]。现在，conflictingPairs = [[2, 5], [3, 5]]。
# 在 nums 中，存在 12 个子数组，其中 [2, 5] 和 [3, 5] 不会同时出现。
# 删除 conflictingPairs 中一个元素后，能够得到的最大子数组数量是 12。
# 
# 
# 提示：
# 2 <= n <= 10^5
# 1 <= conflictingPairs.length <= 2 * n
# conflictingPairs[i].length == 2
# 1 <= conflictingPairs[i][j] <= n
# conflictingPairs[i][0] != conflictingPairs[i][1]
# 
# 
#

from typing import List
# @lc code=start
class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        bMin1 = [(2 << 31) - 1] * (n + 1)
        bMin2 = [(2 << 31) - 1] * (n + 1)
        for pair in conflictingPairs:
            a = min(pair[0], pair[1])
            b = max(pair[0], pair[1])
            if bMin1[a] > b:
                bMin2[a] = bMin1[a]
                bMin1[a] = b
            elif bMin2[a] > b:
                bMin2[a] = b
        res = 0
        ib1 = n
        b2 = 0x3FFFFFFF
        delCount = [0] * (n + 1)
        for i in range(n, 0, -1):
            if bMin1[ib1] > bMin1[i]:
                b2 = min(b2, bMin1[ib1])
                ib1 = i
            else:
                b2 = min(b2, bMin1[i])
            res += min(bMin1[ib1], n + 1) - i
            delCount[ib1] += min(min(b2, bMin2[ib1]), n + 1) - min(bMin1[ib1], n + 1)
        return res + max(delCount)
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubarrays(4, [[2,3],[1,4]])) # 9
    print(solution.maxSubarrays(5, [[1,2],[2,5],[3,5]])) # 12
