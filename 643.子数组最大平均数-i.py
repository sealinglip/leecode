#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#
# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

# 示例：
# 输入：[1, 12, -5, -6, 50, 3], k = 4
# 输出：12.75
# 解释：最大平均数(12-5-6+50)/4 = 51/4 = 12.75


# 提示：
# 1 <= k <= n <= 30, 000。
# 所给数据范围[-10, 000，10, 000]。

from typing import List
# @lc code=start


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = nums[:k]
        total = sum(window)
        N = len(nums)
        maxTotal = total
        for i in range(N - k + 1):
            if total > maxTotal:
                maxTotal = total

            if i < N - k:
                total -= nums[i]
                total += nums[i + k]

        return maxTotal / k

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxAverage([-1], 1))
    print(solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
