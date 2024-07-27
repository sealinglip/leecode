#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心下标
#
# 给你一个整数数组 nums ，请计算数组的 中心下标 。
# 数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。
# 如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。
# 如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1 。

# 示例 1：
# 输入：
# nums = [1, 7, 3, 6, 5, 6]
# 输出：3
# 解释：
# 索引 3 (nums[3]=6) 的左侧数之和(1 + 7 + 3=11)，与右侧数之和(5 + 6=11) 相等。
# 同时, 3 也是第一个符合要求的中心索引。

# 示例 2：
# 输入：
# nums = [1, 2, 3]
# 输出：- 1
# 解释：
# 数组中不存在满足此条件的中心索引。

# 说明：
# nums 的长度范围为[0, 10000]。
# 任何一个 nums[i] 将会是一个范围在[-1000, 1000]的整数。

from typing import List
# @lc code=start


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1

        total = sum(nums)
        N = len(nums)
        s = 0
        for i in range(N):
            if (s << 1) + nums[i] == total:
                return i
            s += nums[i]

        return -1
# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.pivotIndex([-1, -1, -1, -1, -1, 0]))
    print(solution.pivotIndex([1, 7, 3, 6, 5, 6]))
    print(solution.pivotIndex([1, 2, 3]))
