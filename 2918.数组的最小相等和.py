#
# @lc app=leetcode.cn id=2918 lang=python3
#
# [2918] 数组的最小相等和
#
# https://leetcode.cn/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/description/
#
# algorithms
# Medium (37.19%)
# Likes:    31
# Dislikes: 0
# Total Accepted:    13.3K
# Total Submissions: 29.2K
# Testcase Example:  '[3,2,0,1,0]\n[6,5,0]'
#
# 给你两个由正整数和 0 组成的数组 nums1 和 nums2 。
# 你必须将两个数组中的 所有 0 替换为 严格 正整数，并且满足两个数组中所有元素的和 相等 。
# 返回 最小 相等和 ，如果无法使两数组相等，则返回 -1 。
# 
# 
# 示例 1：
# 输入：nums1 = [3,2,0,1,0], nums2 = [6,5,0]
# 输出：12
# 解释：可以按下述方式替换数组中的 0 ：
# - 用 2 和 4 替换 nums1 中的两个 0 。得到 nums1 = [3,2,2,1,4] 。
# - 用 1 替换 nums2 中的一个 0 。得到 nums2 = [6,5,1] 。
# 两个数组的元素和相等，都等于 12 。可以证明这是可以获得的最小相等和。
# 
# 
# 示例 2：
# 输入：nums1 = [2,0,2,0], nums2 = [1,4]
# 输出：-1
# 解释：无法使两个数组的和相等。
# 
# 
# 提示：
# 1 <= nums1.length, nums2.length <= 10^5
# 0 <= nums1[i], nums2[i] <= 10^6
# 
#

from typing import List

# @lc code=start
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        zc1, zc2 = nums1.count(0), nums2.count(0)

        if (zc1 == 0 and sum1 < sum2 + zc2) or (zc2 == 0 and zc1 + sum1 > sum2):
            return -1
        return max(sum2 + zc2, sum1 + zc1)

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minSum([8,13,15,18,0,18,0,0,5,20,12,27,3,14,22,0], [29,1,6,0,10,24,27,17,14,13,2,19,2,11])) # 179
    print(solution.minSum([3,2,0,1,0], [6,5,0])) # 12
    print(solution.minSum([2,0,2,0], [1,4])) # -1
