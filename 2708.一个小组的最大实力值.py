#
# @lc app=leetcode.cn id=2708 lang=python3
#
# [2708] 一个小组的最大实力值
#
# 给你一个下标从 0 开始的整数数组 nums ，它表示一个班级中所有学生在一次考试中的成绩。老师想选出一部分同学组成一个 非空 小组，且这个小组的 实力值 最大，如果这个小组里的学生下标为 i0, i1, i2, ... , ik ，那么这个小组的实力值定义为 nums[i0] * nums[i1] * nums[i2] * ... * nums[ik​] 。

# 请你返回老师创建的小组能得到的最大实力值为多少。

# 示例 1：
# 输入：nums = [3,-1,-5,2,5,-9]
# 输出：1350
# 解释：一种构成最大实力值小组的方案是选择下标为 [0,2,3,4,5] 的学生。实力值为 3 * (-5) * 2 * 5 * (-9) = 1350 ，这是可以得到的最大实力值。

# 示例 2：
# 输入：nums = [-4,-5,-4]
# 输出：20
# 解释：选择下标为 [0, 1] 的学生。得到的实力值为 20 。我们没法得到更大的实力值。
 

# 提示：
# 1 <= nums.length <= 13
# -9 <= nums[i] <= 9

from typing import List
# @lc code=start
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # 负值要不要，这是个问题，可以做一下处理，先排序，负值可以成对用
        nums.sort()
        n = len(nums)
        res = 1
        empty = True
        for i in range(1, n, 2):
            if nums[i] < 0:
                res *= (nums[i-1] * nums[i])
                empty = False

        # 把所有大于0的再乘一下
        for i in range(n-1, -1, -1):
            if nums[i] <= 0:
                break
            res *= nums[i]
            empty = False
        
        return nums[n-1] if empty else res
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxStrength([0,-1])) # 0
    print(solution.maxStrength([3,-1,-5,2,5,-9])) # 1350
    print(solution.maxStrength([-4,-5,-4])) # 20
