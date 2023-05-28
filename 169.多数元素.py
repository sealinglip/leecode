#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。


# 示例 1：
# 输入：nums = [3, 2, 3]
# 输出：3

# 示例 2：
# 输入：nums = [2, 2, 1, 1, 1, 2, 2]
# 输出：2

# 提示：
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9


# 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
# 复习

from typing import List
# @lc code=start


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = c = 0
        for num in nums:
            if num == n:
                c += 1
            elif c > 0:
                c -= 1
            else:
                n = num
                c = 1
        return n


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.majorityElement([3, 2, 3]))  # 3
    print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2
