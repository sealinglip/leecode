#
# @lc app=leetcode.cn id=915 lang=python3
#
# [915] 分割数组
#
# 给定一个数组 nums ，将其划分为两个连续子数组 left 和 right， 使得：

# left 中的每个元素都小于或等于 right 中的每个元素。
# left 和 right 都是非空的。
# left 的长度要尽可能小。
# 在完成这样的分组后返回 left 的 长度 。

# 用例可以保证存在这样的划分方法。


# 示例 1：
# 输入：nums = [5,0,3,8,6]
# 输出：3
# 解释：left = [5,0,3]，right = [8,6]

# 示例 2：
# 输入：nums = [1,1,1,0,6,12]
# 输出：4
# 解释：left = [1,1,1,0]，right = [6,12]


# 提示：
# 2 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^6
# 可以保证至少有一种方法能够按题目所描述的那样对 nums 进行划分。

# 复习

from typing import List
# @lc code=start


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        curMax = leftMax = nums[0]
        splitPos = 0
        for i in range(1, n - 1):
            curMax = max(curMax, nums[i])
            if nums[i] < leftMax:
                leftMax, splitPos = curMax, i
        return splitPos + 1


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.partitionDisjoint([1, 2, 3, 4, 5]))  # 1
    print(solution.partitionDisjoint([5, 0, 3, 8, 6]))  # 3
    print(solution.partitionDisjoint([1, 1, 1, 0, 6, 12]))  # 4
