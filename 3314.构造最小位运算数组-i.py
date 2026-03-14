#
# @lc app=leetcode.cn id=3314 lang=python3
#
# [3314] 构造最小位运算数组 I
#
# https://leetcode.cn/problems/construct-the-minimum-bitwise-array-i/description/
#
# algorithms
# Easy (82.88%)
# Likes:    5
# Dislikes: 0
# Total Accepted:    5.2K
# Total Submissions: 6.1K
# Testcase Example:  '[2,3,5,7]'
#
# 给你一个长度为 n 的质数数组 nums 。你的任务是返回一个长度为 n 的数组 ans ，对于每个下标 i ，以下 条件 均成立：
# ans[i] OR (ans[i] + 1) == nums[i]
# 
# 除此以外，你需要 最小化 结果数组里每一个 ans[i] 。
# 如果没法找到符合 条件 的 ans[i] ，那么 ans[i] = -1 。
# 质数 指的是一个大于 1 的自然数，且它只有 1 和自己两个因数。
# 
# 
# 示例 1：
# 输入：nums = [2,3,5,7]
# 输出：[-1,1,4,3]
# 解释：
# 对于 i = 0 ，不存在 ans[0] 满足 ans[0] OR (ans[0] + 1) = 2 ，所以 ans[0] = -1 。
# 对于 i = 1 ，满足 ans[1] OR (ans[1] + 1) = 3 的最小 ans[1] 为 1 ，因为 1 OR (1 + 1) = 3。
# 对于 i = 2 ，满足 ans[2] OR (ans[2] + 1) = 5 的最小 ans[2] 为 4 ，因为 4 OR (4 + 1) = 5。
# 对于 i = 3 ，满足 ans[3] OR (ans[3] + 1) = 7 的最小 ans[3] 为 3 ，因为 3 OR (3 + 1) = 7。
# 
# 示例 2：
# 输入：nums = [11,13,31]
# 输出：[9,12,15]
# 解释：
# 对于 i = 0 ，满足 ans[0] OR (ans[0] + 1) = 11 的最小 ans[0] 为 9 ，因为 9 OR (9 + 1) = 11。
# 对于 i = 1 ，满足 ans[1] OR (ans[1] + 1) = 13 的最小 ans[1] 为 12 ，因为 12 OR (12 + 1) = 13 。
# 对于 i = 2 ，满足 ans[2] OR (ans[2] + 1) = 31 的最小 ans[2] 为 15 ，因为 15 OR (15 + 1) = 31 。
# 
# 
# 提示：
# 1 <= nums.length <= 100
# 2 <= nums[i] <= 1000
# nums[i] 是一个质数。
# 
# 
#

from typing import List
# @lc code=start
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def calc(x: int) -> int:
            if x & 1 == 0:
                return -1
            c = list(bin(x)[2:])
            idx = 0
            for i in range(len(c)-1, -1, -1):
                if c[i] == '0':
                    idx = i + 1
                    break
            c[idx] = '0'
            return int("".join(c), 2)

        return [calc(x) for x in nums]
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minBitwiseArray([2,3,5,7])) # [-1,1,4,3]
    print(solution.minBitwiseArray([11,13,31])) # [9,12,15]

