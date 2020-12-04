#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#
# 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
# 你需要返回给定数组中的重要翻转对的数量。

# 示例 1:
# 输入: [1,3,2,3,1]
# 输出: 2

# 示例 2:
# 输入: [2,4,3,5,1]
# 输出: 3

# 注意:
# 给定数组的长度不会超过50000。
# 输入数组中的所有数字都在32位整数的表示范围内。

from typing import List
# @lc code=start
class Solution:
    def findReversePairs(self, nums, left, right):
        res = 0
        mid = (left + right) >> 1

        # [i, mid]和[mid+1, right]两个区间分别都是升序
        j = mid + 1
        for i in range(left, mid + 1):
            while j <= right and nums[i] > 2 * nums[j]:
                res += mid - i + 1 # j和[i, mid] 之间的数都可以组成重要翻转对
                j += 1
        return res

    def mergeSort(self, nums, sorted, l, r):
        if l >= r:
            return 0

        mid = (l + r) >> 1
        res = self.mergeSort(nums, sorted, l, mid) + \
                self.mergeSort(nums, sorted, mid + 1, r) + \
                self.findReversePairs(nums, l, r)

        # 将[l, r]之间的元素归并排序
        i, j, k = l, mid + 1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                sorted[k] = nums[i]
                i += 1
            else:
                sorted[k] = nums[j]
                j += 1
            k += 1
        
        while i <= mid:
            sorted[k] = nums[i]
            i += 1
            k += 1
        while j <= r:
            sorted[k] = nums[j]
            j += 1
            k += 1

        for k in range(l, r + 1):
            nums[k] = sorted[k]

        return res

    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted = [0 for n in nums]
        return self.mergeSort(nums, sorted, 0, len(nums) - 1)
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.reversePairs([1,2,3,4,5]))
    print(solution.reversePairs([1,3,2,3,1]))
    print(solution.reversePairs([2,4,3,5,1]))