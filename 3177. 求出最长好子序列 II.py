# 给你一个整数数组 nums 和一个 非负 整数 k 。如果一个整数序列 seq 满足在范围下标范围 [0, seq.length - 2] 中存在 不超过 k 个下标 i 满足 seq[i] != seq[i + 1] ，那么我们称这个整数序列为 好 序列。

# 请你返回 nums 中 好 
# 子序列
#  的最长长度

# 示例 1：
# 输入：nums = [1,2,1,1,3], k = 2
# 输出：4
# 解释：
# 最长好子序列为 [1,2,1,1,3] 。

# 示例 2：
# 输入：nums = [1,2,3,4,5,1], k = 0
# 输出：2
# 解释：
# 最长好子序列为 [1,2,3,4,5,1] 。

# 提示：
# 1 <= nums.length <= 5 * 10^3
# 1 <= nums[i] <= 10^9
# 0 <= k <= min(50, nums.length)

# Hard

from collections import defaultdict
from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # 动规
        # 记dp(i,j)为以nums[i]结尾，有j个不满足约定条件的位置的最长子序列长度
        # 有 dp(i,0) >= 1
        # dp(i,j) = max(dp(x, j-(nums[x] != nums[i])) for x in range(i)) + 1
        # 记zd[j] 表示枚举到位置 i 之前，有 j 个数字与其在序列中的后一个不相等的最长合法序列的长度
        # 则当nums[x] != nums[i]时，有dp(i,j) = zd[j-1] + 1 
        # 当nums[x] == nums[i]时 
        # 
        dp = defaultdict(lambda: [0] * (k+1))
        zd = [0] * (k+1)

        for v in nums:
            tmp = dp[v]
            for j in range(k+1):
                tmp[j] += 1
                if j > 0:
                    tmp[j] = max(tmp[j], zd[j-1] + 1)
            for j in range(k+1):
                zd[j] = max(zd[j], tmp[j])

        return zd[k]

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumLength([1,2,1,1,3], 2)) # 4
    print(solution.maximumLength([1,2,3,4,5,1], 0)) # 2