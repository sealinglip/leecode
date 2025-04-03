#
# @lc app=leetcode.cn id=2874 lang=python3
#
# [2874] 有序三元组中的最大值 II
#
# 给你一个下标从 0 开始的整数数组 nums 。

# 请你从所有满足 i < j < k 的下标三元组 (i, j, k) 中，找出并返回下标三元组的最大值。如果所有满足条件的三元组的值都是负数，则返回 0 。

# 下标三元组 (i, j, k) 的值等于 (nums[i] - nums[j]) * nums[k] 。


# 示例 1：
# 输入：nums = [12,6,1,2,7]
# 输出：77
# 解释：下标三元组 (0, 2, 4) 的值是 (nums[0] - nums[2]) * nums[4] = 77 。
# 可以证明不存在值大于 77 的有序下标三元组。

# 示例 2：
# 输入：nums = [1,10,3,4,19]
# 输出：133
# 解释：下标三元组 (1, 2, 4) 的值是 (nums[1] - nums[2]) * nums[4] = 133 。
# 可以证明不存在值大于 133 的有序下标三元组。 

# 示例 3：
# 输入：nums = [1,2,3]
# 输出：0
# 解释：唯一的下标三元组 (0, 1, 2) 的值是一个负数，(nums[0] - nums[1]) * nums[2] = -3 。因此，答案是 0 。
 

# 提示：
# 3 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^6
# 复习

from typing import List
# @lc code=start
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # 改进 2873 实现
        res = 0
        n = len(nums)

        # 方法1：固定j，借助前后缀数组
        # preMax = [0] * n # preMax[i] = max(nums[:i+1])
        # postMax = [0] * n # postMax[i] = max(nums[i:])
        # preMax[0] = nums[0]
        # postMax[-1] = nums[-1]
        # for i in range(1, n):
        #     preMax[i] = max(preMax[i-1], nums[i])
        # for i in range(n-2, -1, -1):
        #     postMax[i] = max(postMax[i+1], nums[i])

        # for j in range(1, n-1):
        #     res = max(res, (preMax[j-1] - nums[j]) * postMax[j+1])

        # 方法2：固定k，遍历过程中更新区域极值
        maxI = maxD = 0 # maxI = max(nums[i]), maxD = max(nums[i] - nums[j])
        for k in range(n):
            res = max(res, maxD * nums[k])
            maxD = max(maxD, maxI - nums[k])
            maxI = max(maxI, nums[k])

        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumTripletValue([12,6,1,2,7])) # 77
    print(solution.maximumTripletValue([1,10,3,4,19])) # 133
    print(solution.maximumTripletValue([1,2,3])) # 0
