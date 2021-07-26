# 统计一个数字在排序数组中出现的次数。

# 示例 1:
# 输入: nums = [5, 7, 7, 8, 8, 10], target = 8
# 输出: 2

# 示例 2:
# 输入: nums = [5, 7, 7, 8, 8, 10], target = 6
# 输出: 0

# 限制：
# 0 <= 数组长度 <= 50000

# 注意：本题与主站 34 题相同（仅返回值不同）：https: // leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List
from bisect import bisect_left


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = bisect_left(nums, target)
        N = len(nums)
        if i != N and nums[i] == target:
            count = 1
            i += 1
            while i < N and nums[i] == target:
                count += 1
                i += 1
            return count
        else:
            return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.search([5, 7, 7, 8, 8, 10], 8))
    print(solution.search([5, 7, 7, 8, 8, 10], 6))
