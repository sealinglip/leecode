#
# @lc app=leetcode.cn id=1031 lang=python3
#
# [1031] 两个非重叠子数组的最大和
#
# 给你一个整数数组 nums 和两个整数 firstLen 和 secondLen，请你找出并返回两个非重叠 子数组 中元素的最大和，长度分别为 firstLen 和 secondLen 。

# 长度为 firstLen 的子数组可以出现在长为 secondLen 的子数组之前或之后，但二者必须是不重叠的。

# 子数组是数组的一个 连续 部分。


# 示例 1：
# 输入：nums = [0, 6, 5, 2, 2, 5, 1, 9, 4], firstLen = 1, secondLen = 2
# 输出：20
# 解释：子数组的一种选择中，[9] 长度为 1，[6, 5] 长度为 2。

# 示例 2：
# 输入：nums = [3, 8, 1, 3, 2, 1, 8, 9, 0], firstLen = 3, secondLen = 2
# 输出：29
# 解释：子数组的一种选择中，[3, 8, 1] 长度为 3，[8, 9] 长度为 2。

# 示例 3：
# 输入：nums = [2, 1, 5, 6, 0, 9, 5, 0, 3, 8], firstLen = 4, secondLen = 3
# 输出：31
# 解释：子数组的一种选择中，[5, 6, 0, 9] 长度为 4，[0, 3, 8] 长度为 3。


# 提示：
# 1 <= firstLen, secondLen <= 1000
# 2 <= firstLen + secondLen <= 1000
# firstLen + secondLen <= nums.length <= 1000
# 0 <= nums[i] <= 1000

from itertools import accumulate
from typing import List
# @lc code=start


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        accum = [0] + list(accumulate(nums))

        # 动规
        def maxSumTwo(len1: int, len2: int) -> int:
            # 移动右边的窗口，求右窗口和和右窗口左边区域中左窗口最大值的和，记录过程中的这个和的最大值。
            maxSumL = accum[len1]
            res = accum[len1+len2]
            for i in range(len1+len2, len(nums)):
                maxSumL = max(maxSumL, accum[i+1-len2] - accum[i+1-len1-len2])
                res = max(res, maxSumL + accum[i+1] - accum[i+1-len2])

            return res

        return max(maxSumTwo(firstLen, secondLen), maxSumTwo(secondLen, firstLen))


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSumTwoNoOverlap([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2))  # 20
    print(solution.maxSumTwoNoOverlap(
        [3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2))  # 29
    print(solution.maxSumTwoNoOverlap(
        [2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3))  # 31
