#
# @lc app=leetcode.cn id=719 lang=python3
#
# [719] 找出第 k 小的距离对
#
# 给定一个整数数组，返回所有数对之间的第 k 个最小距离。一对(A, B) 的距离被定义为 A 和 B 之间的绝对差值。

# 示例 1:
# 输入：
# nums = [1, 3, 1]
# k = 1
# 输出：0
# 解释：
# 所有数对如下：
# (1, 3) -> 2
# (1, 1) -> 0
# (3, 1) -> 2
# 因此第 1 个最小距离的数对是(1, 1)，它们之间的距离为 0。

# 提示:
# 2 <= len(nums) <= 10000.
# 0 <= nums[i] < 1000000.
# 1 <= k <= len(nums) * (len(nums) - 1) / 2.

# Hard

from typing import List
# @lc code=start


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count(mid: int) -> int:
            cnt = i = 0
            for j, num in enumerate(nums):
                while num - nums[i] > mid:
                    i += 1
                cnt += j - i
            return cnt

        nums.sort()
        # return bisect_left(range(nums[-1] - nums[0]), k, key=count)
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) >> 1
            if count(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo

        # @lc code=end
