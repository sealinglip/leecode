#
# @lc app=leetcode.cn id=2040 lang=python3
#
# [2040] 两个有序数组的第 K 小乘积
#
# https://leetcode.cn/problems/kth-smallest-product-of-two-sorted-arrays/description/
#
# algorithms
# Hard (35.28%)
# Likes:    56
# Dislikes: 0
# Total Accepted:    3.8K
# Total Submissions: 9.7K
# Testcase Example:  '[2,5]\n[3,4]\n2'
#
# 给你两个 从小到大排好序 且下标从 0 开始的整数数组 nums1 和 nums2 以及一个整数 k ，请你返回第 k （从 1 开始编号）小的
# nums1[i] * nums2[j] 的乘积，其中 0 <= i < nums1.length 且 0 <= j < nums2.length 。
# 
# 
# 示例 1：
# 输入：nums1 = [2,5], nums2 = [3,4], k = 2
# 输出：8
# 解释：第 2 小的乘积计算如下：
# - nums1[0] * nums2[0] = 2 * 3 = 6
# - nums1[0] * nums2[1] = 2 * 4 = 8
# 第 2 小的乘积为 8 。
# 
# 示例 2：
# 输入：nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6
# 输出：0
# 解释：第 6 小的乘积计算如下：
# - nums1[0] * nums2[1] = (-4) * 4 = -16
# - nums1[0] * nums2[0] = (-4) * 2 = -8
# - nums1[1] * nums2[1] = (-2) * 4 = -8
# - nums1[1] * nums2[0] = (-2) * 2 = -4
# - nums1[2] * nums2[0] = 0 * 2 = 0
# - nums1[2] * nums2[1] = 0 * 4 = 0
# 第 6 小的乘积为 0 。
# 
# 示例 3：
# 输入：nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3
# 输出：-6
# 解释：第 3 小的乘积计算如下：
# - nums1[0] * nums2[4] = (-2) * 5 = -10
# - nums1[0] * nums2[3] = (-2) * 4 = -8
# - nums1[4] * nums2[0] = 2 * (-3) = -6
# 第 3 小的乘积为 -6 。
# 
# 
# 提示：
# 1 <= nums1.length, nums2.length <= 5 * 10^4
# -10^5 <= nums1[i], nums2[j] <= 10^5
# 1 <= k <= nums1.length * nums2.length
# nums1 和 nums2 都是从小到大排好序的。
# 
#

from typing import List
# @lc code=start
from bisect import bisect
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n1, n2 = len(nums1), len(nums2)
        pivot1 = bisect(nums1, 0)
        pivot2 = bisect(nums2, 0)
        l, r = int(-1e10), int(1e10) # 乘积的取值空间
        # 二分查找
        while l < r:
            mid = (l + r) >> 1
            count = 0 # 统计比mid小的乘积有多少
            # 先看两数组的非正数相乘 和 两数组的正数相乘
            if mid >= 0:
                # 如果mid小于0，这部分怎么相乘都不会比mid小
                i1, i2 = 0, pivot2 - 1
                while i1 < pivot1 and i2 >= 0:
                    if nums1[i1] * nums2[i2] > mid:
                        i1 += 1
                    else:
                        count += pivot1 - i1 # 对于选定的nums2[i2]，nums1中非正数有这么多个位置可以使乘积小于等于mid
                        i2 -= 1

                i1, i2 = pivot1, n2 - 1
                while i1 < n1 and i2 >= pivot2:
                    if nums1[i1] * nums2[i2] > mid:
                        i2 -= 1
                    else:
                        count += i2 - pivot2 + 1 # 对于选定的nums1[i1]，nums2中正数有这么多个位置可以使乘积小于等于mid
                        i1 += 1

            # 再看nums1的非正 和 nums2的正数相乘，以及nums1的正 和 nums2的非正相乘
            if mid > 0:
                count += pivot1 * (n2 - pivot2) + (n1 - pivot1) * pivot2
            else:
                i1, i2 = 0, pivot2
                while i1 < pivot1 and i2 < n2:
                    if nums1[i1] * nums2[i2] > mid:
                        i2 += 1
                    else:
                        count += n2 - i2 # 对于选定的nums1[i1]，nums2中的正数有这么多个位置可以使乘积小于等于mid
                        i1 += 1
                i1, i2 = pivot1, 0
                while i1 < n1 and i2 < pivot2:
                    if nums1[i1] * nums2[i2] > mid:
                        i1 += 1
                    else:
                        count += n1 - i1 # 对于选定的nums2[i2]，nums1中的正数有这么多个位置可以使乘积小于等于mid
                        i2 += 1

            if count < k:
                l = mid + 1
            else:
                r = mid
        
        return l

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.kthSmallestProduct([2,5], [3,4], 2)) # 8
    print(solution.kthSmallestProduct([-4,-2,0,3], [2,4], 6)) # 0
    print(solution.kthSmallestProduct([-2,-1,0,1,2], [-3,-1,2,4,5], 3)) # -6
