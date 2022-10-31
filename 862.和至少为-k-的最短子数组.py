#
# @lc app=leetcode.cn id=862 lang=python3
#
# [862] 和至少为 K 的最短子数组
#
# 给你一个整数数组 nums 和一个整数 k ，找出 nums 中和至少为 k 的 最短非空子数组 ，并返回该子数组的长度。如果不存在这样的 子数组 ，返回 -1 。

# 子数组 是数组中 连续 的一部分。


# 示例 1：
# 输入：nums = [1], k = 1
# 输出：1

# 示例 2：
# 输入：nums = [1,2], k = 4
# 输出：-1

# 示例 3：
# 输入：nums = [2,-1,2], k = 3
# 输出：3


# 提示：
# 1 <= nums.length <= 10^5
# -10^5 <= nums[i] <= 10^5
# 1 <= k <= 10^9

# Hard
# 复习

from collections import deque
from typing import List

# @lc code=start


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preSum = [0]
        curSum = 0
        for i, num in enumerate(nums):
            preSum.append(preSum[-1] + num)

        # q中保存可以与后面的位置配对，差 > k 即得到满足条件的子数组
        q = deque()
        res = n + 1
        for i, s in enumerate(preSum):
            while q and s - preSum[q[0]] >= k:
                # 当前位置和队首
                res = min(res, i - q.popleft())
            while q and preSum[q[-1]] >= s:
                q.pop()
            q.append(i)
        return res if res <= n else -1

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.shortestSubarray([1, 1, 1, -2, 4], 3))
