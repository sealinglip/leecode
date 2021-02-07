#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#
# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

# 示例 1:
# 输入: [1, 2, 3]
# 输出: 6

# 示例 2:
# 输入: [1, 2, 3, 4]
# 输出: 24

# 注意:
# 给定的整型数组长度范围是[3, 104]，数组中所有的元素范围是[-1000, 1000]。
# 输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。

from typing import List
# @lc code=start


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        if nums[1] < 0:  # 有负数的情况
            test1 = nums[0] * nums[1] * nums[-1]
            test2 = nums[-1] * nums[-2] * nums[-3]
            return max(test1, test2)
        else:
            return nums[-1] * nums[-2] * nums[-3]

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumProduct([-100, -99, 2, 50, 74]))
