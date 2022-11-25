#
# @lc app=leetcode.cn id=795 lang=python3
#
# [795] 区间子数组个数
#
# 给你一个整数数组 nums 和两个整数：left 及 right 。找出 nums 中连续、非空且其中最大元素在范围[left, right] 内的子数组，并返回满足条件的子数组的个数。

# 生成的测试用例保证结果符合 32-bit 整数范围。


# 示例 1：
# 输入：nums = [2, 1, 4, 3], left = 2, right = 3
# 输出：3
# 解释：满足条件的三个子数组：[2], [2, 1], [3]

# 示例 2：
# 输入：nums = [2, 9, 2, 5, 6], left = 2, right = 8
# 输出：7


# 提示：
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
# 0 <= left <= right <= 10^9

# 复习


from typing import List
# @lc code=start


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res = 0
        lb = pb = -1  # 记录第一个不大于right的元素，和最后一个在[left, right]之间的元素
        for i, n in enumerate(nums):
            if n <= right:
                if lb == -1:
                    lb = i
                if left <= n:
                    pb = i
                # 以[lb, pb]为左边界，i为右边界，构成新的符合条件的子数组
                if pb != -1:
                    res += (pb - lb + 1)
            elif lb != -1:
                lb = pb = -1

        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.numSubarrayBoundedMax(
        [16, 69, 88, 85, 79, 87, 37, 33, 39, 34], 55, 57))  # 0
    print(solution.numSubarrayBoundedMax([2, 1, 4, 3], 2, 3))  # 3
    print(solution.numSubarrayBoundedMax([7, 3, 6, 7, 1], 1, 4))  # 2
    print(solution.numSubarrayBoundedMax(
        [2, 9, 2, 5, 6], 2, 8))  # 7
