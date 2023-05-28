#
# @lc app=leetcode.cn id=1027 lang=python3
#
# [1027] 最长等差数列
#
# 给你一个整数数组 nums，返回 nums 中最长等差子序列的长度。

# 回想一下，nums 的子序列是一个列表 nums[i1], nums[i2], ..., nums[ik] ，且 0 <= i1 < i2 < ... < ik <= nums.length - 1。并且如果 seq[i+1] - seq[i](0 <= i < seq.length - 1) 的值都相同，那么序列 seq 是等差的。


# 示例 1：
# 输入：nums = [3, 6, 9, 12]
# 输出：4
# 解释：
# 整个数组是公差为 3 的等差数列。

# 示例 2：
# 输入：nums = [9, 4, 7, 2, 10]
# 输出：3
# 解释：
# 最长的等差子序列是[4, 7, 10]。

# 示例 3：
# 输入：nums = [20, 1, 15, 3, 10, 5, 8]
# 输出：4
# 解释：
# 最长的等差子序列是[20, 15, 10, 5]。


# 提示：
# 2 <= nums.length <= 1000
# 0 <= nums[i] <= 500


from math import inf
from typing import List
# @lc code=start


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # 动态规划
        # 记dp(i, j)为以数字i结尾，等差为j的序列长度
        # 边界：第一个元素，任意步长的的等差序列长度都是1，用inf表示任意步长
        dp = {(nums[0], inf): 1}

        uni = set()  # 去重
        uni.add(nums[0])
        for i in range(1, len(nums)):
            num = nums[i]
            dp[(num, inf)] = 1
            for pre in uni:
                dp[(num, num-pre)] = dp.get((pre, num-pre),
                                            dp.get((pre, inf), 0)) + 1

            uni.add(nums[i])
        # for k, v in dp.items():
        #     print("%s: %d" % (str(k), v))
        return max(dp.values())

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestArithSeqLength([1, 2, 1, 2, 3, 2, 4, 2, 8]))  # 4
    print(solution.longestArithSeqLength([12, 28, 13, 6, 34, 36, 53, 24, 29, 2, 23, 0, 22, 25, 53, 34, 23, 50, 35, 43, 53, 11, 48, 56, 44, 53,
          31, 6, 31, 57, 46, 6, 17, 42, 48, 28, 5, 24, 0, 14, 43, 12, 21, 6, 30, 37, 16, 56, 19, 45, 51, 10, 22, 38, 39, 23, 8, 29, 60, 18]))  # 4
    print(solution.longestArithSeqLength([3, 6, 9, 12]))  # 4
    print(solution.longestArithSeqLength([9, 4, 7, 2, 10]))  # 3
    print(solution.longestArithSeqLength([20, 1, 15, 3, 10, 5, 8]))  # 4
