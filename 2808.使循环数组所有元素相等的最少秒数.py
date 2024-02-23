#
# @lc app=leetcode.cn id=2808 lang=python3
#
# [2808] 使循环数组所有元素相等的最少秒数
#
# 给你一个下标从 0 开始长度为 n 的数组 nums 。

# 每一秒，你可以对数组执行以下操作：

# 对于范围在 [0, n - 1] 内的每一个下标 i ，将 nums[i] 替换成 nums[i] ，nums[(i - 1 + n) % n] 或者 nums[(i + 1) % n] 三者之一。
# 注意，所有元素会被同时替换。

# 请你返回将数组 nums 中所有元素变成相等元素所需要的 最少 秒数。


# 示例 1：
# 输入：nums = [1,2,1,2]
# 输出：1
# 解释：我们可以在 1 秒内将数组变成相等元素：
# - 第 1 秒，将每个位置的元素分别变为 [nums[3],nums[1],nums[3],nums[3]] 。变化后，nums = [2,2,2,2] 。
# 1 秒是将数组变成相等元素所需要的最少秒数。

# 示例 2：
# 输入：nums = [2,1,3,3,2]
# 输出：2
# 解释：我们可以在 2 秒内将数组变成相等元素：
# - 第 1 秒，将每个位置的元素分别变为 [nums[0],nums[2],nums[2],nums[2],nums[3]] 。变化后，nums = [2,3,3,3,3] 。
# - 第 2 秒，将每个位置的元素分别变为 [nums[1],nums[1],nums[2],nums[3],nums[4]] 。变化后，nums = [3,3,3,3,3] 。
# 2 秒是将数组变成相等元素所需要的最少秒数。

# 示例 3：
# 输入：nums = [5,5,5,5]
# 输出：0
# 解释：不需要执行任何操作，因为一开始数组中的元素已经全部相等。
 

# 提示：
# 1 <= n == nums.length <= 10^5
# 1 <= nums[i] <= 10^9

from collections import defaultdict
from math import inf
from typing import List
# @lc code=start
class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        # 要把nums都变成x（x是nums已经存在的元素），其时间为nums中相邻x之间的最大距离除以2
        pos = defaultdict(list)
        n = len(nums)
        for i, num in enumerate(nums):
            pos[num].append(i)

        # 异常看每个x，其间隔的最大值
        res = inf
        for x in pos.keys():
            p = pos[x]
            span = max(p[i+1] - p[i] for i in range(len(p) - 1)) if len(p) > 1 else 0
            span = max(span, p[0] + n - p[-1])
            res = min(res, span >> 1)

        return res

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumSeconds([2,1,3,3,2])) # 2
    print(solution.minimumSeconds([1,2,1,2])) # 1
    print(solution.minimumSeconds([5,5,5,5])) # 0