#
# @lc app=leetcode.cn id=2364 lang=python3
#
# [2364] 统计坏数对的数目
#
# https://leetcode.cn/problems/count-number-of-bad-pairs/description/
#
# algorithms
# Medium (44.01%)
# Likes:    76
# Dislikes: 0
# Total Accepted:    21.7K
# Total Submissions: 39.9K
# Testcase Example:  '[4,1,3,3]'
#
# 给你一个下标从 0 开始的整数数组 nums 。如果 i < j 且 j - i != nums[j] - nums[i] ，那么我们称 (i, j)
# 是一个 坏数对 。
# 
# 请你返回 nums 中 坏数对 的总数目。
# 
# 
# 
# 示例 1：
# 输入：nums = [4,1,3,3]
# 输出：5
# 解释：数对 (0, 1) 是坏数对，因为 1 - 0 != 1 - 4 。
# 数对 (0, 2) 是坏数对，因为 2 - 0 != 3 - 4, 2 != -1 。
# 数对 (0, 3) 是坏数对，因为 3 - 0 != 3 - 4, 3 != -1 。
# 数对 (1, 2) 是坏数对，因为 2 - 1 != 3 - 1, 1 != 2 。
# 数对 (2, 3) 是坏数对，因为 3 - 2 != 3 - 3, 1 != 0 。
# 总共有 5 个坏数对，所以我们返回 5 。
# 
# 
# 示例 2：
# 输入：nums = [1,2,3,4,5]
# 输出：0
# 解释：没有坏数对。
# 
# 
# 
# 
# 提示：
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 
# 

from collections import Counter
from typing import List
# from itertools import combinations

# @lc code=start
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        diffCnt = Counter(x - i for i, x in enumerate(nums))
        # 下面的解法会TLE
        # 求nums[i]和i的差值
        # return sum(i * j for i, j in combinations(diffCnt.values(), 2))
        n = len(nums)
        # 改成总的对数减好的对数
        return ((n * (n+1)) >> 1) - sum(c * (c+1) >> 1 for c in diffCnt.values())
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countBadPairs([4,1,3,3])) # 5
    print(solution.countBadPairs([1,2,3,4,5])) # 0
