#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#
# 给你一个整数数组 nums，将 nums 中的的所有偶数元素移动到数组的前面，后跟所有奇数元素。

# 返回满足此条件的 任一数组 作为答案。


# 示例 1：
# 输入：nums = [3, 1, 2, 4]
# 输出：[2, 4, 3, 1]
# 解释：[4, 2, 3, 1]、[2, 4, 1, 3] 和[4, 2, 1, 3] 也会被视作正确答案。

# 示例 2：
# 输入：nums = [0]
# 输出：[0]


# 提示：
# 1 <= nums.length <= 5000
# 0 <= nums[i] <= 5000


from typing import List
# @lc code=start


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        L = len(nums)
        l, r = 0, L-1  # 指针指向奇数、偶数
        while l < r:
            while l < L and (nums[l] & 1 == 0):  # l定位到奇数
                l += 1
            while r >= 0 and (nums[r] & 1 == 1):  # r定位到偶数
                r -= 1

            if l < r:
                nums[l], nums[r] = nums[r], nums[l]

        return nums


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.sortArrayByParity([3, 1, 2, 4]))  # [4, 2, 1, 3]
    print(solution.sortArrayByParity([0]))  # [0]
