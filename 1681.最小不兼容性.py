#
# @lc app=leetcode.cn id=1681 lang=python3
#
# [1681] 最小不兼容性
#
# 给你一个整数数组 nums​​​ 和一个整数 k 。你需要将这个数组划分到 k 个相同大小的子集中，使得同一个子集里面没有两个相同的元素。

# 一个子集的 不兼容性 是该子集里面最大值和最小值的差。

# 请你返回将数组分成 k 个子集后，各子集 不兼容性 的 和 的 最小值 ，如果无法分成分成 k 个子集，返回 - 1 。

# 子集的定义是数组中一些数字的集合，对数字顺序没有要求。


# 示例 1：
# 输入：nums = [1, 2, 1, 4], k = 2
# 输出：4
# 解释：最优的分配是[1, 2] 和[1, 4] 。
# 不兼容性和为(2-1) + (4-1) = 4 。
# 注意到[1, 1] 和[2, 4] 可以得到更小的和，但是第一个集合有 2 个相同的元素，所以不可行。

# 示例 2：
# 输入：nums = [6, 3, 8, 1, 3, 1, 2, 2], k = 4
# 输出：6
# 解释：最优的子集分配为[1, 2]，[2, 3]，[6, 8] 和[1, 3] 。
# 不兼容性和为(2-1) + (3-2) + (8-6) + (3-1) = 6 。

# 示例 3：
# 输入：nums = [5, 3, 3, 6, 3, 3], k = 3
# 输出：- 1
# 解释：没办法将这些数字分配到 3 个子集且满足每个子集里没有相同数字。

# 提示：
# 1 <= k <= nums.length <= 16
# nums.length 能被 k 整除。
# 1 <= nums[i] <= nums.length

# Hard
# 复习

#  下面 ：从小往大填充集合的思路不对，用例2通不过
#  set_info = [[-1, -1, len(nums) // k]
#               for _ in range(k)]  # 记录每个分组的最小、最大值、空位个数
#   set_idx = 0  # 当前还有空位的最前子集序号
#    for i in sorted(cnt.keys()):
#         c = cnt[i]  # 当前数字的个数
#         for j in range(c):
#             if set_info[set_idx+j][0] == -1:
#                 set_info[set_idx+j][0] = i
#             set_info[set_idx+j][2] -= 1

#         while set_idx < k and set_info[set_idx][2] == 0:
#             set_info[set_idx][1] = i
#             set_idx += 1

#     return sum(ma - mi for mi, ma, _ in set_info)

from collections import Counter
from functools import cache
from math import inf
from typing import List
# @lc code=start


class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        if cnt.most_common(1)[0][1] > k:
            # 抽屉原理，没办法划分成k个不含相同元素的子集
            return -1

        n = len(nums)
        size = n // k  # 每个集合大小
        nums.sort()

        # 记忆化搜索
        @cache
        def dfs(left: int, pre: int) -> int:
            '''
            left：剩余数字对应mask
            pre: 前一个数在数组中的索引
            '''
            if left == 0:
                return 0
            if left.bit_count() % size == 0:  # 建新子集
                lb = left & -left  # 取最低位的1
                return dfs(left ^ lb, lb.bit_length() - 1)
            res = inf
            last = nums[pre]
            for i in range(pre + 1, n):  # 枚举本子集的下一个数
                if left >> i & 1 and nums[i] != last:  # 不能有重复数字
                    last = nums[i]
                    res = min(res, last - nums[pre] + dfs(left ^ (1 << i), i))
            return res

        return dfs((1 << n) - 2, 0)


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumIncompatibility([1, 2, 1, 4], 2))  # 4
    print(solution.minimumIncompatibility([6, 3, 8, 1, 3, 1, 2, 2], 4))  # 6
    print(solution.minimumIncompatibility([5, 3, 3, 6, 3, 3], 3))  # -1
