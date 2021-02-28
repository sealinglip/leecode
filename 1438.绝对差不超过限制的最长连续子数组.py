#
# @lc app=leetcode.cn id=1438 lang=python3
#
# [1438] 绝对差不超过限制的最长连续子数组
#
# 给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。
# 如果不存在满足条件的子数组，则返回 0 。

# 示例 1：
# 输入：nums = [8, 2, 4, 7], limit = 4
# 输出：2
# 解释：所有子数组如下：
# [8] 最大绝对差 | 8-8 | = 0 <= 4.
# [8, 2] 最大绝对差 | 8-2 | = 6 > 4.
# [8, 2, 4] 最大绝对差 | 8-2 | = 6 > 4.
# [8, 2, 4, 7] 最大绝对差 | 8-2 | = 6 > 4.
# [2] 最大绝对差 | 2-2 | = 0 <= 4.
# [2, 4] 最大绝对差 | 2-4 | = 2 <= 4.
# [2, 4, 7] 最大绝对差 | 2-7 | = 5 > 4.
# [4] 最大绝对差 | 4-4 | = 0 <= 4.
# [4, 7] 最大绝对差 | 4-7 | = 3 <= 4.
# [7] 最大绝对差 | 7-7 | = 0 <= 4.
# 因此，满足题意的最长子数组的长度为 2 。

# 示例 2：
# 输入：nums = [10, 1, 2, 4, 7, 2], limit = 5
# 输出：4
# 解释：满足题意的最长子数组是[2, 4, 7, 2]，其最大绝对差 | 2-7 | = 5 <= 5 。

# 示例 3：
# 输入：nums = [4, 2, 2, 2, 4, 4, 2, 2], limit = 0
# 输出：3

# 提示：
# 1 <= nums.length <= 10 ^ 5
# 1 <= nums[i] <= 10 ^ 9
# 0 <= limit <= 10 ^ 9

from typing import List
# @lc code=start
from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        N = len(nums)
        s = SortedList()
        l = r = ret = 0  # 移动窗口左右边界
        while r < N:
            s.add(nums[r])
            while s[-1] - s[0] > limit:
                s.remove(nums[l])
                l += 1
            ret = max(ret, r - l + 1)
            r += 1

        return ret

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestSubarray([8, 2, 4, 7], 4))
    print(solution.longestSubarray([10, 1, 2, 4, 7, 2], 5))
    print(solution.longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0))

    nums = list(range(1, pow(10, 4)))
    print(solution.longestSubarray(nums, 5001))
