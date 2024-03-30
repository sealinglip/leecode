#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 求众数 II
#
# 给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。


# 示例 1：
# 输入：[3, 2, 3]
# 输出：[3]

# 示例 2：
# 输入：nums = [1]
# 输出：[1]

# 示例 3：
# 输入：[1, 1, 1, 3, 3, 2, 2, 2]
# 输出：[1, 2]


# 提示：
# 1 <= nums.length <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9


# 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。

from typing import List
# @lc code=start


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele1, ele2 = 0, 0
        cnt1, cnt2 = 0, 0
        N = len(nums)

        for num in nums:
            if cnt1 > 0 and num == ele1:
                cnt1 += 1
            elif cnt2 > 0 and num == ele2:
                cnt2 += 1
            elif cnt1 == 0:
                cnt1 += 1
                ele1 = num
            elif cnt2 == 0:
                cnt2 += 1
                ele2 = num
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1, cnt2 = 0, 0
        res = []
        for num in nums:
            if num == ele1:
                cnt1 += 1
            elif num == ele2:
                cnt2 += 1

        if cnt1 > (N // 3):
            res.append(ele1)
        if cnt2 > (N // 3):
            res.append(ele2)
        return res


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.majorityElement([3, 2, 3]))
    print(solution.majorityElement([1]))
    print(solution.majorityElement([1, 1, 1, 3, 3, 2, 2, 2]))
