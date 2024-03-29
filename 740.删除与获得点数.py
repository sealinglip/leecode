#
# @lc app=leetcode.cn id=740 lang=python3
#
# [740] 删除与获得点数
#
# 给你一个整数数组 nums ，你可以对它进行一些操作。
# 每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] + 1 的元素。
# 开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。


# 示例 1：
# 输入：nums = [3, 4, 2]
# 输出：6
# 解释：
# 删除 4 获得 4 个点数，因此 3 也被删除。
# 之后，删除 2 获得 2 个点数。总共获得 6 个点数。

# 示例 2：
# 输入：nums = [2, 2, 3, 3, 3, 4]
# 输出：9
# 解释：
# 删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
# 之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
# 总共获得 9 个点数。


# 提示：
# 1 <= nums.length <= 2 * 10^4
# 1 <= nums[i] <= 10^4

from typing import List
# @lc code=start
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        keys = list(cnt.keys())
        keys.sort()

        dp = [0, 0]
        # 记dp[0] 为keys[:i] 在不选keys[i]时最多可得，dp[1] 为keys[:i] 在选keys[i]时最多可得
        prev = None
        for k in keys:
            if prev is not None and prev == k - 1:
                # 选了prev就不能选k
                tmp = dp[0]
                dp[0] = max(dp[0], dp[1])
                dp[1] = tmp + k * cnt[k]
            else:
                dp[0] = max(dp[0], dp[1])
                dp[1] = dp[0] + k * cnt[k]
            prev = k

        return max(dp)

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.deleteAndEarn([3, 4, 2]))
    print(solution.deleteAndEarn([2, 2, 3, 3, 3, 4]))
