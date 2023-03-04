#
# @lc app=leetcode.cn id=982 lang=python3
#
# [982] 按位与为零的三元组
#
# 给你一个整数数组 nums ，返回其中 按位与三元组 的数目。

# 按位与三元组 是由下标(i, j, k) 组成的三元组，并满足下述全部条件：

# 0 <= i < nums.length
# 0 <= j < nums.length
# 0 <= k < nums.length
# nums[i] & nums[j] & nums[k] == 0 ，其中 & 表示按位与运算符。

# 示例 1：
# 输入：nums = [2, 1, 3]
# 输出：12
# 解释：可以选出如下 i, j, k 三元组：
# (i=0, j=0, k=1): 2 & 2 & 1
# (i=0, j=1, k=0): 2 & 1 & 2
# (i=0, j=1, k=1): 2 & 1 & 1
# (i=0, j=1, k=2): 2 & 1 & 3
# (i=0, j=2, k=1): 2 & 3 & 1
# (i=1, j=0, k=0): 1 & 2 & 2
# (i=1, j=0, k=1): 1 & 2 & 1
# (i=1, j=0, k=2): 1 & 2 & 3
# (i=1, j=1, k=0): 1 & 1 & 2
# (i=1, j=2, k=0): 1 & 3 & 2
# (i=2, j=0, k=1): 3 & 2 & 1
# (i=2, j=1, k=0): 3 & 1 & 2

# 示例 2：
# 输入：nums = [0, 0, 0]
# 输出：27


# 提示：
# 1 <= nums.length <= 1000
# 0 <= nums[i] < 2^16

# Hard
# 复习

from typing import List
# @lc code=start


class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        # 求ub是为了压缩一下状态
        ub = 1  # ub为比nums最大值大的最小2的整数次幂
        for n in nums:
            while ub <= n:  # 等于这种情况，ub也是要翻倍的
                ub <<= 1

        cnt = [0] * ub
        for n in nums:
            n ^= ub - 1  # 转换为补集
            s = n
            while s:  # 枚举补集的非空子集
                cnt[s] += 1  # cnt[s] 记录的是nums中能和 s 与为 0 的数字个数
                s = (s - 1) & n  # 求下一个子集（子集状压 DP常用技巧）
        cnt[0] = len(nums)  # nums中所有的数和0与都是0 (直接统计空子集)

        return sum(cnt[x & y] for x in nums for y in nums)

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.countTriplets([1, 1, 1]))  # 0
    print(solution.countTriplets([2, 1, 3]))  # 12
    print(solution.countTriplets([0, 0, 0]))  # 27
