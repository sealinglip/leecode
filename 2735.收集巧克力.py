#
# @lc app=leetcode.cn id=2735 lang=python3
#
# [2735] 收集巧克力
#
# 给你一个长度为 n 、下标从 0 开始的整数数组 nums ，表示收集不同巧克力的成本。每个巧克力都对应一个不同的类型，最初，位于下标 i 的巧克力就对应第 i 个类型。

# 在一步操作中，你可以用成本 x 执行下述行为：

# 同时修改所有巧克力的类型，将巧克力的类型 ith 修改为类型 ((i + 1) mod n)th。
# 假设你可以执行任意次操作，请返回收集所有类型巧克力所需的最小成本。

 

# 示例 1：
# 输入：nums = [20,1,15], x = 5
# 输出：13
# 解释：最开始，巧克力的类型分别是 [0,1,2] 。我们可以用成本 1 购买第 1 个类型的巧克力。
# 接着，我们用成本 5 执行一次操作，巧克力的类型变更为 [1,2,0] 。我们可以用成本 1 购买第 2 个类型的巧克力。
# 然后，我们用成本 5 执行一次操作，巧克力的类型变更为 [2,0,1] 。我们可以用成本 1 购买第 0 个类型的巧克力。
# 因此，收集所有类型的巧克力需要的总成本是 (1 + 5 + 1 + 5 + 1) = 13 。可以证明这是一种最优方案。

# 示例 2：
# 输入：nums = [1,2,3], x = 4
# 输出：6
# 解释：我们将会按最初的成本收集全部三个类型的巧克力，而不需执行任何操作。因此，收集所有类型的巧克力需要的总成本是 1 + 2 + 3 = 6 。
 

# 提示：
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10^9
# 1 <= x <= 10^9

from typing import List
# @lc code=start
class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        res = sum(nums)
        cp = nums[:]

        for j in range(1, n):
            for i in range(n):
                cp[i] = min(cp[i], nums[(i + j) % n])
            res = min(res, j * x + sum(cp))

        return res
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.minCost([20,1,15], 5)) # 13
    print(solution.minCost([1,2,3], 4)) # 6
