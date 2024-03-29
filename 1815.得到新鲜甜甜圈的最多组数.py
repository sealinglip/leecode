#
# @lc app=leetcode.cn id=1815 lang=python3
#
# [1815] 得到新鲜甜甜圈的最多组数
#
# 有一个甜甜圈商店，每批次都烤 batchSize 个甜甜圈。这个店铺有个规则，就是在烤一批新的甜甜圈时，之前 所有 甜甜圈都必须已经全部销售完毕。给你一个整数 batchSize 和一个整数数组 groups ，数组中的每个整数都代表一批前来购买甜甜圈的顾客，其中 groups[i] 表示这一批顾客的人数。每一位顾客都恰好只要一个甜甜圈。

# 当有一批顾客来到商店时，他们所有人都必须在下一批顾客来之前购买完甜甜圈。如果一批顾客中第一位顾客得到的甜甜圈不是上一组剩下的，那么这一组人都会很开心。

# 你可以随意安排每批顾客到来的顺序。请你返回在此前提下，最多 有多少组人会感到开心。


# 示例 1：
# 输入：batchSize = 3, groups = [1, 2, 3, 4, 5, 6]
# 输出：4
# 解释：你可以将这些批次的顾客顺序安排为[6, 2, 4, 5, 1, 3] 。那么第 1，2，4，6 组都会感到开心。

# 示例 2：
# 输入：batchSize = 4, groups = [1, 3, 2, 5, 2, 2, 1, 6]
# 输出：4


# 提示：
# 1 <= batchSize <= 9
# 1 <= groups.length <= 30
# 1 <= groups[i] <= 10^9

# Hard
# 复习

from collections import Counter
from functools import cache
from typing import List
# @lc code=start


class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        # 要求groups凑出尽可能多的batchSize的整数倍来
        # 动规
        cnt = Counter(x % batchSize for x in groups)  # 所有的顾客团体按batchSize求余，再计数
        # 每种情况的数量不可能超过groups的总数，那么5位二进制可以存下
        kWidth = 5
        kMask = (1 << kWidth) - 1

        # 构造初始mask
        start = 0
        for i in range(batchSize - 1, 0, -1):  # 不包含余数为0的情况，这些团体统一都排在最前面的，可以都happy
            start = (start << kWidth) | cnt[i]

        @cache
        def dfs(mask: int) -> int:
            if mask == 0:
                return 0

            total = 0  # 总和
            for i in range(1, batchSize):
                # i 代表group % batchSize
                amount = ((mask >> ((i - 1) * kWidth)) & kMask)
                total += i * amount

            best = 0
            for i in range(1, batchSize):
                amount = ((mask >> ((i - 1) * kWidth)) & kMask)
                if amount > 0:
                    # 状态转移：设把余数为i的一组放到最后
                    dp = dfs(mask - (1 << (i - 1) * kWidth))
                    if (total - i) % batchSize == 0:
                        dp += 1
                    best = max(best, dp)
            return best

        res = dfs(start) + cnt[0]
        dfs.cache_clear()
        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxHappyGroups(3, [1, 2, 3, 4, 5, 6]))  # 4
    print(solution.maxHappyGroups(4, [1, 3, 2, 5, 2, 2, 1, 6]))  # 4
