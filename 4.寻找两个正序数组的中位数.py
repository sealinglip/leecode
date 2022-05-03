#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
# 请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 你可以假设 nums1 和 nums2 不会同时为空。

# 示例 1:
# nums1 = [1, 3]
# nums2 = [2]
# 则中位数是 2.0

# 示例 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# 则中位数是(2 + 3)/2 = 2.5

# Hard
from typing import List
# @lc code=start


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalLen = len(nums1) + len(nums2)
        if not totalLen:
            return 0

        half, odd, idx1, idx2, idx, curVal, readVal = (
            totalLen >> 1), totalLen & 1, 0, 0, 0, None, None  # 中位索引、总数是否单、数组1索引、数组2索引、总索引、当前值，读入值

        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] < nums2[idx2]:
                readVal = nums1[idx1]
                idx1 += 1
            elif nums1[idx1] == nums2[idx2]:
                readVal = nums1[idx1]
                idx1 += 1
                idx2 += 1
                idx += 1
                if idx > half:
                    if odd:
                        return readVal
                    else:
                        return (curVal + readVal) / 2
                curVal = readVal
            else:
                readVal = nums2[idx2]
                idx2 += 1

            idx += 1
            if idx > half:
                if odd:
                    return readVal
                else:
                    return (curVal + readVal) / 2
            curVal = readVal

        nums = nums1 if idx1 < len(nums1) else nums2  # nums指向还有剩余元素的数组
        idx3 = half - idx + (idx1 if idx1 < len(nums1) else idx2)

        readVal = nums[idx3]
        if half > idx:
            curVal = nums[idx3 - 1]

        if odd:
            return readVal
        else:
            return (curVal + readVal) / 2

        return curVal

# @lc code=end


if __name__ == '__main__':
    solution = Solution()
    # print(solution.findMedianSortedArrays([1, 3], [2]))
    # print(solution.findMedianSortedArrays([], [2]))
    # print(solution.findMedianSortedArrays([1, 2], [-1, 3]))
    print(solution.findMedianSortedArrays([1, 2, 3], [4, 5, 6]))
    print(solution.findMedianSortedArrays([1, 2, 3], [4, 5, 6, 7, 8, 9]))
