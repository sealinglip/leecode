#
# @lc app=leetcode.cn id=659 lang=python3
#
# [659] 分割数组为连续子序列
#
# 给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个子序列，
# 其中每个子序列都由连续整数组成且长度至少为 3 。

# 如果可以完成上述分割，则返回 true ；否则，返回 false 。

# 示例 1：
# 输入: [1,2,3,3,4,5]
# 输出: True
# 解释:
# 你可以分割出这样两个连续子序列 : 
# 1, 2, 3
# 3, 4, 5
 
# 示例 2：
# 输入: [1,2,3,3,4,4,5,5]
# 输出: True
# 解释:
# 你可以分割出这样两个连续子序列 : 
# 1, 2, 3, 4, 5
# 3, 4, 5
 
# 示例 3：
# 输入: [1,2,3,4,4,5]
# 输出: False
 
# 提示：

# 输入的数组长度范围为 [1, 10000]

from typing import List
# @lc code=start
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if not nums:
            return False

        profile = []
        curVal = nums[0] - 1
        idx = 0
        for num in nums:
            if num != curVal:
                if profile:
                    end = idx - 1 if num == curVal + 1 else -1
                    for i in range(len(profile) - 1, end, -1):
                        if profile[i] < 3:
                            return False
                        profile.pop()
                curVal = num
                idx = 0
            if idx < len(profile):
                profile[idx] += 1
            else:
                profile.insert(0, 1)
            idx += 1

        return all(x > 2 for x in profile)
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPossible([1,2,3,3,4,5]))
    print(solution.isPossible([1,2,3,3,4,4,5,5]))
    print(solution.isPossible([1,2,3,4,4,5]))