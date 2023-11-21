#
# @lc app=leetcode.cn id=2216 lang=python3
#
# [2216] 美化数组的最少删除数
#
# 给你一个下标从 0 开始的整数数组 nums ，如果满足下述条件，则认为数组 nums 是一个 美丽数组 ：

# nums.length 为偶数
# 对所有满足 i % 2 == 0 的下标 i ，nums[i] != nums[i + 1] 均成立
# 注意，空数组同样认为是美丽数组。

# 你可以从 nums 中删除任意数量的元素。当你删除一个元素时，被删除元素右侧的所有元素将会向左移动一个单位以填补空缺，而左侧的元素将会保持 不变 。

# 返回使 nums 变为美丽数组所需删除的 最少 元素数目。

# 示例 1：
# 输入：nums = [1,1,2,3,5]
# 输出：1
# 解释：可以删除 nums[0] 或 nums[1] ，这样得到的 nums = [1,2,3,5] 是一个美丽数组。可以证明，要想使 nums 变为美丽数组，至少需要删除 1 个元素。

# 示例 2：
# 输入：nums = [1,1,2,2,3,3]
# 输出：2
# 解释：可以删除 nums[0] 和 nums[5] ，这样得到的 nums = [1,2,2,3] 是一个美丽数组。可以证明，要想使 nums 变为美丽数组，至少需要删除 2 个元素。
 
# 提示：
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5

# 复习

from math import inf
from typing import List

# @lc code=start
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        # 下面的解法会TLE
        # if n < 2:
        #     return n
        # # 从后往前遍历，每个元素或删或留
        # # 记dp(i)为nums[i:]保留nums[i]，要变成美丽数组需要删除的最少元素个数
        # # 状态转移方程为：
        # # dp(n) = 0, dp(n-1) = ∞
        # # dp(i) = min(dp(j) + (j-i-2) if nums[k] != nums[i])  i < k < j <= n 
        # # or dp(i) = ∞ 如果找不到符合条件的i，k，j
        # dp = [inf] * (n+1)
        # dp[-1] = 0
        # for i in range(n-2, -1, -1):
        #     mi = dp[i]
        #     hasK = False # 有没有找到符合条件的k
        #     for j in range(i+2, n+1):
        #         if not hasK and nums[i] != nums[j-1]:
        #             hasK = True
        #         if hasK:
        #             mi = min(mi, dp[j] + (j - i - 2))
        #     dp[i] = mi

        # return min(dp[i] + i for i in range(n))

        cnt = 0
        even = True
        for i in range(n-1):
            if even and nums[i] == nums[i+1]:
                cnt += 1
            else:
                even = not even

        if (n - cnt) % 2 != 0:
            cnt += 1

        return cnt

# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.minDeletion([1,1,2,2,3,3])) # 2
    print(solution.minDeletion([1,1,2,3,5])) # 1
    print(solution.minDeletion([])) # 0
