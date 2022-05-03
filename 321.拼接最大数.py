#
# @lc app=leetcode.cn id=321 lang=python3
#
# [321] 拼接最大数
#
# 给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。
# 现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中
# 取出的数字保持其在原数组中的相对顺序。

# 求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。
# 说明: 请尽可能地优化你算法的时间和空间复杂度。

# 示例 1:
# 输入:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# 输出:
# [9, 8, 6, 5, 3]

# 示例 2:
# 输入:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# 输出:
# [6, 7, 6, 0, 4]

# 示例 3:
# 输入:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# 输出:
# [9, 8, 9]

# Hard

from typing import List
# @lc code=start


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pickMax(nums: List[int], n: int) -> List[int]:
            if n == 0:
                return []
            stack = []
            drop = len(nums) - n  # 需要移除的元素个数
            for digit in nums:
                while drop and stack and stack[-1] < digit:
                    stack.pop()
                    drop -= 1
                stack.append(digit)
            return stack[:n]  # 截前n位

        def merge(A: List[int], B: List[int]):
            res = []
            while A or B:
                pop = A if A > B else B
                res.append(pop.pop(0))
            return res

        L1, L2 = len(nums1), len(nums2)
        return max(merge(pickMax(nums1, i), pickMax(nums2, k - i)) for i in range(k + 1) if i <= L1 and (k - i) <= L2)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5))
    print(solution.maxNumber([6, 7], [6, 0, 4], 5))
    print(solution.maxNumber([3, 9], [8, 9], 3))
