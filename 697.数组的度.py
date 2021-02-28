#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#
# 给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。
# 你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

# 示例 1：
# 输入：[1, 2, 2, 3, 1]
# 输出：2
# 解释：
# 输入数组的度是2，因为元素1和2的出现频数最大，均为2.
# 连续子数组里面拥有相同度的有如下所示:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组[2, 2]的长度为2，所以返回2.

# 示例 2：
# 输入：[1, 2, 2, 3, 1, 4, 2]
# 输出：6

# 提示：
# nums.length 在1到 50, 000 区间范围内。
# nums[i] 是一个在 0 到 49, 999 范围内的整数。

from typing import List
# @lc code=start


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hash = {}

        maxCnt = 0
        for i, num in enumerate(nums):
            info = hash.get(num, [0, i, i])
            if num not in hash:
                hash[num] = info
            info[2] = i
            info[0] += 1
            if info[0] > maxCnt:
                maxCnt = info[0]

        minSpan = len(nums)
        for key in hash:
            info = hash[key]
            if info[0] == maxCnt:
                span = info[2] - info[1] + 1
                if span < minSpan:
                    minSpan = span

        return minSpan

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findShortestSubArray([1, 2, 2, 3, 1]))
    print(solution.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))
