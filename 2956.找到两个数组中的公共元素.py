#
# @lc app=leetcode.cn id=2956 lang=python3
#
# [2956] 找到两个数组中的公共元素
#
# 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，它们分别含有 n 和 m 个元素。请你计算以下两个数值：

# answer1：使得 nums1[i] 在 nums2 中出现的下标 i 的数量。
# answer2：使得 nums2[i] 在 nums1 中出现的下标 i 的数量。
# 返回 [answer1, answer2]。


# 示例 1：
# 输入：nums1 = [2,3,2], nums2 = [1,2]
# 输出：[2,1]

# 示例 2：
# 输入：nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6]
# 输出：[3,4]
# 解释：
# nums1 中下标在 1，2，3 的元素在 nums2 中也存在。所以 answer1 为 3。
# nums2 中下标在 0，1，3，4 的元素在 nums1 中也存在。所以 answer2 为 4。

# 示例 3：
# 输入：nums1 = [3,4,2,3], nums2 = [1,5]
# 输出：[0,0]
# 解释：
# nums1 和 nums2 中没有相同的数字，所以答案是 [0,0]。

# 提示：
# n == nums1.length
# m == nums2.length
# 1 <= n, m <= 100
# 1 <= nums1[i], nums2[i] <= 100

from typing import List
# @lc code=start
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [sum(n in set2 for n in nums1), sum(n in set1 for n in nums2)]
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.findIntersectionValues([2,3,2], [1,2])) # [2,1]
    print(solution.findIntersectionValues([4,3,2,3,1], [2,2,5,2,3,6])) # [3,4]
    print(solution.findIntersectionValues([3,4,2,3], [1,5])) # [0,0]
