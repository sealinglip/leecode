#
# @lc app=leetcode.cn id=2616 lang=python3
#
# [2616] 最小化数对的最大差值
#
# https://leetcode.cn/problems/minimize-the-maximum-difference-of-pairs/description/
#
# algorithms
# Medium (43.89%)
# Likes:    54
# Dislikes: 0
# Total Accepted:    7.9K
# Total Submissions: 16.8K
# Testcase Example:  '[10,1,2,7,1,3]\n2'
#
# 给你一个下标从 0 开始的整数数组 nums 和一个整数 p 。请你从 nums 中找到 p 个下标对，每个下标对对应数值取差值，你需要使得这 p
# 个差值的 最大值 最小。同时，你需要确保每个下标在这 p 个下标对中最多出现一次。
# 
# 对于一个下标对 i 和 j ，这一对的差值为 |nums[i] - nums[j]| ，其中 |x| 表示 x 的 绝对值 。
# 请你返回 p 个下标对对应数值 最大差值 的 最小值 。
# 
# 
# 示例 1：
# 输入：nums = [10,1,2,7,1,3], p = 2
# 输出：1
# 解释：第一个下标对选择 1 和 4 ，第二个下标对选择 2 和 5 。
# 最大差值为 max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1 。所以我们返回 1。
# 
# 示例 2：
# 输入：nums = [4,2,1,2], p = 1
# 输出：0
# 解释：选择下标 1 和 3 构成下标对。差值为 |2 - 2| = 0 ，这是最大差值的最小值。
# 
# 
# 提示：
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
# 0 <= p <= (nums.length)/2
# 
#

from math import inf
from typing import List
# @lc code=start
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)-1
        diff = [nums[i+1]-nums[i] for i in range(n)]
        if p == 0:
            return 0
        
        def check(x: int) -> bool:
            '''
            测试是否可以从diff中选出p个彼此不相邻的数，使其最大值不超过x。可以返回true，不行返回false
            '''
            cnt = i = 0
            while i < n:
                if diff[i] <= x:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= p
        
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            mid = (l + r) >> 1
            if check(mid):
                r = mid
            else:
                l = mid + 1

        return l

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimizeMax([10,1,2,7,1,3], 2)) # 1
    print(solution.minimizeMax([4,2,1,2], 1)) # 0
