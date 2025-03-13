#
# @lc app=leetcode.cn id=2012 lang=python3
#
# [2012] 数组美丽值求和
#
# 给你一个下标从 0 开始的整数数组 nums 。对于每个下标 i（1 <= i <= nums.length - 2），nums[i] 的 美丽值 等于：
# 2，对于所有 0 <= j < i 且 i < k <= nums.length - 1 ，满足 nums[j] < nums[i] < nums[k]
# 1，如果满足 nums[i - 1] < nums[i] < nums[i + 1] ，且不满足前面的条件
# 0，如果上述条件全部不满足
# 返回符合 1 <= i <= nums.length - 2 的所有 nums[i] 的 美丽值的总和 。


# 示例 1：
# 输入：nums = [1,2,3]
# 输出：2
# 解释：对于每个符合范围 1 <= i <= 1 的下标 i :
# - nums[1] 的美丽值等于 2

# 示例 2：
# 输入：nums = [2,4,6,4]
# 输出：1
# 解释：对于每个符合范围 1 <= i <= 2 的下标 i :
# - nums[1] 的美丽值等于 1
# - nums[2] 的美丽值等于 0
# 示例 3：

# 输入：nums = [3,2,1]
# 输出：0
# 解释：对于每个符合范围 1 <= i <= 1 的下标 i :
# - nums[1] 的美丽值等于 0
 

# 提示：
# 3 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5

from typing import List
# @lc code=start
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        # 先从头到尾，在从尾到头遍历
        flag = [0] * n
        ma = prev = nums[0]
        for i in range(1, n-1):
            num = nums[i]
            if num > ma:
                flag[i] = 2
                ma = num
            elif num > prev:
                flag[i] = 1
            prev = num

        mi = prev = nums[-1]
        for i in range(n-2, 0, -1):
            num = nums[i]
            if num < mi:
                mi = num
            elif num < prev:
                if flag[i] == 2:
                    flag[i] = 1
            else:
                flag[i] = 0
            prev = num

        return sum(flag)

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.sumOfBeauties([1,2,3])) # 2
    print(solution.sumOfBeauties([2,4,6,4])) # 1
    print(solution.sumOfBeauties([3,2,1])) # 0
