#
# @lc app=leetcode.cn id=525 lang=python3
#
# [525] 连续数组
#
# 给定一个二进制数组 nums, 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。

# 示例 1:
# 输入: nums = [0, 1]
# 输出: 2
# 说明: [0, 1] 是具有相同数量0和1的最长连续子数组。

# 示例 2:
# 输入: nums = [0, 1, 0]
# 输出: 2
# 说明: [0, 1](或[1, 0]) 是具有相同数量0和1的最长连续子数组。

# 提示：
# 1 <= nums.length <= 10^5
# nums[i] 不是 0 就是 1

from typing import List
# @lc code=start


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff = 0
        hash = {0: -1}
        maxSpan = 0
        for i, num in enumerate(nums):
            diff += num if num else -1

            if diff in hash:
                span = i - hash[diff]
                if span > maxSpan:
                    maxSpan = span
            else:
                hash[diff] = i

        return maxSpan

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxLength([0, 1]))
    print(solution.findMaxLength([0, 1, 0]))
