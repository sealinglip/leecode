#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#
# 集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复。
# 给定一个数组 nums 代表了集合 S 发生错误后的结果。
# 请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。


# 示例 1：
# 输入：nums = [1, 2, 2, 4]
# 输出：[2, 3]

# 示例 2：
# 输入：nums = [1, 1]
# 输出：[1, 2]


# 提示：
# 2 <= nums.length <= 10^4
# 1 <= nums[i] <= 10^4

from typing import List
# @lc code=start


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup, sum = -1, 0
        n = len(nums)
        for i in range(n):
            idx = abs(nums[i]) - 1
            sum += idx + 1
            if nums[idx] < 0:
                dup = idx + 1
            nums[idx] = -nums[idx]
        missing = ((1 + n) * n >> 1) - sum + dup
        return [dup, missing]

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findErrorNums([1, 5, 3, 2, 2, 7, 6, 4, 8, 9]))
    print(solution.findErrorNums([1, 2, 2, 4]))
    print(solution.findErrorNums([1, 2, 4, 4]))
    print(solution.findErrorNums([1, 1]))
