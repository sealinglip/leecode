#
# @lc app=leetcode.cn id=870 lang=python3
#
# [870] 优势洗牌
#
# 给定两个大小相等的数组 nums1 和 nums2，nums1 相对于 nums 的优势可以用满足 nums1[i] > nums2[i] 的索引 i 的数目来描述。

# 返回 nums1 的任意排列，使其相对于 nums2 的优势最大化。


# 示例 1：
# 输入：nums1 = [2, 7, 11, 15], nums2 = [1, 10, 4, 11]
# 输出：[2, 11, 7, 15]

# 示例 2：
# 输入：nums1 = [12, 24, 8, 32], nums2 = [13, 25, 32, 11]
# 输出：[24, 32, 8, 12]


# 提示：
# 1 <= nums1.length <= 10^5
# nums2.length == nums1.length
# 0 <= nums1[i], nums2[i] <= 10^9

from typing import List
# @lc code=start
import heapq


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 田忌赛马
        # 最简单的方式，两个数组都排序，
        numAndPos = [(n, i) for i, n in enumerate(nums2)]
        numAndPos.sort()
        res = [None] * len(nums1)

        heapq.heapify(nums1)
        discard = []
        for n, i in numAndPos:
            if nums1:
                while nums1 and (p := heapq.heappop(nums1)) <= n:
                    discard.append(p)
                if p > n:
                    res[i] = p
                    continue
            res[i] = discard.pop()

        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.advantageCount(
        [0], [0]))  # [0]
    print(solution.advantageCount(
        [2, 7, 11, 15], [1, 10, 4, 11]))  # [2,11,7,15]
    print(solution.advantageCount(
        [12, 24, 8, 32], [13, 25, 32, 11]))  # [24,32,8,12]
