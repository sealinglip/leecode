#
# @lc app=leetcode.cn id=891 lang=python3
#
# [891] 子序列宽度之和
#
# 一个序列的 宽度 定义为该序列中最大元素和最小元素的差值。

# 给你一个整数数组 nums ，返回 nums 的所有非空 子序列 的 宽度之和 。由于答案可能非常大，请返回对 109 + 7 取余 后的结果。

# 子序列 定义为从一个数组里删除一些（或者不删除）元素，但不改变剩下元素的顺序得到的数组。例如，[3, 6, 2, 7] 就是数组[0, 3, 1, 6, 2, 2, 7] 的一个子序列。


# 示例 1：
# 输入：nums = [2, 1, 3]
# 输出：6
# 解释：子序列为[1], [2], [3], [2, 1], [2, 3], [1, 3], [2, 1, 3] 。
# 相应的宽度是 0, 0, 0, 1, 1, 2, 2 。
# 宽度之和是 6 。

# 示例 2：
# 输入：nums = [2]
# 输出：0


# 提示：
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5

# Hard


from typing import List
# @lc code=start


class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        # 题目中要求顺序不能改变
        # 但实际上，不排序的子序列一定对应一个排序后的子序列，所以数组先排序在求解，答案是一样的
        nums.sort()

        # 对于任意子序列，设起止索引为i，j，这样的子序列共有 2 ^ (j-i-1) 个
        # 对于任意一个位置而言，设其索引为i，则以i为最大值的子序列有 2 ^ i 个，以i为最小值的子序列有 2 ^ (n-i-1) 个
        res = 0
        n = len(nums)
        for i, num in enumerate(nums):
            res = (res + ((1 << i) - (1 << (n-i-1))) * num) % MOD

        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.sumSubseqWidths([2, 1, 3]))  # 6
    print(solution.sumSubseqWidths([3]))  # 0
