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
# 1 <= nums.length <= 500
# 1 <= nums[i] <= 10^9
# 0 <= k <= min(nums.length, 25)

from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # 动规
        # 记dp(i,j)为以nums[i]结尾，有j个不满足约定条件的位置的最长子序列长度
        # 有 dp(i,0) >= 1
        # dp(i,j) = max(dp(x, j-(nums[x] != nums[i]))) + 1 for x in range(i)
        n = len(nums)
        dp = [[-1] * (k+1) for _ in range(n)]

        res = 0

        for i in range(n):
            dp[i][0] = 1
            for j in range(k+1):
                for x in range(i):
                    delta = 1 if nums[i] != nums[x] else 0
                    if j >= delta and dp[x][j-delta] != -1:
                        dp[i][j] = max(dp[i][j], dp[x][j-delta] + 1)
                res = max(res, dp[i][j])

        return res
                    

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumLength([29,30,30], 0)) # 2
    print(solution.maximumLength([1,2,1,1,3], 2)) # 4
    print(solution.maximumLength([1,2,3,4,5,1], 0)) # 2
