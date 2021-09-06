#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#
# 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
# 请你找出符合题意的 最短 子数组，并输出它的长度。


# 示例 1：
# 输入：nums = [2,6,4,8,10,9,15]
# 输出：5
# 解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

# 示例 2：
# 输入：nums = [1,2,3,4]
# 输出：0

# 示例 3：
# 输入：nums = [1]
# 输出：0

# 提示：
# 1 <= nums.length <= 10^4
# -10^5 <= nums[i] <= 10^5

# 进阶：你可以设计一个时间复杂度为 O(n) 的解决方案吗？

from typing import List
# @lc code=start
from bisect import bisect


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 分别确定连续子数组的左边界和右边界，设为[l, r]
        # 必须满足nums[l] > min(nums[l:r+1]), nums[r] < max(nums[l:r+1])
        # 且 l == 0 or min(nums[l:r+1]) >= nums[l - 1]
        #    r == len(nums) - 1 or max(nums[l:r+1]) <= nums[r+1]
        N = len(nums)
        # if N < 2:
        #     return 0

        # stack = [(nums[0], 0)]
        # asc = True
        # for i in range(1, N):
        #     n = nums[i]
        #     if asc and n >= stack[-1][0]:
        #         stack.append((n, i))
        #     else:
        #         asc = False
        #         while stack and stack[-1][0] > n:
        #             stack.pop()
        # l = stack[-1][1] + 1 if stack else 0

        # stack = [(nums[N - 1], N - 1)]
        # desc = True
        # for i in range(N - 2, -1, -1):
        #     n = nums[i]
        #     if desc and n <= stack[-1][0]:
        #         stack.append((n, i))
        #     else:
        #         desc = False
        #         while stack and stack[-1][0] < n:
        #             stack.pop()
        # r = stack[-1][1] - 1 if stack else N - 1
        # return r - l + 1 if r >= l else 0

        maxn, right = float("-inf"), -1
        minn, left = float("inf"), -1

        for i in range(N):
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]

            if minn < nums[N - i - 1]:
                left = N - i - 1
            else:
                minn = nums[N - i - 1]

        return 0 if right == -1 else right - left + 1


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
    print(solution.findUnsortedSubarray([1, 2, 3, 4]))
    print(solution.findUnsortedSubarray([1]))
