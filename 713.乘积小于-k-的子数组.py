#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于 K 的子数组
#
# 给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。


# 示例 1：
# 输入：nums = [10, 5, 2, 6], k = 100
# 输出：8
# 解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2], 、[6]、[10, 5]、[5, 2]、[2, 6]、[5, 2, 6]。
# 需要注意的是[10, 5, 2] 并不是乘积小于 100 的子数组。

# 示例 2：
# 输入：nums = [1, 2, 3], k = 0
# 输出：0


# 提示:
# 1 <= nums.length <= 3 * 10^4
# 1 <= nums[i] <= 1000
# 0 <= k <= 10^6

# 复习

from typing import List
# @lc code=start


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 求前缀积可能会越界，所以不能这么搞
        # 双指针倒是可以
        cnt = 0
        l, r, n = 0, 0, len(nums)
        product = 1

        # 下面的实现写得不够简洁
        # while r < n:
        #     if l < r and product * nums[r] >= k:
        #         product //= nums[l]
        #         l += 1

        #     while r < n and product * nums[r] < k:
        #         product *= nums[r]
        #         r += 1

        #     cnt += r - l  # 所有左边界是l（inclusive）且满足题目要求的子数组
        #     if l == r:
        #         r += 1
        #         product = nums[l]

        # if l < r:
        #     # 再加上 r - l - 1 一直加到 1
        #     cnt += (r - l)*(r - l - 1) // 2

        for r in range(n):
            product *= nums[r]
            while l <= r and product >= k:
                product //= nums[l]
                l += 1
            cnt += r - l + 1  # 所有右边界是r（inclusive）且满足题目要求的子数组

        return cnt

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.numSubarrayProductLessThanK(
        [57, 44, 92, 28, 66, 60, 37, 33, 52, 38, 29, 76, 8, 75, 22], 18))  # 1
    print(solution.numSubarrayProductLessThanK(
        [10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3], 19))  # 18
    print(solution.numSubarrayProductLessThanK([10, 5, 2, 6], 100))  # 8
    print(solution.numSubarrayProductLessThanK([1, 2, 3], 0))  # 0
