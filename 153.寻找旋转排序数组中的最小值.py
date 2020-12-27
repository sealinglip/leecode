#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] 。
# 请找出其中最小的元素。

# 示例 1：
# 输入：nums = [3,4,5,1,2]
# 输出：1

# 示例 2：
# 输入：nums = [4,5,6,7,0,1,2]
# 输出：0

# 示例 3：
# 输入：nums = [1]
# 输出：1

# 提示：
# 1 <= nums.length <= 5000
# -5000 <= nums[i] <= 5000
# nums 中的所有整数都是 唯一 的
# nums 原来是一个升序排序的数组，但在预先未知的某个点上进行了旋转

from typing import List
# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        
        N = len(nums)
        if N == 1:
            return nums[0]

        l, r = 0, N - 1
        while l < r:
            m = (l + r) >> 1
            if nums[l] < nums[m]: 
                if nums[m] < nums[r]:
                    break
                else:
                    # 说明前半段有序，最小值在右半段
                    l = m + 1
            elif nums[m] < nums[r]:
                # 说明后半段有序，最小值在左半段
                r = m
            else:
                # 这种情况只能是m和l重合了，直接将l置为m+1即可
                l = m + 1

        return nums[l]
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.findMin([2, 1]))
    print(solution.findMin([3,4,5,1,2]))
    print(solution.findMin([4,5,6,7,0,1,2]))
    print(solution.findMin([1]))