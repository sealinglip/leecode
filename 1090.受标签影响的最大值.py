#
# @lc app=leetcode.cn id=1090 lang=python3
#
# [1090] 受标签影响的最大值
#
# 我们有一个 n 项的集合。给出两个整数数组 values 和 labels ，第 i 个元素的值和标签分别是 values[i] 和 labels[i]。还会给出两个整数 numWanted 和 useLimit 。

# 从 n 个元素中选择一个子集 s:

# 子集 s 的大小 小于或等于 numWanted 。
# s 中 相同标签最多 不超过 useLimit 项。
# 一个子集的 分数 是该子集的值之和。

# 返回子集 s 的最大 分数 。


# 示例 1：
# 输入：values = [5, 4, 3, 2, 1], labels = [1, 1, 2, 2, 3], numWanted = 3, useLimit = 1
# 输出：9
# 解释：选出的子集是第一项，第三项和第五项。

# 示例 2：
# 输入：values = [5, 4, 3, 2, 1], labels = [1, 3, 3, 3, 2], numWanted = 3, useLimit = 2
# 输出：12
# 解释：选出的子集是第一项，第二项和第三项。

# 示例 3：
# 输入：values = [9, 8, 8, 7, 6], labels = [0, 0, 0, 1, 1], numWanted = 3, useLimit = 1
# 输出：16
# 解释：选出的子集是第一项和第四项。


# 提示：
# n == values.length == labels.length
# 1 <= n <= 2 * 10^4
# 0 <= values[i], labels[i] <= 2 * 10^4
# 1 <= numWanted, useLimit <= n

from collections import defaultdict
from typing import List
# @lc code=start


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        pairs = sorted(zip(values, labels), reverse=True)  # 按分值降序
        res = 0
        cnt = defaultdict(int)
        for v, l in pairs:
            if cnt[l] < useLimit:
                res += v
                numWanted -= 1
                cnt[l] += 1
            if numWanted == 0:
                break

        return res
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.largestValsFromLabels(
        [5, 4, 3, 2, 1], [1, 1, 2, 2, 3], 3, 1))  # 9
    print(solution.largestValsFromLabels(
        [5, 4, 3, 2, 1], [1, 3, 3, 3, 2], 3, 2))  # 12
    print(solution.largestValsFromLabels(
        [9, 8, 8, 7, 6], [0, 0, 0, 1, 1], 3, 1))  # 16
