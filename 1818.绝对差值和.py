#
# @lc app=leetcode.cn id=1818 lang=python3
#
# [1818] 绝对差值和
#
# 给你两个正整数数组 nums1 和 nums2 ，数组的长度都是 n 。
# 数组 nums1 和 nums2 的 绝对差值和 定义为所有 | nums1[i] - nums2[i] |（0 <= i < n）的 总和（下标从 0 开始）。
# 你可以选用 nums1 中的 任意一个 元素来替换 nums1 中的 至多 一个元素，以 最小化 绝对差值和。
# 在替换数组 nums1 中最多一个元素 之后 ，返回最小绝对差值和。因为答案可能很大，所以需要对 10^9 + 7 取余 后返回。

# |x | 定义为：
# 如果 x >= 0 ，值为 x ，或者
# 如果 x <= 0 ，值为 - x


# 示例 1：
# 输入：nums1 = [1, 7, 5], nums2 = [2, 3, 5]
# 输出：3
# 解释：有两种可能的最优方案：
# - 将第二个元素替换为第一个元素：[1, 7, 5] = > [1, 1, 5] ，或者
# - 将第二个元素替换为第三个元素：[1, 7, 5] = > [1, 5, 5]
# 两种方案的绝对差值和都是 | 1-2 | + (| 1-3 | 或者 | 5-3|) + |5-5 | = 3

# 示例 2：
# 输入：nums1 = [2, 4, 6, 8, 10], nums2 = [2, 4, 6, 8, 10]
# 输出：0
# 解释：nums1 和 nums2 相等，所以不用替换元素。绝对差值和为 0

# 示例 3：
# 输入：nums1 = [1, 10, 4, 4, 2, 7], nums2 = [9, 3, 5, 1, 7, 4]
# 输出：20
# 解释：将第一个元素替换为第二个元素：[1, 10, 4, 4, 2, 7] = > [10, 10, 4, 4, 2, 7]
# 绝对差值和为 | 10-9 | + | 10-3 | + | 4-5 | + | 4-1 | + | 2-7 | + | 7-4 | = 20


# 提示：
# n == nums1.length
# n == nums2.length
# 1 <= n <= 10^5
# 1 <= nums1[i], nums2[i] <= 10^5

from typing import List
# @lc code=start

from bisect import bisect_right


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10 ** 9 + 7
        N = len(nums1)

        a = nums1[:]
        a.sort()

        absSum = 0
        maxDelta = 0
        for n1, n2 in zip(nums1, nums2):
            curAbs = abs(n1 - n2)
            absSum += curAbs
            i = bisect_right(a, n2)
            if i:
                maxDelta = max(maxDelta, curAbs - (n2 - a[i-1]))
            if i != N:
                maxDelta = max(maxDelta, curAbs - (a[i] - n2))

        return (absSum if maxDelta <= 0 else absSum - maxDelta) % MOD

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.minAbsoluteSumDiff([1, 28, 21], [9, 21, 20]))
    print(solution.minAbsoluteSumDiff([1, 7, 5], [2, 3, 5]))
    print(solution.minAbsoluteSumDiff(
        [2, 4, 6, 8, 10], [2, 4, 6, 8, 10]))
    print(solution.minAbsoluteSumDiff(
        [1, 10, 4, 4, 2, 7], [9, 3, 5, 1, 7, 4]))
