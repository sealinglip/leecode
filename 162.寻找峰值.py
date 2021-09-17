#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#
# 峰值元素是指其值严格大于左右相邻值的元素。
# 给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
# 你可以假设 nums[-1] = nums[n] = -∞ 。
# 你必须实现时间复杂度为 O(log n) 的算法来解决此问题。


# 示例 1：
# 输入：nums = [1, 2, 3, 1]
# 输出：2
# 解释：3 是峰值元素，你的函数应该返回其索引 2。

# 示例 2：
# 输入：nums = [1, 2, 1, 3, 5, 6, 4]
# 输出：1 或 5
# 解释：你的函数可以返回索引 1，其峰值元素为 2；
# 或者返回索引 5， 其峰值元素为 6。


# 提示：
# 1 <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
# 对于所有有效的 i 都有 nums[i] != nums[i + 1]

from typing import List
# @lc code=start


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1 or nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return N - 1

        def findPeak(l: int, r: int) -> int:
            '''
            查找区间[l, r]之间的峰值
            '''
            if l + 2 == r:
                if nums[l] < nums[l + 1] and nums[r] < nums[l + 1]:
                    return l + 1
                else:
                    return None
            if l + 3 == r:
                if nums[l] < nums[l + 1] and nums[l + 2] < nums[l + 1]:
                    return l + 1
                elif nums[r] < nums[l + 2] and nums[l + 2] > nums[l + 1]:
                    return l + 2
                else:
                    return None
            else:
                m = (l + r) >> 1
                if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
                    return m
                else:
                    res = findPeak(l, m)
                    if res is not None:
                        return res
                    else:
                        return findPeak(m, r)

        return findPeak(0, N - 1)

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findPeakElement([1, 2, 3, 1]))  # 2
    print(solution.findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # 1 or 5
